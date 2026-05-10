import os
from dotenv import load_dotenv

load_dotenv()

IPINFO_TOKEN = os.getenv("IPINFO_TOKEN")
YANDEX_DISK_TOKEN = os.getenv("YANDEX_DISK_TOKEN")

if not IPINFO_TOKEN or not YANDEX_DISK_TOKEN:
    raise ValueError("Tokens not found")

IPIFY_URL = "https://api.ipify.org?format=json"
IPINFO_URL_TEMPLATE = "https://ipinfo.io/{ip}/json?token={token}"
YANDEX_API_BASE = "https://cloud-api.yandex.net/v1/disk/resources"
REQUEST_TIMEOUT = 10

def get_config():
    return {
        "ipinfo_token": IPINFO_TOKEN,
        "yandex_token": YANDEX_DISK_TOKEN,
        "ipify_url": IPIFY_URL,
        "ipinfo_url_template": IPINFO_URL_TEMPLATE,
        "yandex_api_base": YANDEX_API_BASE,
        "timeout": REQUEST_TIMEOUT
    }