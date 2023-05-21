"""
import requests
from bs4 import BeautifulSoup

url = 'https://explorer.bitquery.io/bsc/'  # Substitua pela URL correta do Bitquery

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
"""
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium import webdriver

driver_service = webdriver.chrome.service.Service(ChromeDriverManager().install())
driver_service.start()
driver = webdriver.Chrome(service=driver_service)
# Carregar a página
driver.get('https://explorer.bitquery.io/bsc/tokens?from=2023-05-21&till=2023-05-21')

# Localizar a tabela e extrair o conteúdo da tbody
table_element = driver.find_element(By.XPATH, '//div[@class="table-responsive"]//table')
tbody_element = table_element.find_element(By.TAG_NAME, 'tbody')
tbody_html = tbody_element.get_attribute('innerHTML')


# Imprimir o conteúdo da tbody
print(tbody_html)

driver.quit()
