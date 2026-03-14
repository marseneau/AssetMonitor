# AssetMonitor

## Description

AssetMonitor is a Python tool that automates daily monitoring of multi-account investment portfolios.

## Features

- Parses multiple accounts and assets from a JSON input file.
- Fetches financial data using the yfinance API.
- Calculates daily price changes for each asset.
- Aggregates data by account to generate and send formatted email reports.
- Produces tables with per-account totals, price changes, and position changes.
- Environment based config for secure credentials.

## Getting Started

### Clone Repository

```bash
git clone https://github.com/marseneau/AssetMonitor.git
pip install yfinance
mkdir AssetMonitor/user_data
```

### Environment setup

AssetMonitor/samples directory provides templates for required environment variables and JSON input file.
Both of the contained files will need to reside in AssetMonitor/user_data.
**Note:** Do not commit these user_data contents with **any** personal env.sh or portfolio data. Git
will ignore the directory by default.

## Usage

### Run the script manually
Specify option '-d' to run in debug mode. This will generate filler data without necessitating 
additional API calls.
```bash
source user_data/env.sh
python3 main.py [-d]
```
### Optionally, schedule to run with Cron

1. Create a script, 'run.sh'

```bash
#!/bin/bash
cd /path/to/AssetMonitor
source user_data/env.sh
python3 main.py
```

2. Make it executable

```bash
chmod 755 run.sh
```

3. Schedule with Cron

Below example assumes 4:30PM EST, 30 minutes after market close.
Additionally, a log file will be created on each execution.

```
crontab -e

30 16 * * 1-5 /path/to/AssetMonitor/run.sh >> /path/to/AssetMonitor/log.txt 2>&1
```
