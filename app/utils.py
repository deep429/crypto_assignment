from fastapi import APIRouter, HTTPException
from app.exchanges import get_price, get_ohlcv, list_exchanges

router = APIRouter()

@router.get("/price")
async def price(symbol: str, exchange: str = "binance"):
    try:
        return await get_price(symbol, exchange)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/historical")
async def historical(symbol: str, exchange: str = "binance", timeframe: str = "1d", limit: int = 30):
    try:
        return await get_ohlcv(symbol, exchange, timeframe, limit)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/exchanges")
async def exchanges():
    return list_exchanges()
