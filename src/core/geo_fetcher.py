import requests

class GeoFetcher:
    """Класс для получения гео-данных через сервис ipinfo.io"""
    def __init__(self, config):
        # Сохраняем конфиг для общего доступа
        self.config = config
        # Сразу достаём токен в отдельную переменную — так удобнее писать запросы
        self.token = config['ipinfo_token'] # Поскольку ipinfo требует токен в каждом запросе, мы сразу «вытаскиваем» его в self.token. Это избавит от повторений config['ipinfo_token'] в методах ниже.
    def get_geo(self, ip):
        """Формирует ссылку и готовит запрос к ipinfo."""
        # Подставляем IP и токен в шаблон из конфига
        url = self.config['ipinfo_url_template'].format(ip=ip, token=self.token)
        # Отправляем запрос к API с таймаутом из конфига
        response = requests.get(url, timeout=self.config['timeout'])
        response.raise_for_status()  # Автоматическая проверка на ошибки сервера
        # Превращаем JSON-ответ в словарь Python
        data = response.json()
        
        # Возвращаем весь словарь с данными
        return data
    


