import requests
from bs4 import BeautifulSoup
import pandas as pd
proxy_df = pd.DataFrame(columns=['ip', 'Port', 'Country', 'Autonomy', 'Type', 'Response time'])
import random

Headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
           'accept': '*/*'}

def get_html(url, params=None):
    r = requests.get(url, headers=Headers, params=params)
    return r

proxy_list = []
mini_list = []

def get_page_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    line = soup.find('div', class_='table_block').find('table').find('tbody').find_all('tr')

    for tr in line:
        mini_list = []
        td = tr.find_all('td')
        ip = td[0].text
        port = td[1].text
        proxy_data = {'ip': ip,
                'Port': port}
        mini_list.append(proxy_data['ip'])
        mini_list.append(proxy_data['Port'])
        proxy_list.append(mini_list)

def proxy_f():
    url = 'https://hidemy.name/ru/proxy-list/'
    html = get_html(url)
    if html.status_code == 200:
        get_page_data(html.text)
        df_proxy = pd.DataFrame(columns=['ip', 'port'], data=proxy_list)
        df_proxy.to_csv('proxyxel.csv')
    else:
        print('Error connection...')
        print('Check your internet connection, please!')

proxy_f()
print('Well done!')

def get_rndm_one_proxy():
    proxy_df = pd.read_csv('proxyxel.csv')
    ip_list = proxy_df['ip'].tolist()
    port_list = proxy_df['port'].tolist()
    i = random.randint(0, len(ip_list))
    ip = ip_list[i]
    port = port_list[i]
    proxies = {'https': 'https://' + str(ip) + ':' + str(port)}
    print('One random proxy from proxies, we founded ', '\n', proxies)
    return proxies






