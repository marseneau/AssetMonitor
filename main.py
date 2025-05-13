import yfinance as yf
import json
import os
import smtplib
from email.message import EmailMessage
from dataclasses import dataclass

sender = os.environ["SENDER_EMAIL"]
recipient = os.environ["RECEIVER_EMAIL"]
password = os.environ["SENDER_PASSWORD"]

print("sender email:", sender)
print("receiver email:", recipient)
print("sender password: ", password)

@dataclass
class Asset:
    symbol: str
    quantity: float
    account: str

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

def load_portfolio(file_path="portfolio.json"):
    with open(file_path, "r") as f:
        return json.load(f)

def send_email():
    msg = EmailMessage()
    msg["Subject"] = "Test"
    msg["From"] = sender
    msg["To"] = recipient
    msg.set_content("Third test email")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)


def main():
    portfolio = load_portfolio()

    print(portfolio)
    print("\n\n")

    assets = populate_assets(portfolio)

    print(assets)

    #send_email()

    #for account in portfolio["accounts"]:    

if __name__ == "__main__":
    main()
