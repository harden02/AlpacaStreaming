import numpy as np
import pandas as pd
import asyncio
import yaml
from time import sleep
from alpaca.data.timeframe import TimeFrame
from alpaca.data.live import StockDataStream
import alpacaConnection as ac

def main():
    config = yaml.safe_load(open("API.yaml"))
    connection = ac.getStreamingConnection(config['Key'], config['Secret'])
    ac.subscribeToStream(connection, 'AAPL')


if __name__ == "__main__":
    main()