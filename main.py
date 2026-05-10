# Точка входа в приложение IP Detector
# Этот файл запускает всю программу
import datetime
import json
# Импортируем нашу конфигурацию
from config import get_config
# Импортируем класс из папки src/core
from src.core.ip_fetcher import IPFetcher
from src.core.geo_fetcher import GeoFetcher
from src.core.yandex_uploader import YandexDiskUploader

def main():
    """
    Главная функция программы.
    Запускает последовательность:
    1. Получение IP
    2. Получение геоданных
    3. Сохранение в JSON
    4. Загрузка на Яндекс.Диск
    """
    # Загружаем все настройки одним вызовом
    config = get_config()
    
    print("=" * 50)
    print(" IP Detector - Определение геолокации")
    print("=" * 50)
    print(f"✅ Конфигурация загружена")
    print(f"🔑 Токен ipinfo: {'✓' if config['ipinfo_token'] else '✗'}")
    print(f"🔑 Токен Яндекс.Диск: {'✓' if config['yandex_token'] else '✗'}")
    print("=" * 50)
        # Создаем экземпляр класса и передаем ему настройки
    ip_fetcher = IPFetcher(config)  # создаём объект класса. В этот момент срабатывает __init__, и конфиг сохраняется внутри объекта.
    
    # Вызываем метод и сохраняем результат
        # Пытаемся выполнить запрос. Если сеть отвалится или API вернет ошибку — программа не упадёт, а перейдёт в except
    try:
        current_ip = ip_fetcher.get_ip()
        print(f"🌍 Твой внешний IP: {current_ip}")
    except Exception as e:
            # e — это объект ошибки. str(e) превратит его в читаемый текст для пользователя
        print(f"❌ Не удалось получить IP: {e}")
    print("\n🚀 Запуск программы...")
    print("⏳ В разработке...")
        # --- ТЕСТ ГЕО-ФЕТЧЕРА ---
    try:
        geo_fetcher = GeoFetcher(config)
        geo_data = geo_fetcher.get_geo(current_ip)
            
        print(f"📍 Город: {geo_data.get('city', 'Неизвестно')}")
        print(f"📍 Регион: {geo_data.get('region', 'Неизвестно')}")
        print(f"📍 Координаты: {geo_data.get('loc', 'Неизвестно')}")
        print(f"📍 Провайдер: {geo_data.get('org', 'Неизвестно')}")
            # Формируем итоговый словарь с данными для сохранения
        # --- ФОРМИРУЕМ ИМЯ ФАЙЛА С ДАТОЙ ---
        now = datetime.datetime.now()
        # Формат: report_2026-05-10_17-30-00.json
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"report_{timestamp}.json"
        
        print(f"💾 Сохраняем отчёт в: {filename}")        
        report_data = {
            "ip": current_ip,
            "city": geo_data.get('city'),
            "region": geo_data.get('region'),
            "country": geo_data.get('country'),
            "loc": geo_data.get('loc'),
            "org": geo_data.get('org'),
            "timezone": geo_data.get('timezone')
            }
            # Открываем файл для записи (utf-8 важен для русских названий городов)
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(report_data, f, indent=4, ensure_ascii=False)
            # --- ЗАГРУЗКА НА ДИСК ---
            print("\n📤 Загрузка на Яндекс.Диск...")
            
            # Создаем загрузчик
            uploader = YandexDiskUploader(config)
            
            # Загружаем файл result.json в корень Диска как report.json
            uploader.upload_file(filename, f'/{filename}')
            
            print("✅ Всё готово! Проверь свой Яндекс.Диск.")
    except Exception as e:
        print(f"❌ Ошибка получения гео-данных: {e}")

# Эта конструкция гарантирует, что код выполнится только при прямом запуске
# Если мы импортируем main.py в другом файле - код НЕ выполнится
if __name__ == "__main__":
    main()