import time
import json
from concurrent import futures

import os
import grpc
import location_pb2
import location_pb2_grpc
from kafka import KafkaProducer



# TOPIC_NAME = os.environ["TOPIC_NAME"]
# KAFKA_SERVER = os.environ["KAFKA_SERVER"]

TOPIC_NAME= "locations-topic"

KAFKA_SERVER= "kafka-service:9092"



class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):

        request_value = {
            "person_id": int(request.person_id),
            "longitude": request.longitude,
            "latitude": request.latitude,
        }
        print(f'Location created - gRPC:  {request_value}')

        producer.send(TOPIC_NAME, json.dumps(request_value, default=json_util.default).encode('utf-8'))


        return location_pb2.LocationMessage(**request_value)

# Initialize Kafka Producer 
producer = KafkaProducer(bootstrap_servers=[KAFKA_SERVER])

print('Kafka Producer Started...')

time.sleep(10)

# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)


print("gRPC Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
