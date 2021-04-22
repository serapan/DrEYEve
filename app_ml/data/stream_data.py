from json import dumps
from app_ml.functionalities.constants import MONGO_URL
import sys
import pandas as pd
import pymongo
import uuid
import time
import requests
import datetime

# python3 stream_data.py peugeot_207_02.csv

def find_next_driver_id(cars_db):
    routes_collection = cars_db['routes']
    cursor = routes_collection.aggregate(
        [
            {'$group': {'_id': {'DriverId': '$DriverId', 'RouteId': '$RouteId'}}}
        ]
    )
    next_driver_id = max([d['_id']['DriverId'] for d in cursor]) + 1
    return next_driver_id

def read_file(file, driver_id, route_id):
    df = pd.read_csv(file, delimiter=';', decimal=',')
    df['DriverId'] = driver_id
    df['Timestamp'] = df.index + 1
    df['RouteId'] = route_id
    df = df.reset_index(drop=True)
    data = df.to_dict('records')
    return data

def get_date():
    date_now = datetime.datetime.now()
    return datetime.datetime(date_now.year, date_now.month, date_now.day, date_now.hour, date_now.minute, date_now.second)

def stream(data, cars_db):
    headers = {'Content-type': 'application/json'}
    body = dumps({'route_id': data[0]['RouteId'], 'driver_id': data[0]['DriverId'], 'date': str(get_date()), 'is_active': 1})
    requests.post(url='http://localhost:8080/api/routes', data=body, headers=headers).json()
    time.sleep(2)
    for record in data:
        cars_db['routes'].insert_one(record)
        time.sleep(1)
    requests.post(url='http://localhost:8080/api/routes/{0}'.format(data[0]['DriverId']), data={}, headers=headers).json()

def main():
    file = sys.argv[1]
    cars_db = pymongo.MongoClient(MONGO_URL)['cars']
    driver_id = find_next_driver_id(cars_db)
    route_id = uuid.uuid4().hex
    data = read_file(file, driver_id, route_id)
    stream(data, cars_db)    
    

if __name__ == '__main__':
    main()