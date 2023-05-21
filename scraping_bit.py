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

table_element = soup.find('div', class_='table-responsive').find('table')
tbody_element = table_element.find('tbody')

with open('tbody.txt', 'wb') as file:
        file.write(tbody_element.encode('utf-8'))