# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: tf
#     language: python
#     name: python3
# ---

# +
import os

import numpy as np
import pandas as pd
from configuration import Config, FilePaths
from tqdm import tqdm

# Set seeds to ensure reproduceability
np.random.seed(Config.seed)
os.environ["PYTHONHASHSEED"] = str(Config.seed)

FILE_PATHS = FilePaths()
# -

# # Organise data from Vetcompass' EHRs into a pandas dataframe, where each row represents a single patient, and each column represents a calendar day of the year.  

# Load up the saved CSV's from VetCompass

# Read all three CSVs into a pandas data frame (I was provided with a combined_documents.csv, secondary_patient_level_annotations.csv and a secondary_problem_level_annotations.csv)
for i in tqdm(range(0, 3), ncols=100, desc="Loading data.."):
    raw_df_as_read = pd.read_csv(FILE_PATHS.RAW_DATA)
    patient_level_annotations_as_read = pd.read_csv(FILE_PATHS.PATIENT_LEVEL_DATA)
    problem_level_annotations_as_read = pd.read_csv(FILE_PATHS.PROBLEM_LEVEL_DATA)
print("------Loading is completed ------")

# - We are given lots of extraeneous information, so lets strip non relavent data. Note that patient ID is unique to each patient. 
# - Firstly we create a copy of the data, create an additional column called Date which contains the date record was made
# - Then we drop unnessicary columns, and filter all records by the study date (1/1/2019 -> 31/12/2019)

# +
raw_df = raw_df_as_read.copy()

# Then we split the recorded date to DateTimeDay column, so we can get concat records existing on a single day"
raw_df[["DateTimeDay", "DateTimeSeconds"]] = raw_df["RecordedDate"].str.split(
    "T", expand=True
)
raw_df["Date"] = pd.to_datetime(raw_df["DateTimeDay"], format="%Y-%m-%d")


raw_df.drop(
    Config.raw_data_columns_drop, axis=1, inplace=True, errors="ignore"
)  # Drop un-needed columns
raw_df = raw_df[
    (raw_df["Date"] >= Config.study_start_date)
    & (raw_df["Date"] <= Config.study_end_date)
]  # Only include patients withint study start date
raw_df
# -

patient_level_annotations = patient_level_annotations_as_read.copy()
patient_level_annotations.drop(Config.patient_level_columns_drop, axis=1, inplace=True)
patient_level_annotations

study_patients = set(
    patient_level_annotations.loc[
        patient_level_annotations["Is this patient included in the study_1"] == "Yes",
        "PatientID",
    ].tolist()
)

# +
problem_level_annotations = problem_level_annotations_as_read.copy()

# Drop all patients NOT in study
problem_level_annotations = problem_level_annotations[
    problem_level_annotations.PatientID.isin(study_patients)
]

problem_level_annotations[
    ["DateTimeDay", "DateTimeSeconds"]
] = problem_level_annotations["DocumentDate"].str.split(" ", expand=True)
problem_level_annotations["Date"] = pd.to_datetime(
    problem_level_annotations["DateTimeDay"], format="%d/%m/%Y"
)

problem_level_annotations.drop(Config.problem_level_columns_drop, axis=1, inplace=True)


# -

# Simple function to check if we have multiple entries per day. 

# +
def check_multiple_entries(df) -> list:
    "Check there are not multiple entries per day, if so remove these days from the data pool"
    multiple_entries_list = []
    for i in set(df.PatientID.tolist()):
        results = df.loc[df.PatientID == i]
        if not results.Date.is_unique:
            multiple_entries_list.append(i)
    return multiple_entries_list


df = problem_level_annotations[
    ~problem_level_annotations.PatientID.isin(
        check_multiple_entries(problem_level_annotations)
    )
]

if len(check_multiple_entries(df)) != 0:
    raise Exception("Sorry, but it appears you have multiple categorised days!")

print(f"You have {len(df.PatientID.unique())} patients included in this study")
print(f"and a total of {len(df.index)} 24 hour periods classified")

# +
# Merge the EHRs to the DF
ehrs = []
for index, row in df.iterrows():
    ehr = raw_df[(raw_df.PatientId == row.PatientID) & (raw_df.Date == row.Date)]
    ehr_list = ehr.Document.to_list()
    ehrs.append(" ".join(ehr_list))

df.loc[:, "ehr"] = ehrs.copy()

# +
# Filter only the patient visits
df_patients_visits = df[df[Config.is_visit_column] == "Yes"].copy()
patient_id_set: set = set(df_patients_visits[Config.patient_id_column].values)

tmp_list: list = []

print(f"{len(patient_id_set)} patients included in this study who had a visit")

df_patients_visits["DOY"] = df_patients_visits["Date"].dt.dayofyear
# -

# Create a list of the patients EHR, by replacing the day of year of a premade string with the EHR textual input.

ehr_stream_list: list = []
patient_id_list: list = []
for patient_id in patient_id_set:
    patient_stream: list = [str(x) for x in range(1, 365 + 1)]
    patient_id_list.append(patient_id)
    patient_records = df_patients_visits.loc[
        df_patients_visits[Config.patient_id_column] == patient_id
    ]
    for i in range(len(patient_records)):
        patient_stream[
            patient_records.iloc[[i]].DOY.values[0] - 1
        ] = patient_records.iloc[[i]].ehr.values[0]
    ehr_stream_list.append(patient_stream)

restructured_df = pd.DataFrame(ehr_stream_list)
restructured_df.set_axis(patient_id_list, inplace=True)
restructured_df.index.name = "Patient Id"

restructured_df.to_csv(FILE_PATHS.REARRANGED_DATA)

# A final CSV file has been saved with a patients EHR timestream being predicted as a row. 
# Windowing should occur next
