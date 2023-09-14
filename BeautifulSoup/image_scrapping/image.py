import requests
from bs4 import BeautifulSoup

url = "https://yaswanth1320.github.io/travel-website/"
r = requests.get("https://yaswanth1320.github.io/travel-website/")

soup=BeautifulSoup(r.text,'lxml')

box = soup.find("div", class_ = "image")
image = box.find("img")
image_url = image['src']
full_url = url + image_url

img_data = requests.get(full_url).content
with open('travel.jpg', 'wb') as handler:
    handler.write(img_data)