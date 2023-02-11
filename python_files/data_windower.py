#!/usr/bin/env python
# coding: utf-8

import numpy
import pandas as pd
from configuration import Config, FilePaths

FILE_PATHS = FilePaths()
output_adjusted_timesteps: bool = True
rearranged_df_as_read = pd.read_csv(FILE_PATHS.REARRANGED_DATA, dtype=str)
rearranged_df = rearranged_df_as_read.copy()
rearranged_df.set_index("Patient Id", inplace=True)
rearranged_df = rearranged_df.dropna()
rearranged_df


def fit_data_to_timesteps(
    df, verbose: bool = Config.verbose, pad_timesteps: bool = True
) -> list[list]:
    """Converts pandas datastep to timestream. 

    Args:
        df (Dataframe): Patient dataframe, with each row being a patient
        verbose (bool, optional): _description_. Defaults to False.
        pad_timesteps (bool, optional): _description_. Defaults to True.

    Returns:
        list[list]: _description_
    """    
    patient_id_set: set = set(df.index)
    time_stamps: list = [str(x) for x in range(1, 365 + 1)]
    ehr_stream: list = []
    for patient_id in patient_id_set:
        element = df.index.get_loc(patient_id)
        if verbose is True:
            print("-" * 56)
            print(f"Patient: {element}")
            print("-" * 56)
        for (colname, colvalue) in df.iloc[element].iteritems():
            if colvalue not in time_stamps:
                end_timestep: int = int(Config.time_step) + int(colname)
                clamped_end_timestep: int = numpy.clip(end_timestep, 0, 365)
                row_slice = df.iloc[element]
                if verbose is True:
                    print(f"Visit found")
                    print(f"Timestep with entry: {colname}")
                    print(f"Timestep to go up till: { clamped_end_timestep}")
                    print("_" * 56)
                data_stream = row_slice.iloc[
                    int(colname) : int(clamped_end_timestep)
                ].to_list()

                # Pad timestreams to timestep length
                if len(data_stream) < Config.time_step:
                    diff: int = Config.time_step - len(data_stream)
                    pad_stream: list = [str('<pad>') for x in range(1, diff + 1)]
                    data_stream.extend(pad_stream)

                # Add count from previous timesteps
                ehr_stream.append(
                  data_stream
                )
    return ehr_stream


ehr_stream: list = fit_data_to_timesteps(rearranged_df)

def add_time_since_last_vist(time_stream: list[list], verbose: bool = Config.verbose) -> list[list]:
    """Adjusts a timestream to count time since the last visit. 
        i.e. 
        from ['Visit', '1', '2', '3', 'Visit', '5', '6']
        to ['Visit', '1', '2', '3', 'Visit', '1', '2']

    Args:
        time_stream (list[list]): Unadjusted patient timestream
        verbose (bool, optional): Output information. Defaults to False.

    Returns:
        list[list]: Adjusted timestream
    """    
    adjusted_time_stream: list = []
    for index, _ in enumerate(time_stream):
        inner_lst = [int(s) if s.isdigit() else s for s in ehr_stream[index]]
        adjusted_inner_lst: list = []
        count = 0
        for inner_index, inner_element in enumerate(inner_lst):
            if(type(inner_element) == str):
                adjusted_inner_lst.append(inner_element)
                if verbose: print(f'index of {inner_index} is a string, count reset')
                count = 0
            if count != 0:
                if verbose: print(f'Times since last visit {count}')
                adjusted_inner_lst.append(str(count))
            count += 1
        adjusted_time_stream.append(adjusted_inner_lst)
    return adjusted_time_stream
if output_adjusted_timesteps: ehr_stream =  add_time_since_last_vist(ehr_stream)       

