import requests
from bs4 import BeautifulSoup

url = "https://www.dextools.io/app/en/ether/pool-explorer"

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')