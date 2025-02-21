import requests
import pandas as pd
from datetime import datetime, timedelta
from tabulate import tabulate

# Определяем параметры
ticker = "SBER"
days = 30  # Количество дней

# URL для запроса данных через API MOEX ISS
url = f'https://iss.moex.com/iss/history/engines/stock/markets/shares/boards/TQBR/securities/{ticker}.json'

# Вычисляем даты
end_date = datetime.today().strftime("%Y-%m-%d")
start_date = (datetime.today() - timedelta(days=days)).strftime("%Y-%m-%d")

# Параметры запроса
params = {
    "from": start_date,
    "till": end_date,
    "limit": 100,  # Увеличиваем лимит данных
    "start": 0
}

# Отправляем GET-запрос
response = requests.get(url, params=params)

# Проверяем успешность запроса
if response.status_code == 200:
    data = response.json()
else:
    print("Ошибка запроса:", response.status_code)
    print(response.text)
    exit()

# Проверяем наличие данных
if "history" not in data or "data" not in data["history"] or not data["history"]["data"]:
    print("Нет актуальных данных за указанный период.")
    exit()

# Извлекаем данные
columns = data['history']['columns']
data = data['history']['data']

# Создаём DataFrame
df = pd.DataFrame(data, columns=columns)

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
