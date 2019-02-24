import base64
import datetime
from google.cloud import bigquery
import json

def send_to_bq(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    card_id = json.loads(pubsub_message)["Card"]
    project_id = event['attributes']['projectId']
    location = event['attributes']['deviceRegistryLocation']
    registry_id = event['attributes']['deviceRegistryId']
    device_id = event['attributes']['deviceId']
    client = bigquery.Client()
    dataset_id = 'my_iot_dataset'  
    table_id = 'myiotdataset'
    table_ref = client.dataset(dataset_id).table(table_id)
    table = client.get_table(table_ref)  # API request
    rows_to_insert = [
    (card_id,registry_id,device_id,  datetime.datetime.now()), ]
    
    errors = client.insert_rows(table, rows_to_insert)
    assert errors == []
