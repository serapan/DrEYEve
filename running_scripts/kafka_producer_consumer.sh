sudo $KAFKA_HOME/bin/connect-standalone.sh ./kafka_producer_config/worker.properties ./kafka_producer_config/MongoSourceConnector.properties > /dev/null 2>&1 &
sleep 6
cd ..
python3 -m app_ml.predict.kafka_consumer
