import pandas as pd
import geopandas as gpd
from census import Census
from us import states
import pathlib
import os
from tqdm import tqdm
from decouple import Config, RepositoryEnv
from slugify import slugify
<<<<<<< HEAD:code/distribution/extract_acs_variable.py
=======
import requests
>>>>>>> fcd3f30fcbe6b7db79cfe615b466121f7202c890:code/distribution/extract_acs_variables.py

config = Config(RepositoryEnv(".env"))
YEAR = 2021
c = Census(config("CENSUS_API_KEY"), year=YEAR)


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
                variable + "E",  # Estimate
                variable + "M",  # Margin of Error
                variable + "MA",  # Margin of Error label
            ),
            state_fips=state,
            county_fips="*",
            tract="*",
            blockgroup="*",
        )

        # Create a dataframe from the census data
        ga_df = pd.DataFrame(ga_census)
        ga_df["geoid"] = (
            ga_df["state"]
            + ga_df["county"]
            + ga_df["tract"]
            + ga_df[
                "block group"
            ]  # combine the truncated fips code into a single fips code
        )
        ga_df = ga_df.drop(
            columns=["NAME", "state", "county", "tract", "block group"]
        )  # remove the processed columns
        dfs.append(ga_df)
    return pd.concat(dfs)


def save_variable(variable, force=False):
    # Look for variable descriptions here: https://api.census.gov/data/2021/acs/acs5/variables.html

<<<<<<< HEAD:code/distribution/extract_acs_variable.py
    data_dir = "../../data/distribution/"
=======
    data_dir = "../../data/distribution/"  # + variable
>>>>>>> fcd3f30fcbe6b7db79cfe615b466121f7202c890:code/distribution/extract_acs_variables.py
    os.system("mkdir -p %s" % data_dir)  # Make a directory if it does not exist
    assert os.path.isdir(data_dir)
    assert variable is not None
    df = extract_acs_variables(
        variable,
        [
            states.AL.fips,
            states.GA.fips,
            states.VA.fips,
            states.DC.fips,
            states.MD.fips,
        ],
    )

    counties = sorted(df["geoid"].str[:5].unique())
    pbar = tqdm(counties)
    for county in pbar:
<<<<<<< HEAD:code/distribution/extract_acs_variable.py
        pdf = df[df["GEOID21"].str[:5] == county]
        export_path = os.path.join(
            data_dir,
            "{year}_{county}_{variable}.csv.xz".format(
                year=YEAR, variable=slugify(variable, "-").lower(), county=county
=======
        pdf = df[df["geoid"].str[:5] == county]
        value_vars = list(df.columns)
        value_vars.remove("geoid")
        pdf = pd.melt(pdf, id_vars=["geoid"], value_vars=value_vars)
        pdf["year"] = YEAR

        # Example standard export name 2021_fips-01001_measure-acs-b19013-001_rows-3.csv.xz, note we slugify with measure name to remove underscores
        export_path = os.path.join(
            data_dir,
            "{year}_fips-{county}_measure-acs-{variable}_rows-{row_count}.csv.xz".format(
                year=YEAR, county=county, variable=slugify(variable), row_count=len(pdf)
>>>>>>> fcd3f30fcbe6b7db79cfe615b466121f7202c890:code/distribution/extract_acs_variables.py
            ),
        )
        if not force and os.path.isfile(export_path):
            continue

        # converting the data frame to a standard long format
        expected_cols = requests.get(
            "https://raw.githubusercontent.com/uva-bi-sdad/sdc.metadata/master/data/column_structure.json"
        ).json()
        pdf = pdf.reindex(expected_cols, axis=1)
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
