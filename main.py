import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send a GET request to the website
    response = requests.get(url)

    # If the GET request is successful, the status code will be 200
    if response.status_code != 200:
        return None

    # Get the content of the response
    page_content = response.content

    # Create a BeautifulSoup object and specify the parser
    soup = BeautifulSoup(page_content, 'html.parser')

    # Find the product, price, image, and availability on the page
    product = soup.find('div', class_='product_main').find('h1').text
    price = soup.find('p', class_='price_color').text
    image = url + soup.find('div', class_='item active').find('img')['src']
    availability = soup.find('p', class_='instock availability').text.strip()

    # Return the data
    return {
        'product': product,
        'price': price,
        'image': image,
        'availability': availability,
    }

# Test the function
data = scrape_website('http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html')
print(data)
