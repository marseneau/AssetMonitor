import yfinance as yf
import argparse
import json
import os
import sys
import smtplib
from email.message import EmailMessage
from dataclasses import dataclass

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

@dataclass
class Asset:
    symbol: str
    quantity: float
    account: str

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

def send_email():
    msg = EmailMessage()
    msg["Subject"] = "Test"
    msg["From"] = sender
    msg["To"] = recipient
    msg.set_content("test email")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)

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

    send_email()

    #for account in portfolio["accounts"]:    

if __name__ == "__main__":
    main()
