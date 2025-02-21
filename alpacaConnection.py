from alpaca.data.live import StockDataStream
from alpaca.data.enums import DataFeed
import logging
import pubsubHandler as ps

logger = logging.getLogger(__name__)

def getStreamingConnection(key, secret):
    conn = StockDataStream(key, secret, DataFeed.IEX)
    logger.info("Establishing connection with alpaca API")
    return conn

async def handle_trade(data):
    logger.info(f"data is {data}")
    #ps.publishMessage(data)

def subscribeToStream(client, symbols):
    client.subscribe_bars(handle_trade, symbols)
    logger.info(f"Subscribed to {symbols}")
    client.run()
