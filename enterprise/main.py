import sys
import os
import time
from dotenv import load_dotenv

# Добавляем корень проекта в путь, чтобы импортировать модули
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.ip_fetcher import IPFetcher
from src.core.geo_fetcher import GeoFetcher
from enterprise.map_visualizer import MapVisualizer

def print_effect(text, delay=0.05):
    """Эффект печатной машинки"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    load_dotenv()
    
    # Эффект "взлом системы"
    print("\n" + "="*60)
    print_effect("🔐 ИНИЦИАЛИЗАЦИЯ СИСТЕМЫ СЛЕЖЕНИЯ...", 0.1)
    print_effect("📡 Подключение к спутникам...", 0.1)
    print_effect("🌍 Поиск цели...", 0.1)
    print("="*60 + "\n")
    
    # Конфигурация
    config = {
        'ipinfo_token': os.getenv('IPINFO_TOKEN'),
        'ipify_url': 'https://api.ipify.org?format=json',
        'ipinfo_url_template': 'https://ipinfo.io/{ip}/json?token={token}',
        'timeout': 10
    }
    
    try:
        # Получаем IP
        ip_fetcher = IPFetcher(config)
        target_ip = ip_fetcher.get_ip()
        print_effect(f"🎯 ЦЕЛЬ ОБНАРУЖЕНА: {target_ip}", 0.05)
        
        # Получаем геоданные
        geo_fetcher = GeoFetcher(config)
        geo_data = geo_fetcher.get_geo(target_ip)
        
        city = geo_data.get('city', 'Unknown')
        region = geo_data.get('region', 'Unknown')
        loc = geo_data.get('loc', '')
        
        print_effect(f"📍 ГОРОД: {city}, {region}", 0.05)
        
        if loc:
            lat, lon = map(float, loc.split(','))
            print_effect(f"📡 КООРДИНАТЫ: {lat}, {lon}", 0.05)
            
            # Создаём карту
            print_effect("\n🛰️ ГЕНЕРАЦИЯ КАРТЫ СЛЕЖЕНИЯ...", 0.1)
            visualizer = MapVisualizer()
            visualizer.create_surveillance_map(lat, lon, city, zoom=15)
            visualizer.save_and_open("target_location.html")
            
            print_effect("\n✅ ЦЕЛЬ ЗАХВАЧЕНА. КАРТА ОТКРЫТА В БРАУЗЕРЕ", 0.05)
        else:
            print_effect("❌ КООРДИНАТЫ НЕ ПОЛУЧЕНЫ", 0.1)
            
    except Exception as e:
        print_effect(f"❌ ОШИБКА СИСТЕМЫ: {e}", 0.1)
    
    print("\n" + "="*60)
    print_effect("🔚 СЕАНС ЗАВЕРШЁН", 0.1)
    print("="*60 + "\n")

if __name__ == "__main__":
    main()