import requests
# Конфиг читается в main.py и передаётся в класс через __init__.
# Fetcher не зависит от файлов, работает только с переданными данными.
class IPFetcher:
    def __init__(self, config):        
        self.config = config
    def get_ip(self):
        """Отправляет запрос к API и получает IP."""
        
        # requests.get() отправляет запрос. 
        # timeout нужен, чтобы программа не зависла, если нет интернета.
        response = requests.get(self.config['ipify_url'], timeout=self.config['timeout'])
                # Проверяем статус ответа. Если ошибка (404, 500 и т.д.) - выбросит исключение
        response.raise_for_status()
        # Автоматическая проверка успеха. Если сервер вернул ошибку (например, сайт недоступен или лимит исчерпан), программа сама остановится с чётким сообщением.
        # Парсим JSON-ответ в словарь Python и забираем значение по ключу 'ip'
        return response.json()['ip']