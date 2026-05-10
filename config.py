import os
from dotenv import load_dotenv
# python-dotenv - библиотека для работы с .env файлами
# load_dotenv() - функция, которая читает файл .env и загружает
# переменные в среду Python, делая их доступными через os.getenv()
# Эта команда читает файл .env и "выливает" его содержимое в переменные среды Python
load_dotenv()
# Получаем токены из переменных окружения
# os.getenv() безопасно достаёт значение по имени переменной
IPINFO_TOKEN = os.getenv("IPINFO_TOKEN")
YANDEX_DISK_TOKEN = os.getenv("YANDEX_DISK_TOKEN")

# Проверяем, что токены действительно существуют
# Если хоть один пустой — останавливаем программу с понятной ошибкой
if not IPINFO_TOKEN or not YANDEX_DISK_TOKEN:
    raise ValueError("❌ Ошибка: не найдены токены в файле .env! Проверьте, что файл существует и заполнен.")
# --- КОНСТАНТЫ (настройки проекта) ---

# Ссылки на API
IPIFY_URL = "https://api.ipify.org?format=json"
# Шаблон для ipinfo: {ip} и {token} мы подставим позже через format()
IPINFO_URL_TEMPLATE = "https://ipinfo.io/{ip}/json?token={token}"

# Базовый адрес API Яндекс.Диска
YANDEX_API_BASE = "https://cloud-api.yandex.net/v1/disk/resources"

# Таймаут (в секундах)
# Сколько времени ждем ответ от сервера. Если сеть плохая — не висим бесконечно, а прерываемся
REQUEST_TIMEOUT = 10
def get_config():
    """
    Возвращает словарь со всеми настройками проекта.
    Удобно передавать в другие модули одним объектом.
    """
    return {
        "ipinfo_token": IPINFO_TOKEN,
        "yandex_token": YANDEX_DISK_TOKEN,
        "ipify_url": IPIFY_URL,
        "ipinfo_url_template": IPINFO_URL_TEMPLATE,
        "yandex_api_base": YANDEX_API_BASE,
        "timeout": REQUEST_TIMEOUT
    }

# Для отладки: выводим сообщение при импорте config.py
print("✅ Конфигурация загружена успешно!")