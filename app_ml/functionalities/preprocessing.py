from sklearn.utils import shuffle
from sklearn.preprocessing import LabelEncoder
from app_ml.functionalities.constants import TRAFFIC_MAP, SURFACE_MAP, GENERATED_DATA_PATH, FOLDERS
import pandas as pd
import os

def get_all_csv_files_from_folder(folder):
    files = os.listdir(GENERATED_DATA_PATH + '/' + folder)
    files.sort()
    files.sort(key=len)
    return files

def preprocess_dataframe(df, columns):
    df_data = df.drop(columns=columns, axis=1)
    df_data = df_data.replace({'roadSurface': SURFACE_MAP, 'traffic': TRAFFIC_MAP})
    return df_data

def window_df_and_append_to_list(window, columns, df, final_data, final_labels):
    df_data = preprocess_dataframe(df, columns)
    for i in range(0, df_data.shape[0] - window + 1):
        final_data.append(df_data.iloc[i:(i + window), :].values)
        final_labels.append(df.iloc[window - 1 + i]['drivingStyle'])
    return final_data, final_labels

def list_of_windowed_dfs_to_one_df(final_data, final_labels):
    final_data_df = pd.DataFrame({'sequence': final_data})
    final_labels_df = pd.DataFrame({'drivingStyle': final_labels})
    final_labels_df['drivingStyleEncoded'] = final_labels_df.apply(LabelEncoder().fit_transform)
    return final_data_df, final_labels_df

def create_dataset_window(window_size, folders):
    final_data = []
    final_labels = []
    for folder in folders:
        files = get_all_csv_files_from_folder(folder)
        for file in files:
            df = pd.read_csv(GENERATED_DATA_PATH + '/' + folder + '/' + file)
            final_data, final_labels = window_df_and_append_to_list(window_size, ['drivingStyle', 'AltitudeVariation', 'VehicleSpeedInstantaneous'], df, final_data, final_labels)
    final_data_df, final_labels_df = list_of_windowed_dfs_to_one_df(final_data, final_labels)
    return final_data_df, final_labels_df

def create_dataset(window_size=1, folders=FOLDERS):
    if window_size > 1:
        return create_dataset_window(window_size, folders)
    dfs = []
    for folder in folders:
        files = get_all_csv_files_from_folder(folder)
        folder_dfs = [pd.read_csv(GENERATED_DATA_PATH + '/' + folder + '/' + file) for file in files]
        folder_df = pd.concat(folder_dfs, axis=0).reset_index(drop=True)
        dfs.append(folder_df)
    df = pd.concat(dfs).reset_index(drop=True)
    df = shuffle(df)
    df_data = preprocess_dataframe(df, ['drivingStyle', 'AltitudeVariation', 'VehicleSpeedInstantaneous'])
    labels = pd.DataFrame()
    labels['drivingStyle'] = df['drivingStyle']
    labels['drivingStyleEncoded'] = labels.apply(LabelEncoder().fit_transform)
    return df_data, labels

def create_test_set(window_size=1, file='yo'):
    x_test, labels_test = create_dataset(window_size, [file])
    y_test = labels_test['drivingStyleEncoded']
    if window_size > 1:
        return x_test['sequence'], y_test    
    return x_test, y_test
