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

## Usage

source env.sh
