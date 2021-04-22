import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql.session import SparkSession
from pyspark import SparkFiles
from sklearn.preprocessing import MinMaxScaler
from json import loads
from collections import Counter
from sqlalchemy import create_engine, insert, MetaData, Table
from app_ml.functionalities.constants import SAVED_MODEL_PATH, TRAFFIC_MAP, SURFACE_MAP, POSTGRES_URL, SPARK_WINDOW
import sqlalchemy as sa
import numpy as np
import pandas as pd
import tensorflow as tf

# sc = SparkContext(master='local[*]', appName='DataReceiver')
sc = SparkContext(appName='DataReceiver')
ssc = StreamingContext(sc, SPARK_WINDOW)
spark = SparkSession(sc)

MODEL = tf.keras.models.load_model(SparkFiles.get(SAVED_MODEL_PATH), compile=False)

ENGINE = create_engine(POSTGRES_URL)

def preprocess_row(row):
    def dict_to_list(d):
        return np.asarray(
            [
                # float(d['VehicleSpeedInstantaneous']), 
                float(d['VehicleSpeedAverage']), 
                float(d['VehicleSpeedVariance']), float(d['VehicleSpeedVariation']), 
                float(d['LongitudinalAcceleration']), float(d['EngineLoad']),
                float(d['EngineCoolantTemperature']), float(d['ManifoldAbsolutePressure']), 
                float(d['EngineRPM']), float(d['MassAirFlow']), float(d['IntakeAirTemperature']), 
                float(d['VerticalAcceleration']), float(d['FuelConsumptionAverage']), 
                float(SURFACE_MAP[d['roadSurface']]), float(TRAFFIC_MAP[d['traffic']])
            ]
        )
    row = loads(row)
    route_id = list(row.keys())[0]
    driver_id = row[route_id][0]['DriverId']
    timestamp = row[route_id][-1]['Timestamp']
    data = row[route_id]
    data = np.asarray([dict_to_list(d) for d in data])
    # data = np.where(np.isnan(data), 0, data)
    return [route_id, driver_id, timestamp, data]

def preprocess_row_2(row):
    scaler = MinMaxScaler(feature_range=(-1, 1))
    route_id = row[0]
    driver_id = row[1][0][0]
    start = row[1][0][1]
    end = row[1][-1][1]
    data = [record[2] for record in row[1]]
    df = pd.DataFrame(columns=['sequence'])
    for i in range(0, len(data)):
        df.at[i, 'sequence'] = data[i]
    data = df['sequence']
    data = data.apply(scaler.fit_transform)
    return [route_id, driver_id, start, end, np.asarray(list(data))]

def predict_and_save_rdd(data):
    def predict(data):
        predictions = MODEL.predict(data)
        results = np.argmax(predictions, axis=1)
        results_count = Counter(results)
        aggressive_count = 0 if results_count.get(0) is None else results_count.get(0)
        normal_count = 0 if results_count.get(1) is None else results_count.get(1)
        total_count = aggressive_count + normal_count
        return aggressive_count / total_count, normal_count / total_count
    def save(route_id, driver_id, start, end, aggressive_score, normal_score):
        meta = MetaData(ENGINE)
        # routes = Table('routes', meta, autoload=True)
        scores = Table('scores', meta, autoload=True)
        # routes_stmt = sa.dialects.postgresql.insert(routes).values({'route_id': route_id, 'user_id': driver_id})
        # routes_stmt = routes_stmt.on_conflict_do_nothing(index_elements=['route_id'])
        scores_stmt = insert(scores).values(
            {
                'route_id': route_id, 'start_time': start, 'end_time': end,
                'aggressive_score': aggressive_score, 'normal_score': normal_score
            }
        )
        conn = ENGINE.connect()
        # conn.execute(routes_stmt)
        conn.execute(scores_stmt)
        conn.execute('COMMIT')
        conn.close()
    if not data:
        return
    for i in range(0 ,len(data)):
        route_id = data[i][0]
        driver_id = data[i][1]
        start = data[i][2]
        end = data[i][3]
        aggressive_score, normal_score = predict(data[i][4])
        save(route_id, driver_id, start, end, aggressive_score, normal_score)
        print('{0}, {1}, {2}, {3}, {4}, {5}'.format(route_id, driver_id, start, end, aggressive_score, normal_score))

def main():
    lines = ssc.socketTextStream('localhost', 9999)
    lines.map(lambda row: preprocess_row(row))\
         .map(lambda row: (row[0], row[1:]))\
         .groupByKey()\
         .mapValues(list).map(lambda x: list(x))\
         .map(lambda row: preprocess_row_2(row))\
         .foreachRDD(lambda rdd: predict_and_save_rdd(rdd.collect()))   
    ssc.start()
    ssc.awaitTermination()

    
if __name__ == '__main__':
    main()