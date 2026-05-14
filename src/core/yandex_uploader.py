import requests
import logging

class YandexDiskUploader:
    def __init__(self, config):
        self.token = config['yandex_token']
        self.base_url = config['yandex_api_base']
        self.timeout = config['timeout']

    def get_upload_url(self, file_path, overwrite=True):
        params = {'path': file_path}
        if overwrite:
            params['overwrite'] = 'true'
            
        headers = {'Authorization': f'OAuth {self.token}'}
        response = requests.get(f'{self.base_url}/upload', params=params, headers=headers, timeout=self.timeout)
        response.raise_for_status()
        return response.json()['href']

    def upload_file(self, local_file_path, disk_file_path, overwrite=True):
        upload_url = self.get_upload_url(disk_file_path, overwrite=overwrite)
        
        with open(local_file_path, 'rb') as f:
            # Pre-signed ссылка уже содержит авторизацию, заголовок убираем
            response = requests.put(upload_url, data=f, timeout=self.timeout)
            response.raise_for_status()
            
        logging.info(f"✅ Файл успешно загружен: {disk_file_path}")