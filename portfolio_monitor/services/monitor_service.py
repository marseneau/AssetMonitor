import sys

from portfolio_monitor.emailer import *
from portfolio_monitor.portfolio import *
from portfolio_monitor.market_data import *

def run_monitor(debug = False):
    portfolio = load_portfolio()

    if debug:
        mock_performance(portfolio)
        print("DEBUG DATA: ")
        print(portfolio)
        return portfolio
    else:
        fetch_performance(portfolio)
        email_body = build_email_body(portfolio)
        send_email(email_body)

    return portfolio
