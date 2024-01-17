import requests
from bs4 import BeautifulSoup

def get_price_and_titles(urls, headers):
    df_titles, df_prices, discount_price = [], [], []
        for url in urls:
            # return all the data from the website
            page = requests.get(url, headers=HEADERS)
            # parse the information and pull individual items
            soup = BeautifulSoup(page.content, 'html.parser')
            # limit the amount of times to try and scrape data
            limit_find = 100
            title = None
            while title is None:
                title = soup.find(id="productTitle")
                limit_find -= 1
                if limit_find == 0:
                    print('Error: To many inquiries')
                    return [], [], []
            df_titles.append(title.get_text())
            price = None
            while price is None:
                price = soup.find("span", {"class": "a-price-whole"})
                limit_find -= 1
                if limit_find == 0:
                    print('Error: To many inquiries')
                    return [], [], []
            p = float(price.get_text()[0:2])
            df_prices.append(p)
            discount_price.append(p * 0.7)
        return df_titles, df_prices, discount_price
