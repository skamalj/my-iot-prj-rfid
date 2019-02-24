import base64
from google.cloud import iot_v1
from google.cloud import firestore
import json

def authCard(cardid):
    data_ack = {'CardId' : cardid, 'Status': 'NotAuth'}
    db = firestore.Client()
    doc_ref = db.collection(u'cards').document(cardid)
    if doc_ref.get().exists:
        doc = doc_ref.get().to_dict()
        if (doc['Status'] == 'Authorised'):
            data_ack['Status'] = 'Authorised'
        print(u'Document Exists: {}'.format(str(doc)))
    else:
        doc_ref.set(data_ack)
        print(u'Document Created: {}'.format(str(data_ack)))
    return data_ack    

def sendAuthStatus(event, data_ack):

    """Get Message attributes -project, registry, location and device
    for sending reply to client
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    project_id = event['attributes']['projectId']
    location = event['attributes']['deviceRegistryLocation']
    registry_id = event['attributes']['deviceRegistryId']
    device_id = event['attributes']['deviceId']
    
    client = iot_v1.DeviceManagerClient()
    name = client.device_path(project_id, location, registry_id, device_id)
    
    message = bytes(str(data_ack),'utf-8')
    print('Sending acknowledgment: '+ str(data_ack)) 
    response = client.modify_cloud_to_device_config(name, bytes(str(data_ack),'utf-8'))
    print('Message response:' + str(response))
    
def verify_card(event, context):
    
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    card_id = json.loads(pubsub_message)["Card"]
    print('Pubsub message :' + pubsub_message + 'recieved with attributes :' + str(event['attributes']) )
    
    """Check card authorization against firestore
    """
    data_ack = authCard(card_id)

    """Send card status back to client
    """
    sendAuthStatus(event,data_ack)
