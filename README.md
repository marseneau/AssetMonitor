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
**Note:** Do not commit these user_data contents with **any** real env.sh or portfolio data.

## Usage

### Run the script manually
```bash
source user_data/env.sh
python main.py
```
