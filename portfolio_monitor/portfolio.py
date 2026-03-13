import json
from .dataclass_types import Asset

def load_portfolio(file_path="user_data/portfolio.json"):
    with open(file_path, "r") as f:
        portfolio = json.load(f)

    assets = []

    for account in portfolio["accounts"]:
        for asset in account["assets"]:
            assets.append(Asset(
                symbol=asset["symbol"],
                quantity=asset["quantity"],
                account=account["name"]
            ))

    return assets
