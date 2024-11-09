import requests
import time
from datetime import datetime, timezone, timedelta

def fetch_time_data():
    response = requests.get("https://yandex.com/time/sync.json?geo=213")
    raw_data = response.json()
    print("Ответ в сыром виде:", raw_data)
    return raw_data

def parse_time_data(data):
    timestamp = data['time'] / 1000
    moscow_offset = timedelta(milliseconds=data['clocks']['213']['offset'])
    human_time = datetime.fromtimestamp(timestamp, tz=timezone.utc) + moscow_offset
    timezone_name = data['clocks']['213']['name']
    print("Время:", human_time.strftime("%Y-%m-%d %H:%M:%S"))
    print("Часовой пояс:", timezone_name)
    return human_time

def measure_time_delta():
    deltas = []
    for _ in range(5):
        start_time = datetime.now(timezone.utc)
        data = fetch_time_data()
        api_time = parse_time_data(data)
        delta = (start_time - api_time).total_seconds()
        deltas.append(abs(delta))
        print(f"Дельта времени: {abs(delta)} секунд")
    avg_delta = sum(deltas) / len(deltas)
    print(f"Средняя дельта времени: {avg_delta} секунд")

if __name__ == "__main__":
    measure_time_delta()

