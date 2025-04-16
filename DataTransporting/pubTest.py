from google.cloud import pubsub_v1
import json

# TODO(developer)
project_id = "nhoung-data-eng"
topic_id = "my-topic"

publisher = pubsub_v1.PublisherClient()
# The `topic_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/topics/{topic_id}`
topic_path = publisher.topic_path(project_id, topic_id)

with open("oneDayVehicleData.json", "r") as file:
    data = json.load(file)
    # print(data)

for n in data:
    for id in n:
        message = json.dumps(id)
        json_data = message.encode("utf-8")
        future = publisher.publish(topic_path, json_data)
        # print(future.result())
    
# print(data[0])
# for n in range(1, 10):
#     data_str = f"Message number {n}"
#     # Data must be a bytestring
#     data = data_str.encode("utf-8")
#     # When you publish a message, the client returns a future.
#     future = publisher.publish(topic_path, data)
#     print(future.result())

print(f"Published messages to {topic_path}.")