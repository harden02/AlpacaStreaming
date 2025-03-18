from google.cloud import pubsub
import logging
import yaml
import json
import re


logger = logging.getLogger(__name__)
pubSubConfig = yaml.safe_load(open("config.yaml"))

def publishMessage(message):    #publishes message to pubsub
    publisher = pubsub.PublisherClient()
    psAddress = 'projects/{project}/topics/{topic}'.format(
        project = pubSubConfig['projectId'],
        topic = pubSubConfig['pubSubTopic'],  
    )
    logger.info(f"publishing message to {psAddress}, message: {message}")
    publisher.publish(psAddress, message)

def serializeJSON(messagePayload):
    logger.info("serialzing JSON for publishing")
    epochSeconds = re.search('([0-9]*),', str(messagePayload['t'])) #extract seconds from timestamp object with regex search
    messagePayload['t'] = epochSeconds.group(1)
    names_key = {'T' : 'Type' ,                   #key values for JSON to match BQ schema
                 'S' : 'Symbol',
                 'o' : 'Open', 
                 'h' : 'High',
                 'l' : 'Low',
                 'c' : 'Close',
                 'v' : 'Volume',
                 't' : 'Timestamp', 
                 'n' : 'numTradeTickers',
                 'vw': 'VolumeWeightedPrice'
              }
    for key in names_key:
        messagePayload[names_key[key]] = messagePayload.pop(key) #renames keys in JSON to match desired bigQuery output
    return json.dumps(messagePayload).encode('utf-8') #return JSON object as bytes for publishing to pubsub