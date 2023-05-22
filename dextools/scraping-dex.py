import requests
from bs4 import BeautifulSoup

url = "https://www.dextools.io/app/en/ether/pool-explorer"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url, headers=headers)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')
"""
datatable_body = soup.find('datatable-body')

if datatable_body:
   
    for row_wrapper in datatable_body.find_all('datatable-row-wrapper', class_='ng-star-inserted'):
      
        for body_cell in row_wrapper.find_all('datatable-body-cell', class_='ng-star-inserted'):
          
            cell_content = body_cell.text.strip()
            print(cell_content)
else:
    print("Elemento 'datatable-body' não encontrado.")
"""
with open('html-dex.txt', 'wb') as file:
        file.write(soup.encode('utf-8'))