from app_ml.functionalities.preprocessing import window_df_and_append_to_list,list_of_windowed_dfs_to_one_df
from app_ml.functionalities.constants import WINDOW
import pymongo
import numpy as np
import pandas as pd

def split_dataframe(df):
    dfs = [d.reset_index(drop=True) for _, d in df.groupby(df.index - np.arange(len(df)))]
    return dfs

def generate_final_dataframe_mongo(dataframes):
    final_data = []
    final_labels = []
    for dataframe in dataframes:
        dataframe = dataframe.dropna(axis=0, how='any')
        dfs = split_dataframe(dataframe)
        for df in dfs:
            final_data, final_labels = window_df_and_append_to_list(WINDOW, ['drivingStyle', 'AltitudeVariation', 'VehicleSpeedInstantaneous', 'Timestamp', 'DriverId', 'RouteId', '_id'], df, final_data, final_labels)
    final_data_df, final_labels_df = list_of_windowed_dfs_to_one_df(final_data, final_labels)
    return final_data_df, final_labels_df

def read_from_mongo_as_dataframe(cars_db):
    routes_collection = cars_db['routes']
    cursor = routes_collection.aggregate(
        [
            {'$group': {'_id': {'DriverId': '$DriverId', 'RouteId': '$RouteId'}}}
        ]
    )
    driver_route_ids = [(d['_id']['DriverId'], d['_id']['RouteId']) for d in cursor]
    dfs = []
    for t in driver_route_ids:
        cursor = routes_collection.find(
            {'$and': [
                    {'DriverId': t[0]},
                    {'RouteId': t[1]}
                ]
            },
        ).sort('Timestamp', pymongo.ASCENDING)
        df = pd.DataFrame(list(cursor))
        dfs.append(df)
    data, labels = generate_final_dataframe_mongo(dfs)
    return data, labels
    