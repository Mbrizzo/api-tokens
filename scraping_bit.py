import requests
from bs4 import BeautifulSoup

url = 'https://explorer.bitquery.io/bsc/dex_tokens?from=2023-05-19&till=2023-05-19'  # Substitua pela URL correta do Bitquery

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}
response = requests.get(url)


if response.status_code == 200:
    
    soup = BeautifulSoup(response.content, 'html.parser')   
    body = soup.find('body')
    with open('body.txt', 'wb') as file:
        file.write(body.encode('utf-8'))
else:   
    print('Erro na solicitação:', response.status_code)
