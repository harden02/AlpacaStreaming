import numpy as np
import pandas as pd
import yaml
from time import sleep
from alpaca.data.live import StockDataStream
from alpaca.data.enums import DataFeed

def getStreamingConnection(key, secret):
    conn = StockDataStream(key, secret, DataFeed.IEX)
    return conn

async def handle_trade(data):
    print(data)


def subscribeToStream(client, symbols):
    client.subscribe_bars(handle_trade, symbols)
    client.run()
