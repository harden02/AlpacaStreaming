import logging
import sys
import yaml
import alpacaConnection as ac

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

def main():
    config = yaml.safe_load(open("API.yaml"))
    connection = ac.getStreamingConnection(config['Key'], config['Secret'])
    ac.subscribeToStream(connection, 'AAPL')


if __name__ == "__main__":
    main()