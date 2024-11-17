import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    return response.text

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    listings = soup.find_all('article', class_='list-card')
    data = []
    for listing in listings:
        address = listing.find('address', class_='list-card-addr').text
        price = listing.find('div', class_='list-card-price').text
        data.append({'address': address, 'price': price})
    return data

def create_dataframe(data):
    df = pd.DataFrame(data)
    return df

def main():
    url = "https://www.zillow.com/homes/Los-Angeles,-CA_rb/"
    html = fetch_html(url)
    data = parse_html(html)
    df = create_dataframe(data)
    df.to_csv('zillow_listings.csv', index=False)

if __name__ == "__main__":
    main()
