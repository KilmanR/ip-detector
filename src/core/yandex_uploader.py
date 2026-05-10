import requests
import os

class YandexDiskUploader:
    """Класс для загрузки файлов на Яндекс.Диск"""
    def __init__(self, config):
        # Сохраняем токен Яндекс.Диска
        self.token = config['yandex_token']
        # Базовый URL API
        self.base_url = config['yandex_api_base']
        # Таймаут для запросов
        self.timeout = config['timeout']
    def get_upload_url(self, file_path):
        """
        Запрашивает у Яндекса временную ссылку для загрузки файла.
        file_path — путь к файлу на Диске (например, '/report.json')
        """
        # Параметры запроса: куда сохранить файл на Диске
        params = {'path': file_path}
        
        # Заголовки с авторизацией
        headers = {'Authorization': f'OAuth {self.token}'}
        # Отправляем запрос на получение ссылки для загрузки
        response = requests.get(
            f'{self.base_url}/upload',
            params=params,
            headers=headers,
            timeout=self.timeout
        )
        response.raise_for_status()
        
        # Извлекаем ссылку из JSON-ответа
        return response.json()['href']
    def upload_file(self, local_file_path, disk_file_path):
        """
        Загружает файл на Яндекс.Диск.
        local_file_path — путь к файлу на компьютере
        disk_file_path — путь, где сохранить на Диске
        """
        # Получаем ссылку для загрузки
        upload_url = self.get_upload_url(disk_file_path)
        # Читаем файл в бинарном режиме ('rb' работает для любых файлов: json, txt, jpg)
        with open(local_file_path, 'rb') as f:
            # Яндекс требует метод PUT для отправки данных по временной ссылке
            response = requests.put(
                upload_url,
                data=f,  # Передаём открытый файл как поток данных
                headers={'Authorization': f'OAuth {self.token}'},
                timeout=self.timeout
            )
            response.raise_for_status()
            print(f"✅ Файл успешно загружен на Яндекс.Диск: {disk_file_path}")
