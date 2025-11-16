from app.exchanges import list_exchanges

def test_list_exchanges():
    exs = list_exchanges()
    assert "binance" in exs
    assert isinstance(exs, list)
