import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_product_info(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.5"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return []
    except Exception as err:
        print(f"An error occurred: {err}")
        return []
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    products = []
    
    for item in soup.select('.s-result-item'):
        name = item.h2.text if item.h2 else 'N/A'
        price = item.find('span', 'a-price-whole').text if item.find('span', 'a-price-whole') else 'N/A'
        rating = item.find('span', 'a-icon-alt').text if item.find('span', 'a-icon-alt') else 'N/A'
        if ((name=='N/A') or (price=='N/A') or (rating=='N/A')):
            continue
        products.append({
            'Name': name,
            'Price': price,
            'Rating': rating
        })
    
    return products

def main():
    url = input("Please enter the URL of the e-commerce page: ")

    product_info = extract_product_info(url)

    if product_info:
        df = pd.DataFrame(product_info)
        df.to_csv('products.csv', index=False)
        print("Product information has been saved to 'products.csv'")
    else:
        print("No product information found or an error occurred.")

if __name__ == "__main__":
    main()
