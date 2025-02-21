import requests
import pandas as pd
import apimoex
from datetime import datetime, timedelta

# Определяем параметры
ticker = "SBER"
days = 30  # Количество дней

# Вычисляем даты
end_date = datetime.today().strftime("%Y-%m-%d")
start_date = (datetime.today() - timedelta(days=days)).strftime("%Y-%m-%d")

# URL API МосБиржи
url = "https://iss.moex.com/iss/engines/stock/markets/shares/securities/{}/candles.json".format(ticker)

# Параметры запроса (дневные свечи)
params = {
    "from": start_date,
    "till": end_date,
    "interval": 24  # Интервал 24 означает дневные данные
}

# Запрос данных
with requests.Session() as session:
    data = apimoex.get_market_candles(session, ticker, interval=24, start=start_date, end=end_date)

# Преобразуем данные в DataFrame
df = pd.DataFrame(data)

# Переименуем столбцы для удобства
df.rename(columns={"begin": "Дата", "close": "Цена закрытия", "volume": "Объём торгов"}, inplace=True)

# Выводим результат
print(df)
