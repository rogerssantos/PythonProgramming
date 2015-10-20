import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page < max_pages:
        url = 'https://www.thenewboston.com/trade/search.php?pages=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text