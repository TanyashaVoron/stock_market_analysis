import pandas as pd

# Создание DataFrame
data = {
    'BOARDID': ['TQBR', 'TQBR'],
    'TRADEDATE': ['2013-03-25', '2013-03-26'],
    'SHORTNAME': ['Сбербанк', 'Сбербанк'],
    'SECID': ['SBER', 'SBER'],
    'NUMTRADES': [140, 183],
    'VALUE': [59340002.8, 126030358.8],
    'OPEN': [96.0, 98.58],
    'LOW': [96.0, 97.08],
    'HIGH': [101.14, 99.31],
    'LEGALCLOSEPRICE': [98.66, 97.13],
    'WAPRICE': [99.95, 98.19],
    'CLOSE': [98.79, 97.2],
    'VOLUME': [593680, 1283550],
    'MARKETPRICE2': [99.99, 97.82],
    'MARKETPRICE3': [99.99, 97.82],
    'ADMITTEDQUOTE': [99.99, 97.82],
    'MP2VALTRD': [8572433621.95, 12218468579.3],
    'MARKETPRICE3TRADESVALUE': [8572433621.95, 12218468579.3],
    'ADMITTEDVALUE': [8572433621.95, 12218468579.3],
    'WAVAL': [None, None],  # Пропущенные значения
    'TRADINGSESSION': [3, 3],
    'CURRENCYID': ['SUR', 'SUR'],
    'TRENDCLSPR': [None, -1.61]  # Пропущенное значение
}

df = pd.DataFrame(data)
print(df)

# Обработка пропущенных значений и некорректных типов данных
df = df.applymap(lambda x: x if isinstance(x, (int, float, str)) else None)

# Преобразование даты в человекочитаемый формат
df['TRADEDATE'] = pd.to_datetime(df['TRADEDATE']).dt.strftime('%d.%m.%Y')

# Явное преобразование числовых столбцов
numeric_columns = [
    'NUMTRADES', 'VALUE', 'OPEN', 'LOW', 'HIGH', 'LEGALCLOSEPRICE', 'WAPRICE', 'CLOSE',
    'VOLUME', 'MARKETPRICE2', 'MARKETPRICE3', 'ADMITTEDQUOTE', 'MP2VALTRD',
    'MARKETPRICE3TRADESVALUE', 'ADMITTEDVALUE', 'TRENDCLSPR'
]
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')  # Преобразуем в числовой тип, игнорируя ошибки

# Настройка параметров отображения
pd.set_option('display.max_columns', None)  # Показать все столбцы
pd.set_option('display.width', 1000)  # Установить ширину вывода
pd.set_option('display.float_format', '{:.2f}'.format)  # Форматирование чисел с плавающей точкой
pd.set_option('display.colheader_justify', 'center')  # Центрирование заголовков столбцов

# Вывод DataFrame
print(df)