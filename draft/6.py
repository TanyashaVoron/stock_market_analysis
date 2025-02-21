import pandas as pd

data = {
    'history': {
        'columns': [
            'BOARDID', 'TRADEDATE', 'SHORTNAME', 'SECID', 'NUMTRADES', 'VALUE', 'OPEN', 'LOW', 'HIGH',
            'LEGALCLOSEPRICE', 'WAPRICE', 'CLOSE', 'VOLUME'
        ],
        'data': [
            ['TQBR', '2013-03-25', 'Сбербанк', 'SBER', 140, 59340002.8, 96, 96, 101.14, 98.66, 99.95, 98.79,
             593680],
            ['TQBR', '2013-03-26', 'Сбербанк', 'SBER', 183, 126030358.8, 98.58, 97.08, 99.31, 97.13, 98.19, 97.2,
             1283550]
        ]
    }
}

columns = data['history']['columns']
rows = data['history']['data']

# Создаем DataFrame
df = pd.DataFrame(rows, columns=columns)
df_ = pd.DataFrame()
print(df['CLOSE'])
print(df)