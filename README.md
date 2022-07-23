# Stock-Scrapper-and-Predictor
In this project, an easy to use finanical data scrapper is developed for extracting the stocks data from Yahoo Finance for: 
1. Current timestamp: 
  - price, change, change percent, close price, open price, range (low to high) and volume parameters are extracted and stored in as JSON object.
  - Stocks of interest can be provided in "my_stocks" variable in get_current_stock_prices.py. As "my_stocks" is list, multiple entries can be made.
2. historical period: 
  - data, open, high, low, close, adj close, volume and name.

Currently, working on developing AI/ML model for predicting stock close prices. This model will be avilable shortly. 

# Steps for reproducing in your machine 
1. Create a virtual enviroment (Optional but would highly recommend as this comes under best practices)
2. Install Requirements: pip install -r requirements.txt
3. Current timestamp stock data: python get_current_stock_prices.py
4. Historical timestamp stock data: python get_current_stock_prices.py
