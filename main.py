import argparse
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
    run_monitor(debug = DEBUG_MODE)

if __name__ == "__main__":
    main()
