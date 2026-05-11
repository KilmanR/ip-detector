import csv
import datetime
import os

class Reporter:
    def __init__(self, config):        
        self.config = config
        self.file_path = "reports/history.csv"
    def save_report(self, btc_price, usd_rub, status):
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")                                     
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        write_header = not os.path.exists(self.file_path)
        with open(self.file_path, 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            if write_header:
                writer.writerow(['timestamp', 'btc_price', 'usd_rub', 'status'])
            writer.writerow([timestamp, btc_price, usd_rub, status])
        return f"Отчёт сохранён: {self.file_path}"