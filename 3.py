import pandas as pd
from tabulate import tabulate

# Данные JSON
json_data = {
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

data = {
    key: [row[idx] for row in json_data['history']['data']]
    for idx, key in enumerate(json_data['history']['columns'])
}
print(data)

# Создаём DataFrame
df = pd.DataFrame(data=data)

print(df.VALUE)
# Красивый вывод
print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))

# Оставляем только нужные столбцы: дата и цена закрытия
df = df[['TRADEDATE', 'CLOSE']].rename(columns={'TRADEDATE': 'Дата', 'CLOSE': 'Цена'})

# Преобразуем дату в формат ДД.ММ.ГГ
df['Дата'] = pd.to_datetime(df['Дата']).dt.strftime('%d.%m.%y')

# Преобразуем цену в числовой тип
df['Цена'] = pd.to_numeric(df['Цена'], errors='coerce')

# Удаляем строки с пустыми значениями цены
df = df.dropna(subset=['Цена'])

# Сортируем по дате
df = df.sort_values(by='Дата')

# Красивый вывод
print(tabulate(df, headers='keys', tablefmt='grid', showindex=False))

# Сохраняем в CSV
df.to_csv('SBER_daily_prices.csv', index=False, encoding='utf-8')


json_data = {
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

json_data_new = {
    'BOARDID':['TQBR','TQBR'],
    'TRADEDATE':['2013-03-25','2013-03-26'],
    'SHORTNAME':['Сбербанк','Сбербанк'],
    'SECID':['SBER','SBER'],
    'NUMTRADES':[183,140],
    'VALUE':[59340002.8,126030358.8],
    'OPEN':[96,96.58],
    'LOW':[96,97.88],
    'HIGH':[101.14,99.31],
    'LEGALCLOSEPRICE':[98.66,97.13],
    'WAPRICE':[99.95,98.19],
    'CLOSE':[98.79,97.2],
    'VOLUME':[593680,1283550]
}
