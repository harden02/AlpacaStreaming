from alpaca.data.live import StockDataStream
from alpaca.data.enums import DataFeed
import logging

logger = logging.getLogger(__name__)

def getStreamingConnection(key, secret):
    conn = StockDataStream(key, secret, DataFeed.IEX)
    logger.info("Establishing connection with alpaca API")
    return conn

async def handle_trade(data):
    print(data)


def subscribeToStream(client, symbols):
    client.subscribe_bars(handle_trade, symbols)
    client.run()
    logger.info(f"Subscribed to {symbols}")
