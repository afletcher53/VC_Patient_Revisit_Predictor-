class Config:
    vocab_size = 20000
    batch_size = 160
    epochs = 50
    labels = ["Visit"]
    cleaned_ehr_column = "rejoined"
    stopword_ehr_column = "stopwords_removed"
    tokenized_ehr_column = "tokenized_ehr"
    target_column = "Visit"
    patient_id_column = "PatientID"
    is_visit_column = "Is this note a visit_2"
    ehr_column = "ehr"
    max_len = 200
    max_features = 5000
    dimensions = 100
    seed: int = 2023
    time_step: int = 30
    study_start_date: str = '2019-1-1'
    study_end_date: str = '2019-12-31'
    time_step_delta:int = time_step - 1
    raw_data_columns_drop = ['Type', 'DateTimeSeconds', 'CaseNumber', 'DataSiloName', 'LatestPatientVersionID']
    patient_level_columns_drop: list = [
 'CaseNumber',
 'LatestPatientVersionID',
 'BreedVeNomID',
 'DataSiloName',
 'VetCompassBreed',
 'SpeciesVeNomID',
 'SourceSpecies',
 'VetCompassSpecies',
 'FirstNoteDate',
 'LatestPatientVersionDate',
 'FirstVersionDate',
 'LastNoteDate',
 'CodingStarted',
 'FirstClinicId',
 'SourceClinicName',
 'IsArchived']

    problem_level_columns_drop: list = [ 'DataSiloName', 'ProblemID', 'VeNomID',
       'VetCompassProblemID', 'TermName', 'Context',
       'TextHighlightedWhenCreated','CodingStarted',
       'CaseNumber', 'LatestPatientVersionID', 'BreedVeNomID',
       'VetCompassBreed', 'SpeciesVeNomID', 'SourceSpecies',
       'VetCompassSpecies', 'FirstVersionDate', 'LatestPatientVersionDate',
       'FirstNoteDate', 'LastNoteDate', 'FirstClinicId', 'SourceClinicName',"DateTimeDay", "DateTimeSeconds","DocumentDate",
 'IsArchived']
    verbose: bool = True

import os


class FilePaths:
    def __init__(self) -> None:
        self.home_directory = os.getcwd()
        self.DATA_DIR = self._DATA_DIR()
        self.UPDATED_DATA_DIR = self._UPDATED_DATA_DIR()
        self.RAW_DATA = self._RAW_DATA()
        self.PATIENT_LEVEL_DATA = self._PATIENT_LEVEL_DATA()
        self.PROBLEM_LEVEL_DATA = self._PROBLEM_LEVEL_DATA()
        self.REARRANGED_DATA = self._REARRANGED_DATA()
        self.SAVED_DATA = self._SAVED_DATA()
        self.EHR_STREAM = self._EHR_STREAM()
        self.TARGET_VALUES = self._TARGET_VALUES()
        self.X_TRAIN = self._X_TRAIN()
        self.X_TEST = self._X_TEST()
        self.Y_TRAIN = self._Y_TRAIN()
        self.Y_TEST = self._Y_TEST()
        self.X_VAL = self._X_VAL()
        self.Y_VAL = self._Y_VAL()
        self.FILE_TO_GLOVE = self._FILE_TO_GLOVE()

    def _SAVED_DATA(self) -> str:
        return os.path.join(self.UPDATED_DATA_DIR, "saved_data.csv")

    def _DATA_DIR(self) -> str:
        return "/home/aaron/aaron_data/"

    def _UPDATED_DATA_DIR(self) -> str:
        return "/home/aaron/updated_data"

    def _RAW_DATA(self) -> str:
        return os.path.join(self.DATA_DIR, "combined_documents.csv")

    def _PATIENT_LEVEL_DATA(self) -> str:
        return os.path.join(self.UPDATED_DATA_DIR, "secondary_patient_level_annotations_v1.csv")
    
    def _PROBLEM_LEVEL_DATA(self) -> str:
        return os.path.join(self.UPDATED_DATA_DIR, "secondary_problem_level_annotations_v1.csv")

    def _REARRANGED_DATA(self) -> str:   
        return os.path.join(self.UPDATED_DATA_DIR, "rearranged_data.csv")

    def _EHR_STREAM(self) -> str:
        return os.path.join(self.UPDATED_DATA_DIR, "ehr_stream.pkl")

    def _TARGET_VALUES(self) -> str:
        return os.path.join(self.UPDATED_DATA_DIR, "target_values.pkl")

    def _X_TRAIN(self) -> str:
        return os.path.join(self.UPDATED_DATA_DIR, "x_train.pkl")

    def _X_TEST(self) -> str:
        return os.path.join(self.UPDATED_DATA_DIR, "x_test.pkl")

    def _Y_TRAIN(self) -> str:
        return os.path.join(self.UPDATED_DATA_DIR, "y_train.pkl")

    def _Y_TEST(self) -> str:
        return os.path.join(self.UPDATED_DATA_DIR, "y_test.pkl")

    def _X_VAL(self) -> str:
        return os.path.join(self.UPDATED_DATA_DIR, "x_val.pkl")

    def _Y_VAL(self) -> str:
        return os.path.join(self.UPDATED_DATA_DIR, "y_val.pkl")

    def _FILE_TO_GLOVE(self) -> str:
        return os.path.join(self.UPDATED_DATA_DIR, "glove.6B.100d.txt")
        