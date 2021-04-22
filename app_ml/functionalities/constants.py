import os

TRAFFIC_MAP = {
    'LowCongestionCondition': 0,
    'NormalCongestionCondition': 1,
    'HighCongestionCondition': 2
}

SURFACE_MAP = {
    'SmoothCondition': 0,
    'UnevenCondition': 1,
    'FullOfHolesCondition': 2
}

TO_CHECK_IF_NAN_FIELDS = [
    'VehicleSpeedInstantaneous', 'VehicleSpeedAverage', 'VehicleSpeedVariance', 'VehicleSpeedVariation',
    'LongitudinalAcceleration', 'EngineLoad', 'EngineCoolantTemperature', 'ManifoldAbsolutePressure',
    'EngineRPM', 'MassAirFlow', 'IntakeAirTemperature', 'VerticalAcceleration', 'FuelConsumptionAverage'
    ]

WINDOW = 20

SPARK_WINDOW = 20

MONGO_URL = 'mongodb://localhost:27017'

POSTGRES_URL = 'postgres://postgres:postgres@localhost/cars'

GENERATED_DATA_PATH = '/home/serafeim/Documents/SHMMY/Thesis/Code/app_ml/train/generated_data' 

ORIGINAL_DATA_PATH = '/home/serafeim/Documents/SHMMY/Thesis/Code/app_ml/data'

SAVED_MODEL_PATH = '/home/serafeim/Documents/SHMMY/Thesis/Code/RNN_MODEL'

FOLDERS = os.listdir(GENERATED_DATA_PATH)

FILES = ['opel_corsa_01', 'opel_corsa_02', 'peugeot_207_01', 'peugeot_207_02']
