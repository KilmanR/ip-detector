import requests

class YandexDiskUploader:
    def __init__(self, config):
        self.token = config['yandex_token']
        self.base_url = config['yandex_api_base']
        self.timeout = config['timeout']

    def get_upload_url(self, file_path):
        params = {'path': file_path}
        headers = {'Authorization': f'OAuth {self.token}'}
        response = requests.get(f'{self.base_url}/upload', params=params, headers=headers, timeout=self.timeout)
        response.raise_for_status()
        return response.json()['href']

    def upload_file(self, local_file_path, disk_file_path):
        upload_url = self.get_upload_url(disk_file_path)
        with open(local_file_path, 'rb') as f:
            response = requests.put(
                upload_url,
                data=f,
                headers={'Authorization': f'OAuth {self.token}'},
                timeout=self.timeout
            )
            response.raise_for_status()