trap 'sudo kill $STREAM_PID; exit' INT
cd ..
python3 -m app_ml.data.stream_data ./app_ml/data/peugeot_207_01.csv &
STREAM_PID=$!
sleep 10
python3 -m app_ml.data.stream_data ./app_ml/data/peugeot_207_02.csv
