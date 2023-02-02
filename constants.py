import os

# HOME_DIR:str = '/home/aaron/timeseries_nlp'
cwd = os.getcwd()
HOME_DIR: str = cwd

DATA_DIR: str = "/home/aaron/aaron_data/"
UPDATED_DATA_DIR: str = "/home/aaron/updated_data"
RAW_DF: str = os.path.join(DATA_DIR, "combined_documents.csv")
PATIENT_LEVEL_DF: str = os.path.join(
    UPDATED_DATA_DIR, "secondary_patient_level_annotations_v1.csv"
)
PROBLEM_LEVEL_DF: str = os.path.join(
    UPDATED_DATA_DIR, "secondary_problem_level_annotations_v1.csv"
)
REARRANGED_DATA_FILEPATH: str = os.path.join(
    "/home/aaron/timeseries_nlp/data/", "rearranged_data.csv"
)
REARRANGED_DATA_FILEPATH_FLAT: str = os.path.join(
    "/home/aaron/timeseries_nlp/data/", "rearranged_data_flat.csv"
)

SEED:int = 2023

TIME_STEP: int = 30