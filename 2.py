import requests
import pandas as pd

# URL для запроса данных через API MOEX ISS
url = "https://iss.moex.com/iss/history/engines/stock/markets/shares/boards/TQBR/securities/SBER.json"

# Параметры запроса (интервал и количество дней)
params = {
    "start": 0,  # Начало выборки
    "date": None,  # Если нужно ограничить выборку определенной датой
    "limit": 1000  # Лимит строк в ответе
}

# Отправляем GET-запрос
response = requests.get(url)
print(response)

# Проверяем успешность запроса
if response.status_code == 200:
    data = response.json()
    print(data)

    # Извлекаем метаданные и данные из JSON
    columns = data['history']['columns']
    rows = data['history']['data']

    # Создаем DataFrame
    df = pd.DataFrame(rows, columns=columns)
    print(df)

    # Оставляем только нужные столбцы: дата и цена закрытия
    # df = df[['TRADEDATE', 'CLOSE']]
    # df.columns = ['Date', 'Price']  # Переименовываем столбцы

    # Преобразуем дату в формат datetime
    # df['Date'] = pd.to_datetime(df['Date'])

    # Сортируем по дате
    # df = df.sort_values(by='Date')

    # Выводим результат
    #print(df)

    # Сохраняем в CSV файл (если нужно)
    # df.to_csv('SBER_daily_prices.csv', index=False)
else:
    print(f"Ошибка при получении данных. Код ошибки: {response.status_code}")