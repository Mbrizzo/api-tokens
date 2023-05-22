from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import date

today = date.today()
date_string = today.strftime("%Y-%m-%d")

driver_service = webdriver.chrome.service.Service(ChromeDriverManager().install())
driver_service.start()
driver = webdriver.Chrome(service=driver_service)
# Carregar a página
url = f"https://explorer.bitquery.io/bsc/tokens?from={date_string}&till={date_string}"
driver.get(url)

# Localizar a tabela e extrair o conteúdo da tbody
html_content = driver.page_source
driver.quit()

soup = BeautifulSoup(html_content, 'html.parser')

rows = soup.find_all('tr')

for row in rows:

    name_element = row.find('a', href=True)
    name = getattr(name_element, 'text', '').strip()

    
    address_element = row.find_all('a', href=True)
    if len(address_element) > 0:
        address = address_element[-1]['href'].split('/')[-1]
    else:
        address = ''

    with open('name_and_address.txt', 'a') as file:
        file.write(f"Nome do Token: {name}\n")
        file.write(f"Endereço do Contrato: {address}\n")
        file.write("---\n")

    
    print('Nome do Token:', name)
    print('Endereço do Contrato:', address)
    print('---')

def honeyPot(address):
    pass
    if address == '<ENDEREÇO_HONEYPOT>':
        return True
    else:
        return False

honeypot = honeyPot(address)
print(honeypot)