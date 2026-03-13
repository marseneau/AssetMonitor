import yfinance as yf
import random
from .dataclass_types import Asset

def fetch_performance(assets):
    symbols = list({asset.symbol for asset in assets})

    try:
        data = yf.download(
            symbols,
            period="2d",
            group_by="ticker",
            progress=False
        )
    except Exception as e:
        print(e)
        return

    for asset in assets:
        if asset.symbol not in data:
            continue

        hist = data[asset.symbol]
        
        if len(hist) < 2:
            continue
        
        curr = hist["Close"].iloc[-1]
        prev = hist["Close"].iloc[-2]

        asset.latest_price = curr
        asset.previous_price = prev
        asset.change = curr - prev
        asset.percent_change = (asset.change / prev) * 100

#Generate dummy data, allowing for fewer api calls during development
def mock_performance(assets):
    for asset in assets:
        prev = round(random.uniform(100, 200), 2)
        curr = round(prev * random.uniform(0.95, 1.05), 2)

        asset.latest_price = curr
        asset.previous_price = prev
        asset.change = round((curr - prev), 2)
        asset.percent_change = round((asset.change / prev) * 100, 2)
