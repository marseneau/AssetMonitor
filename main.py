import yfinance as yf
import argparse
import os
import sys
from email.message import EmailMessage
from portfolio_monitor.emailer import *
from portfolio_monitor.portfolio import load_portfolio
from portfolio_monitor.market_data import *

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

def main():
    portfolio = load_portfolio()

    if DEBUG_MODE:
        mock_performance(portfolio)
        print("sender email:", sender)
        print("receiver email:", recipient)
        print("sender password: ", password)
        print("DEBUG DATA: ")
        print(portfolio)
    else:
        fetch_performance(portfolio)
        email_body = build_email_body(portfolio)
        send_email(sender, recipient, password, email_body)

if __name__ == "__main__":
    main()
