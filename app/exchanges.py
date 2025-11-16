import ccxt
from typing import List, Dict, Any

async def get_price(symbol: str, exchange: str = "binance") -> Dict[str, Any]:
    """Get current price for a symbol on a given exchange."""
    try:
        exchange_obj = getattr(ccxt, exchange)()
        ticker = exchange_obj.fetch_ticker(symbol)
        return {
            "symbol": symbol,
            "exchange": exchange,
            "price": ticker["last"],
            "bid": ticker["bid"],
            "ask": ticker["ask"]
        }
    except Exception as e:
        raise Exception(f"Error fetching price: {str(e)}")

async def get_ohlcv(symbol: str, exchange: str = "binance", timeframe: str = "1d", limit: int = 30) -> List[List[Any]]:
    """Get OHLCV data for a symbol."""
    try:
        exchange_obj = getattr(ccxt, exchange)()
        ohlcv = exchange_obj.fetch_ohlcv(symbol, timeframe, limit=limit)
        return ohlcv
    except Exception as e:
        raise Exception(f"Error fetching OHLCV: {str(e)}")

def list_exchanges() -> List[str]:
    """List all available exchanges."""
    return ccxt.exchanges
