import folium
import webbrowser
import os
import time

class MapVisualizer:
    def __init__(self):
        self.map = None
        
    def create_surveillance_map(self, lat, lon, city, zoom=13):
        """Создаёт карту с анимированным зумом от глобуса до цели"""
        # Создаём карту
        self.map = folium.Map(
            location=[lat, lon],
            zoom_start=3,  # Начинаем с глобуса
            tiles='OpenStreetMap'
        )
        
        # Добавляем спутниковый слой
        folium.TileLayer(
            tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
            attr='ESRI',
            name='Satellite',
            overlay=True,
            control=True
        ).add_to(self.map)
        
        # Добавляем маркер
        folium.Marker(
            location=[lat, lon],
            popup=f"🎯 TARGET: {city}\n📍 {lat}, {lon}",
            icon=folium.Icon(color='red', icon='exclamation-sign', prefix='fa'),
            tooltip="ЦЕЛЬ ОБНАРУЖЕНА"
        ).add_to(self.map)
        
        # Добавляем круг
        folium.Circle(
            location=[lat, lon],
            radius=1000,
            color='red',
            fill=True,
            fill_color='red',
            fill_opacity=0.3
        ).add_to(self.map)
        
        # Добавляем переключатель слоёв
        folium.LayerControl().add_to(self.map)
        
        return self.map
    
    def save_and_open(self, filename="surveillance_map.html"):
        """Сохраняет карту с анимацией зума и открывает в Chrome"""
        filepath = os.path.join(os.path.dirname(__file__), filename)
        
        # Сначала сохраняем базовую карту
        self.map.save(filepath)
        
        # Читаем сохранённый HTML и добавляем анимацию
        with open(filepath, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Добавляем JavaScript для анимации зума
        animation_script = """
        <script>
        // Анимированный зум от глобуса до цели
        setTimeout(function() {
            var map = Object.values(document.getElementsByTagName('script'))
                .find(s => s.innerHTML.includes('L.map'))
                .innerHTML.match(/map_([a-f0-9]+)/);
            
            // Получаем карту Leaflet
            var m = window.Object.values(window).find(v => v && v._leaflet_id);
            
            if (m) {
                // Координаты цели
                var targetLat = """ + str(self.map.location[0]) + """;
                var targetLon = """ + str(self.map.location[1]) + """;
                
                // Анимация зума
                var zoomLevels = [3, 5, 8, 11, 13, 15];
                var delay = 0;
                
                zoomLevels.forEach(function(zoom, index) {
                    setTimeout(function() {
                        m.setView([targetLat, targetLon], zoom, {
                            animate: true,
                            duration: 2
                        });
                    }, index * 1500);
                });
            }
        }, 1000);
        </script>
        """
        
        # Вставляем скрипт перед закрывающим </body>
        html_content = html_content.replace('</body>', animation_script + '</body>')
        
        # Сохраняем обновлённый HTML
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # Открываем в Google Chrome
        chrome_path = None
        
        # Пробуем найти Chrome
        chrome_paths = [
            "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
            "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
            "/usr/bin/google-chrome",
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        ]
        
        for path in chrome_paths:
            if os.path.exists(path):
                chrome_path = path
                break
        
        # Открываем в браузере
        if chrome_path:
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open(f'file://{os.path.abspath(filepath)}')
        else:
            # Если Chrome не найден, открываем в браузере по умолчанию
            webbrowser.open(f'file://{os.path.abspath(filepath)}')
        
        print(f"🛰️ Карта открыта в браузере: {filepath}")