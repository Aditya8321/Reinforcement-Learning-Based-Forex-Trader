# BRX-B Stock Data Acquisition

## Overview
This project focuses on acquiring and processing financial data for **BRX-B stock**.  
The data was obtained using the **Alpha Vantage API** and supplemented with scraping from Yahoo Finance's **Most Active Stocks** list.

## Data Sources
- **Alpha Vantage API**  
  Used to pull historical stock data for BRX-B.
- **Yahoo Finance (Most Active Stocks)**  
  [Yahoo Finance - Most Active](https://finance.yahoo.com/most-active) was scraped to gather current trending stock activity.

## Files
- `stage04_data-acquisition-and-ingestion_homework-starter.ipynb`  
  Jupyter Notebook containing the data acquisition and ingestion workflow.

## Requirements
To run the notebook, install the following dependencies:

```bash
pip install requests pandas beautifulsoup4 yfinance
