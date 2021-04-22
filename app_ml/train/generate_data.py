from pprint import pprint
from shutil import rmtree
from app_ml.functionalities.constants import FILES, GENERATED_DATA_PATH, ORIGINAL_DATA_PATH
import pandas as pd
import numpy as np
import os

def print_analysis(df, df_full, df_empty, dfs):
    pprint('======================================================')
    pprint(df.shape)
    pprint(df_full.shape)
    pprint(df_empty.shape)
    pprint(len(dfs))
    pprint(min(map(len, dfs)))
    pprint('======================================================')

def generate(file, dfs):
    try:
        os.mkdir(GENERATED_DATA_PATH + '/' + file)
    except FileExistsError:
        rmtree(GENERATED_DATA_PATH + '/' + file)
        os.mkdir(GENERATED_DATA_PATH + '/' + file)
    for i in range(0, len(dfs)):
        # temp_df = dfs[i].drop(columns=['roadSurface', 'traffic'], axis=1) 
        temp_df = dfs[i]
        temp_df.to_csv(GENERATED_DATA_PATH + '/' + file + '/data{0}.csv'.format(i),index=False, header=True)

def main():
    for file in FILES:
        df = pd.read_csv(ORIGINAL_DATA_PATH + '/{0}.csv'.format(file), delimiter=';', decimal=',')
        df_full = df.dropna(axis=0)
        # df_empty = df[df.isna().any(axis=1)]
        dfs = [d for _, d in df_full.groupby(df_full.index - np.arange(len(df_full)))]
        # pprint(file)
        # print_analysis(df, df_full, df_empty, dfs)
        generate(file, dfs)
    print('CSV files generated and stored at {0}'.format(GENERATED_DATA_PATH))
    
if __name__ == '__main__':
    main()