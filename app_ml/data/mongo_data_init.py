from app_ml.functionalities.constants import MONGO_URL, ORIGINAL_DATA_PATH
import pandas as pd
import sys
import pymongo
import uuid

FILES = [
    'opel_corsa_01.csv', 
    'opel_corsa_02.csv'
    # 'peugeot_207_01.csv'
    # 'peugeot_207_02.csv'
]

def create_db():
    try:
        conn = pymongo.MongoClient(MONGO_URL)
        if 'cars' in conn.list_database_names():
            conn.drop_database('cars')
        cars_db = conn['cars']
        cars_db['routes']
        print('Mongo database created successfully')
    except:
        print('Unexpected error:', sys.exc_info()[0])
        raise

def read_file(file, driver_id, route_id):
    df = pd.read_csv(file, delimiter=';', decimal=',')
    df['DriverId'] = driver_id
    df['Timestamp'] = df.index + 1
    df['RouteId'] = route_id
    df = df.reset_index(drop=True)
    data = df.to_dict('records')
    return data

def insert_data(file, db, driver_id):
    route_id = uuid.uuid4().hex
    data = read_file(file, driver_id, route_id)
    db['routes'].insert_many(data)

def main():
    create_db()
    cars_db = pymongo.MongoClient(MONGO_URL)['cars']
    driver_id = 1
    for file in FILES:
        insert_data(ORIGINAL_DATA_PATH + '/' + file, cars_db, driver_id)
        # If uncommented we will have two drivers instead of one
        driver_id += 1
        
    print('Data inserted successfully to MongoDB')

if __name__ == "__main__":
    main()