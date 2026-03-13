import yfinance as yf
import argparse
import json
import os
import sys
from email.message import EmailMessage
from portfolio_monitor.emailer import send_email
from portfolio_monitor.portfolio import load_portfolio

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

def fetch(assets):
    for x in assets:
        print(x.symbol)

    return 0

def main():
    portfolio = load_portfolio()
    fetch(portfolio)

    if DEBUG_MODE:
      print("sender email:", sender)
      print("receiver email:", recipient)
      print("sender password: ", password)
      print(portfolio)
    else:
      send_email(sender, recipient, password, "temp body")

if __name__ == "__main__":
    main()
