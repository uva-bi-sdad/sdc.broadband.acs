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


def extract_acs_variable(variable, force=False):
    # Look for variable descriptions here: https://api.census.gov/data/2021/acs/acs5/variables.html

    ga_census = c.acs5.state_county_blockgroup(
        fields=(
            "NAME",
            variable + "_001E",
            variable + "_001M",
            variable + "_001MA",
        ),
        state_fips=states.AL.fips,
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
    ga_df[ga_df[variable + "_001E"] < 0].value_counts()
    data_dir = "../../data/distribution/" + variable
    os.system("mkdir -p %s" % data_dir)  # Make a directory if it does not exist
    assert os.path.isdir(data_dir)
    counties = sorted(ga_df["GEOID21"].str[:5].unique())
    for county in tqdm(counties):
        pdf = ga_df[ga_df["GEOID21"].str[:5] == county]
        export_path = os.path.join(data_dir, "{county}.csv.xz".format(county=county))
        if not force and os.path.isfile(export_path):
            continue
        pdf.to_csv(export_path, index=False)


if __name__ == "__main__":
    variables = ["B19013", "B28002"]
    vpbar = tqdm(variables)
    for v in vpbar:
        vpbar.set_description("Parsing: %s" % v)
        extract_acs_variable(v, force=True)
