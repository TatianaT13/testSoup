import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import tkinter as tk
from tkinter import messagebox

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
    image_relative_url = soup.find('div', class_='item active').find('img')['src']
    image_url = urljoin(url, image_relative_url)
    availability = soup.find('p', class_='instock availability').text.strip()

    # Return the data
    return {
        'product': product,
        'price': price,
        'image': image_url,
        'availability': availability,
    }

def scrape_and_display():
    url = url_entry.get()
    data = scrape_website(url)
    if data is not None:
        messagebox.showinfo("Scraping Results", f"Product: {data['product']}\nPrice: {data['price']}\nImage: {data['image']}\nAvailability: {data['availability']}")
    else:
        messagebox.showerror("Error", "Failed to scrape the website.")

# Create a Tkinter window
window = tk.Tk()

# Create a label and entry for the URL
url_label = tk.Label(window, text="URL:")
url_label.pack()
url_entry = tk.Entry(window)
url_entry.pack()

# Create a button to start the scraping
scrape_button = tk.Button(window, text="Scrape", command=scrape_and_display)
scrape_button.pack()

# Start the Tkinter event loop
window.mainloop()
