import yfinance as yf

# Download data then export as CSV
data_df = yf.download("CODE_FOR_DATA_FROM_YAHOO_FINANCE", start="2010-07-13", end="2022-03-20")
data_df.to_csv('bitcoin_yahoo.csv')
