def load_config():
    sender = os.environ.get("SENDER_EMAIL")
    recipient = os.environ.get("RECEIVER_EMAIL")
    password = os.environ.get("SENDER_PASSWORD")

    if sender is None or recipient is None or password is None:
        print("ERROR: Missing sender or recipient data. Did you source your env.sh?")
        sys.exit()

    return sender, recipient, password
