from alpaca.data.live import StockDataStream
from alpaca.data.enums import DataFeed
import logging
import pubsubHandler as ps

logger = logging.getLogger(__name__)

def getStreamingConnection(key, secret):
    conn = StockDataStream(key, secret, True, DataFeed.IEX) #sets up streaming connection with alpaca API
    logger.info("Establishing connection with alpaca API")
    return conn

async def handle_trade(data): #async function to handle incoming trade data and publish it to Pub/Sub
    logger.info(f"data is {data}")
    jsonData = ps.serializeJSON(data)
    print(jsonData)
    ps.publishMessage(jsonData)

def subscribeToStream(client, symbols): #subscribes to a stream of given symbols
    client.subscribe_bars(handle_trade, symbols)
    logger.info(f"Subscribed to {symbols}")
    client.run()
