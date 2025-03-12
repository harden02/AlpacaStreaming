import logging
import sys
import yaml
import alpacaConnection as ac
import google.cloud.logging
import os


def main():
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    config = yaml.safe_load(open("api.yaml"))
    connection = ac.getStreamingConnection(config['Key'], config['Secret'])
    ac.subscribeToStream(connection, 'AAPL')


if __name__ == "__main__":
    if int(os.environ.get("PRODUCTION", 0)) == 1: #checks if env is production and sets up cloud logging
        client = google.cloud.logging.Client()
        client.setup_logging()
    main()