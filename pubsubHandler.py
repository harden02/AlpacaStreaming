from google.cloud import pubsub
import logging

logger = logging.getLogger(__name__)

def publishMessage(publisher, topicName, projectId, message):
    publisher = pubsub.PublisherClient()
    psAddress = 'projects/{project}/topics/{topic}'.format(
        project = projectId,
        topic = topicName,  
    )
    logger.info(f"publishing message to {psAddress}, message: {message}")
    publisher.publish(psAddress, message)
