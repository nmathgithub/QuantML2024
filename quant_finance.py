# New Python file to explore quantiative finance 
# import pandas as pd 
import yfinance as yf 
# import matplotlib.pyplot as plt 
# import seaborn 

stock = yf.Ticker('AAPL')
dividends_2024 = stock.dividends 
print(dividends_2024)