import smtplib
from collections import defaultdict
from datetime import datetime
from email.message import EmailMessage

def send_email(sender, recipient, password, body):
    msg = EmailMessage()
    msg["Subject"] = "Portfolio Update: " + datetime.now().strftime("%m-%d-%Y")
    msg["From"] = sender
    msg["To"] = recipient
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)

def build_email_body(portfolio):
    accounts = defaultdict(list)
    
    #Group by account
    for asset in portfolio:
        accounts[asset.account].append(asset)

    tables = []

    COLUMN_FORMAT = "{:7} | {:5} | {:10} | {:10} | {:8} | {:7} | {:12}"

    for account_name, account_assets in accounts.items():
        tables.append(f"Account: {account_name}")

        #Header row
        header = COLUMN_FORMAT.format("Symbol", "Qty", "Prev", "Latest", "$ Chg", "% Chg", "Pos Chg $")
        tables.append(header)
        tables.append("-" * len(header))

        #Body rows
        for asset in account_assets:
            pos_change = asset.change * asset.quantity
            tables.append(COLUMN_FORMAT.format(
                    asset.symbol,
                    asset.quantity,
                    f"{asset.previous_price:.2f}",
                    f"{asset.latest_price:.2f}",
                    f"{asset.change:.2f}",
                    f"{asset.percent_change:.2f}%",
                    f"${pos_change:,.2f}"))

        tables.append("")

    return "\n".join(tables)
