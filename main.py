import yfinance
import pandas as pd

def download_stock_data(symbol,start_date,end_date):
    """

    :param symbol: Stock symbol
    :param start_date: Start date in 'YYYY-MM-DD' format
    :param end_date: End date in 'YYYY-MM-DD' format
    :return: Dataframe containing stock data
    """
    stock_data=yfinance.download(symbol,start=start_date,end=end_date)
    return stock_data

def save_to_csv(data,symbol):
    """

    :param data: Dataframe containing data
    :param symbol: Stock symbol to use in the file name
    """
    filename=f"{symbol}_data.csv"
    data.to_csv(filename)
    print(f"Data saved to {filename}")

def main():
    symbol=input("Enter the stock symbol:")
    start_date=input("Enter the start date (YYYY-MM-DD):")
    end_date=input("Enter the end date (YYYY-MM-DD):")

    stock_data=download_stock_data(symbol,start_date,end_date)
    print(stock_data)

    save_to_csv(stock_data,symbol)

if __name__=="__main__":
    main()
