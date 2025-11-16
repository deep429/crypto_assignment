# crypto_assignment

## Overview
This project implements a Python-based MCP (Model Context Protocol) server that provides fast, reliable access to real-time and historical cryptocurrency market data from major exchanges. Using FastAPI as the web framework and CCXT for exchange integration, the server exposes RESTful endpoints to fetch market prices, historical OHLCV (candlestick) data, and exchange listings. The server is caching requests to optimize performance and includes robust error handling.

## Project Structure
  app/
    main.py       # FastAPI app initialization
    routes.py     # API route definitions
    exchanges.py  # CCXT integration for market data
    utils.py      # Caching utilities and helpers
  tests/
    test_routes.py    # API endpoint test cases
    test_exchanges.py # Exchange-related tests
  requirements.txt
  README.md
  
---

## Installation

1. **Clone the repository**
    ```
    git clone https://github.com/deep429/crypto_assignment.git
    cd crypto_assignment
    ```

2. **Create a virtual environment (recommended)**
    ```
    python -m venv venv
    source venv/bin/activate    # On Windows: venv\Scripts\activate
    ```

3. **Install Python dependencies**
    ```
    pip install -r requirements.txt
    ```

---

## Usage

1. **Start the FastAPI server**
    ```
    uvicorn app.main:app --reload
    ```

2. **Explore the API**
   - Interactive API docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Example endpoint:  
     ```
     http://127.0.0.1:8000/price?symbol=BTC/USDT&exchange=binance
     ```

---

## API Endpoints

| Endpoint         | Method | Description                                  |
|------------------|--------|----------------------------------------------|
| `/price`         | GET    | Get current price of a trading pair          |
| `/historical`    | GET    | Fetch OHLCV historical data                  |
| `/exchanges`     | GET    | List all exchanges supported via CCXT        |

**Parameters:**
- `symbol` (e.g., `BTC/USDT`)
- `exchange` (e.g., `binance`)
- `timeframe` (for historical data, e.g., `1h`, `1d`)
- `limit` (number of bars to fetch)

---

## Testing

1. **Run all tests**
    ```
    pytest tests/
    ```

---

## Assumptions

- Symbols must be valid market pairs supported by the chosen exchange.
- Exchange availability and data depend on CCXT’s support.
- In-memory cache is used (for larger deployments, consider Redis).
- This is an educational/demonstration codebase; production features (auth, persistent cache, rate limiting) are left as extensions.

---

## Future Enhancements

- Add authentication/authorization
- Support more data providers (e.g., CoinMarketCap)
- Implement advanced caching or rate limiting
- Add WebSocket endpoints for real-time push
- Expand endpoint coverage (order book, recent trades, etc.)

