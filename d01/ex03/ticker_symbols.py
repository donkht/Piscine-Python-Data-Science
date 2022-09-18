import sys

def ticker_symbols():
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
        if sys.argv[1].upper() in STOCKS:
            for key, value in COMPANIES.items():
                if COMPANIES[key] == sys.argv[1].upper():
                    print(key + " " + str(STOCKS[sys.argv[1].upper()]))
        else:
            print("Unknown ticker")


if __name__ == '__main__':
    ticker_symbols()