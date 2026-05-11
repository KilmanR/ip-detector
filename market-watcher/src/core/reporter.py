import json
import datetime
import os

class Reporter:
    def __init__(self, config):        
        self.config = config
        self.file_path = "reports/history.json"
    def save_report(self, btc_price, usd_rub, status):
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")        
        # print(f"💾 Сохраняем отчёт в: {self.file_path}")        
        report_data = {
            "timestamp": timestamp,
            "btc_price": btc_price,
            "usd_rub": usd_rub,
            "status": status            
            }
        
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding='utf-8') as f:
                history = json.load(f)
            history.append(report_data)
        else:
            history = [report_data]
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(history, f, indent=4, ensure_ascii=False)
        return f"Отчёт сохранён: {self.file_path}" 