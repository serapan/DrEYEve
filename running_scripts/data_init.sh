cd ..
python3 -m app_ml.data.mongo_data_init
python3 -m app_ml.data.postgres_data_init
python3 -m app_ml.data.insert_data_to_postgres