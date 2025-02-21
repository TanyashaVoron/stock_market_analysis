import pandas as pd
from tabulate import tabulate

# JSON-ответ
json_data = {
    'history': {
        'columns': [
            'BOARDID', 'TRADEDATE', 'SHORTNAME', 'SECID', 'NUMTRADES', 'VALUE', 'OPEN', 'LOW', 'HIGH',
            'LEGALCLOSEPRICE', 'WAPRICE', 'CLOSE', 'VOLUME', 'MARKETPRICE2', 'MARKETPRICE3', 'ADMITTEDQUOTE',
            'MP2VALTRD', 'MARKETPRICE3TRADESVALUE', 'ADMITTEDVALUE', 'WAVAL', 'TRADINGSESSION', 'CURRENCYID', 'TRENDCLSPR'
        ],
        'data': [
            ['TQBR', '2013-03-25', 'Сбербанк', 'SBER', 140, 59340002.8, 96, 96, 101.14, 98.66, 99.95, 98.79,
             593680, 99.99, 99.99, 99.99, 8572433621.95, 8572433621.95, 8572433621.95, None, 3, 'SUR', None],
            ['TQBR', '2013-03-26', 'Сбербанк', 'SBER', 183, 126030358.8, 98.58, 97.08, 99.31, 97.13, 98.19, 97.2,
             1283550, 97.82, 97.82, 97.82, 12218468579.3, 12218468579.3, 12218468579.3, None, 3, 'SUR', -1.61]
        ]
    }
}

# Создаём DataFrame
df = pd.DataFrame(json_data['history']['data'], columns=json_data['history']['columns'])

# Красивый вывод
print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
