import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_price():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/price", params={"symbol": "BTC/USDT"})
        assert response.status_code == 200
        assert "price" in response.json()

@pytest.mark.asyncio
async def test_exchanges():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/exchanges")
        assert response.status_code == 200
        assert "binance" in response.json()
