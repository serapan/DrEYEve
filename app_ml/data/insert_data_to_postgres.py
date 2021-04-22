import os
from pprint import pprint

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from app_ml.functionalities.constants import SPARK_WINDOW, MONGO_URL, WINDOW, SAVED_MODEL_PATH, POSTGRES_URL
from app_ml.functionalities.preprocessing import create_test_set
from app_ml.models.RNN import RNN
from sqlalchemy import create_engine, insert, MetaData, Table
from collections import Counter
import pymongo
import tensorflow as tf
import numpy as np
import datetime

DATES = [datetime.datetime(2021, 2, 17, 9, 13, 27), datetime.datetime(2021, 2, 18, 21, 33, 2)]

FILES = [
    'opel_corsa_01', 
    'opel_corsa_02'
    # 'peugeot_207_01' 
    # 'peugeot_207_02'
]

def read_driver_route_id_from_mongo():
    cars_db = pymongo.MongoClient(MONGO_URL)['cars']
    routes_collection = cars_db['routes']
    cursor = routes_collection.aggregate(
        [
            {'$group': {'_id': {'DriverId': '$DriverId', 'RouteId': '$RouteId'}}}
        ]
    )
    driver_route_ids = [(d['_id']['DriverId'], d['_id']['RouteId']) for d in cursor]
    return driver_route_ids

def predict_for_file(model, file):
    x_test, y_test = create_test_set(WINDOW, file)
    x_test, _ = model.preprocess_test(x_test, y_test)
    predictions = model.model.predict(x_test)
    results = np.argmax(predictions, axis=1)
    return results

def make_scores(results):
    results_count = Counter(results)
    aggressive_count = 0 if results_count.get(0) is None else results_count.get(0)
    normal_count = 0 if results_count.get(1) is None else results_count.get(1)
    total_count = aggressive_count + normal_count
    return aggressive_count / total_count, normal_count / total_count

def make_postgres_data_list(route_id, results):
    data = []
    start = 10
    for i in range(0, len(results)):
        end = start + SPARK_WINDOW - 1
        aggressive_score, normal_score = make_scores(results[i])
        d = {
                'route_id': route_id, 'start_time': start, 'end_time': end,
                'aggressive_score': aggressive_score, 'normal_score': normal_score
            }
        data.append(d)
        start = end + 1
    return data

def insert_to_postgres_db(route_id, driver_id, date, model, engine, file):
    results = predict_for_file(model, file)
    spark_windowed_results = [results[i:SPARK_WINDOW+i] for i in range(0, len(results) - SPARK_WINDOW, SPARK_WINDOW)]
    data = make_postgres_data_list(route_id, spark_windowed_results)
    meta = MetaData(engine)
    routes = Table('routes', meta, autoload=True)
    scores = Table('scores', meta, autoload=True)
    routes_stmt = insert(routes).values({'route_id': route_id, 'user_id': driver_id, 'date': date, 'is_active': 0})
    scores_stmt = insert(scores).values(data)
    conn = engine.connect()
    conn.execute(routes_stmt)
    conn.execute(scores_stmt)
    conn.execute('COMMIT')
    conn.close()
    

def main():
    driver_route_ids = read_driver_route_id_from_mongo()
    model = RNN((20, 15), 2)
    model.model = tf.keras.models.load_model(SAVED_MODEL_PATH, compile=False)
    engine = create_engine(POSTGRES_URL)
    for i in range(0, len(FILES)):
        insert_to_postgres_db(driver_route_ids[i][1], driver_route_ids[i][0], DATES[i], model, engine, FILES[i])
    engine.dispose()
    print('Data inserted successfully to PostgresDB')


if __name__ == '__main__':
    main()