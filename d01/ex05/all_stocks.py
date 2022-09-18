from re import S
import sys

def all_stocks():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
        }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
        }

    if len(sys.argv) == 2:
        splitted = sys.argv[1].replace(' ', '').split(",")
        for x in splitted:
            if x == '':
                return
        for x in splitted:
            if x.upper() in STOCKS:
                for company, ticker in COMPANIES.items():
                    if COMPANIES[company] == x.upper():
                        print(ticker + " is a ticker symbol for " + company)
            elif x.capitalize() in COMPANIES:
                print(x.capitalize() + " stock price is " + str(STOCKS[COMPANIES[x.capitalize()]]))
            else:
                print(x + "k is an unknown company or an unknown ticker symbol")





if __name__ == '__main__':
    all_stocks()