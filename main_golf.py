import requests,json,os,datetime;from dotenv import load_dotenv
load_dotenv();C={'ipinfo_token':os.getenv('IPINFO_TOKEN'),'yandex_token':os.getenv('YANDEX_DISK_TOKEN'),'ipify_url':'https://api.ipify.org?format=json','ipinfo_url_template':'https://ipinfo.io/{ip}/json?token={token}','yandex_api_base':'https://cloud-api.yandex.net/v1/disk/resources','timeout':10}
I=requests.get(C['ipify_url'],timeout=C['timeout']).json()['ip']
G=requests.get(C['ipinfo_url_template'].format(ip=I,token=C['ipinfo_token']),timeout=C['timeout']).json()
F=f"report_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
open(F,'w',encoding='utf-8').write(json.dumps(G,indent=4,ensure_ascii=False))
U=requests.get(f'{C["yandex_api_base"]}/upload',params={'path':f'/{F}'},headers={'Authorization':f'OAuth {C["yandex_token"]}'},timeout=C['timeout']).json()['href']
requests.put(U,data=open(F,'rb'),headers={'Authorization':f'OAuth {C["yandex_token"]}'},timeout=C['timeout'])
print(f"✅ {I} | {G.get('city')} | {F}")