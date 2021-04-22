KAFKA_PRODUCER_PID=$(ps aux | grep -m 1 'sudo /opt/kafka/bin/connect-standalone.sh ./kafka_producer_config/worker.properties ./kafka_producer_config/MongoSourceConnector.properties' | awk '{print $2}')
sudo kill $KAFKA_PRODUCER_PID
sleep 5
sudo $KAFKA_HOME/bin/kafka-topics.sh --zookeeper localhost:2181 --delete --topic routes.cars.routes
sleep 2
sudo $KAFKA_HOME/bin/kafka-server-stop.sh
sleep 5
sudo $KAFKA_HOME/bin/zookeeper-server-stop.sh
sudo rm -rf /tmp/zookeeper/
sudo rm -rf /tmp/kafka-logs/
sudo rm /tmp/connect.offsets