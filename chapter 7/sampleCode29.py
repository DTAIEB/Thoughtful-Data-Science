import requests
import json

def ensure_topic_exists(topic_name):
    response = requests.post(
                message_hub_creds["kafka_rest_url"] + "/admin/topics", 
                data = json.dumps({"name": topic_name}),
                headers={"X-Auth-Token": message_hub_creds["api_key"]}
            )
    if response.status_code != 200 and response.status_code != 202 and \
       response.status_code != 422 and response.status_code != 403:
        raise Exception(response.json())
