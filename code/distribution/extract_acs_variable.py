import pandas as pd
import geopandas as gpd
from census import Census
from us import states
import pathlib
import os
from tqdm import tqdm
from decouple import Config, RepositoryEnv

config = Config(RepositoryEnv(".env"))
c = Census(config("CENSUS_API_KEY"), year=2021)


def extract_acs_variables(variable, states):
    dfs = []
    pbar = tqdm(states)
    for state in pbar:
        pbar.set_description(
            "Downloading {variable} for {state}".format(variable=variable, state=state)
        )
        ga_census = c.acs5.state_county_blockgroup(
            fields=(
                "NAME",
                variable + "E",
                variable + "M",
                variable + "MA",
            ),
            state_fips=state,
            county_fips="*",
            tract="*",
            blockgroup="*",
        )

        # Create a dataframe from the census data
        ga_df = pd.DataFrame(ga_census)
        ga_df["GEOID21"] = (
            ga_df["state"] + ga_df["county"] + ga_df["tract"] + ga_df["block group"]
        )
        ga_df = ga_df.drop(columns=["NAME", "state", "county", "tract", "block group"])
        dfs.append(ga_df)
    return pd.concat(dfs)


def save_variable(variable, force=False):
    # Look for variable descriptions here: https://api.census.gov/data/2021/acs/acs5/variables.html

    data_dir = "../../data/distribution/" + variable
    os.system("mkdir -p %s" % data_dir)  # Make a directory if it does not exist
    assert os.path.isdir(data_dir)
    assert variable is not None
    df = extract_acs_variables(variable, [states.AL.fips, states.GA.fips])

    counties = sorted(df["GEOID21"].str[:5].unique())
    pbar = tqdm(counties)
    for county in pbar:
        pdf = df[df["GEOID21"].str[:5] == county]
        export_path = os.path.join(data_dir, "{county}.csv.xz".format(county=county))
        if not force and os.path.isfile(export_path):
            continue
        pdf.to_csv(export_path, index=False)
        pbar.set_description("Saved to: %s" % export_path)


if __name__ == "__main__":
    variables = [
        "B19013_001",
        "B28001_001",
        "B28001_002",
        "B28002_001",
        "B28002_004",
        "B28002_007",
        "B28002_013",
    ]
    vpbar = tqdm(variables)
    for v in vpbar:
        vpbar.set_description("Parsing: %s" % v)
        save_variable(v, force=True)
