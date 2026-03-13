import yfinance as yf
import argparse
import json
import os
import sys
from email.message import EmailMessage
from portfolio_monitor.emailer import send_email
from portfolio_monitor.dataclass_types import Asset

#Print relevant data based on argument flag
DEBUG_MODE = False

parser = argparse.ArgumentParser()
parser.add_argument(
        "-d",
        "--debug",
        action = "store_true",
        default = False)

DEBUG_MODE = parser.parse_args().debug

sender = os.environ.get("SENDER_EMAIL")
recipient = os.environ.get("RECEIVER_EMAIL")
password = os.environ.get("SENDER_PASSWORD")

if sender is None or recipient is None or password is None:
    print("ERROR: Missing sender or recipient data. Did you source your env.sh?")
    sys.exit()

def load_portfolio(file_path="user_data/json/portfolio.json"):
    with open(file_path, "r") as f:
        return json.load(f)

def populate_assets(portfolio):
    assets = []
    for account in portfolio["accounts"]:
        for asset in account["assets"]:
            assets.append(Asset(
                symbol=asset["symbol"],
                quantity=asset["quantity"],
                account=account["name"]
            ))
    return assets

def fetch(assets):
    for x in assets:
        print(x.symbol)

    return 0

def main():
    portfolio = load_portfolio()
    assets = populate_assets(portfolio)
    fetch(assets)

    if DEBUG_MODE:
      print("sender email:", sender)
      print("receiver email:", recipient)
      print("sender password: ", password)
      print(portfolio)
      print("\n\n")
      print(assets)
    else:
      send_email(sender, recipient, password, "temp body")

if __name__ == "__main__":
    main()
