from google.cloud import pubsub
import logging
import yaml


logger = logging.getLogger(__name__)
pubSubConfig = yaml.safe_load(open("config.yaml"))

def publishMessage(message):
    publisher = pubsub.PublisherClient()
    psAddress = 'projects/{project}/topics/{topic}'.format(
        project = pubSubConfig['projectID'],
        topic = pubSubConfig['pubSubTopic'],  
    )
    logger.info(f"publishing message to {psAddress}, message: {message}")
    publisher.publish(psAddress, message)
