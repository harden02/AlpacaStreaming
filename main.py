import logging
import sys
import yaml
import alpacaConnection as ac


def main():
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    config = yaml.safe_load(open("api.yaml"))
    connection = ac.getStreamingConnection(config['Key'], config['Secret'])
    ac.subscribeToStream(connection, 'AAPL')


if __name__ == "__main__":
    main()