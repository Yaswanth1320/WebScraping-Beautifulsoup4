import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

names = soup.find_all("a", class_ ="title")

product_names = []
for i in names:
    name = i.text
    product_names.append(name)


prices = soup.find_all("h4", class_ ="pull-right price")

price_list = []
for i in prices:
    price = i.text
    price_list.append(price)

desc = soup.find_all("p", class_ = "description")

dec_list = []
for i in desc:
    des = i.text
    dec_list.append(des)

print(dec_list)

reviews = soup.find_all("p", class_ = "pull-right")

review_list = []
for i in reviews:
    review = i.text
    review_list.append(review)

df = pd.DataFrame({"Products Name": product_names, "Prices": price_list, "Description": dec_list, "Review": review_list})

print(df)

df.to_excel("Product_details.xlsx")


