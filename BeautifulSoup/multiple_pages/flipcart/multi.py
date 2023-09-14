import requests
from bs4 import BeautifulSoup
import pandas as pd

name_list = []
prices_list = []
desc_list  =[]
review_list = []

for i in range(1,15):
    website_url = "https://www.flipkart.com/search?q=mobiles+under+50000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_19_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_19_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobiles+under+50000%7CMobiles&requestId=65eff265-23e3-45a5-98f3-f691588444e6&as-searchtext=mobiles+under+50000&page="+str(i)
    r = requests.get(website_url)
    
    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_ = "_1YokD2 _3Mn1Gg")
    
    names = box.find_all("div", class_ = "_4rR01T")
    
    for i in names:
        name = i.text
        name_list.append(name)
    
    prices = box.find_all("div", class_= "_30jeq3 _1_WHN1")
    
    for i in prices:
        price = i.text
        prices_list.append(price)
    
    desc = box.find_all("ul", class_ = "_1xgFaf")
    
    for i in desc :
        description = i.text
        desc_list.append(description)
    
    
    reviews = box.find_all("div", class_ = "_3LWZlK")
    
    for i in reviews:
        rev = i.text
        review_list.append(rev)
    
    loop = len(name_list)== len(prices_list)== len(desc_list)== len(review_list)
    print(loop)

print(len(name_list))
print(len(prices_list))
print(len(desc_list))
print(len(review_list))

df = pd.DataFrame({"Product Name ": name_list, "Product_price": prices_list, "Description": desc_list, "Product_review": review_list})
df.to_excel("flipcart.xlsx")


