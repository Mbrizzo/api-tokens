from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import date

# Configurar as opções do Chrome
options = Options()
options.add_argument("--headless")  # Executar o navegador em modo headless
options.add_argument("--no-sandbox")  # Desativar o sandbox para evitar problemas de permissões

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
options.add_argument(f"user-agent={user_agent}")

driver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service, options=options)

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

contracts = []

for row in rows:
    name_element = row.find('a', href=True)
    name = getattr(name_element, 'text', '').strip()

    address_element = row.find_all('a', href=True)
    if len(address_element) > 0:
        address = address_element[-1]['href'].split('/')[-1]
        contracts.append(address)

        with open('./name_and_address.txt', 'a') as file:
            file.write(f"Nome do Token: {name}\n")
            file.write(f"Endereço do Contrato: {address}\n")
            file.write("---\n")

        print('Nome do Token:', name)
        print('Endereço do Contrato:', address)
        print('---')
"""
print("Lista de Contratos:")
for contract in contracts:
    print(contract)
"""
for contract in contracts:    
    honeypot_url = "https://honeypot.is/"
    driver.get(honeypot_url)
    
    address_input = driver.find_element(By.ID, 'address')
    address_input.clear()
    address_input.send_keys(contract)
    
    check_button = driver.find_element(By.ID, 'check4hp')
    check_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'summary-subheading')))
    
    summary_heading = driver.find_element(By.ID, 'summary-heading')
    summary_subheading = driver.find_element(By.ID, 'summary-subheading')
    result = summary_subheading.text.strip()

    # Imprimir o resultado para cada contrato
    print('Contrato:', contract)
    print('Resumo:', summary_heading.text.strip())
    print('Descrição:', result)
    print('---')