from kafka import KafkaConsumer
from json import loads, dumps
from collections import deque
from app_ml.functionalities.constants import WINDOW, TO_CHECK_IF_NAN_FIELDS
from pprint import pprint
import socket
import signal
import sys    
import math

msg_queue = {}

def server_init():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 9999))
    sock.listen(1)
    print('Waiting for Spark to connect...')
    spark_conn, addr = sock.accept()
    print('Spark connected')
    return spark_conn

def preprocess(message):
    msg = message.replace('\n', '')
    msg = msg.replace(' ', '')
    msg += '\n'
    return msg

def main():
    def signal_handler(sig, frame):
        consumer.close()
        print('Kafka consumer exiting')
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    spark_conn = server_init()
    
    consumer = KafkaConsumer(
        'routes.cars.routes',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        auto_commit_interval_ms=500,
        max_poll_records = 50,
        # fetch_max_wait_ms=0,
        # group_id='Yo-id',
        group_id = None,
        value_deserializer=lambda x: loads(x.decode('utf-8'))
    )

    for message in consumer:
        record = loads(message.value)
        pprint(record)
        if any(math.isnan(val) for val in [record[x] for x in TO_CHECK_IF_NAN_FIELDS]):
            continue
        route_id = record['RouteId']
        msg_queue[route_id] = msg_queue.get(route_id, deque([]))
        msg_queue[route_id].append(record)
        if len(msg_queue[route_id]) == WINDOW:
            msg = dumps(
                {
                    route_id: list(msg_queue[route_id])
                }
            )
            msg = preprocess(msg)
            # pprint(msg)
            spark_conn.send(bytes(msg, 'utf-8'))
            msg_queue[route_id].popleft()


if __name__ == '__main__':
    main()