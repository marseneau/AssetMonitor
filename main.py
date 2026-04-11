import yfinance as yf
import argparse
import os
import sys
from email.message import EmailMessage
from portfolio_monitor.emailer import *
from portfolio_monitor.portfolio import load_portfolio
from portfolio_monitor.market_data import *
from portfolio_monitor.services.monitor_service import run_monitor

#Print relevant data based on argument flag
DEBUG_MODE = False

parser = argparse.ArgumentParser()
parser.add_argument(
        "-d",
        "--debug",
        action = "store_true",
        default = False)

DEBUG_MODE = parser.parse_args().debug

def main():
    portfolio = load_portfolio()

    #remainder gets moved to service
    if DEBUG_MODE:
        mock_performance(portfolio)
        print("DEBUG DATA: ")
        print(portfolio)
    else:
        fetch_performance(portfolio)
        email_body = build_email_body(portfolio)
        send_email(sender, recipient, password, email_body)

if __name__ == "__main__":
    main()
