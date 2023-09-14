import pandas
import requests
from bs4 import BeautifulSoup

website_url = "https://www.airbnb.co.in/s/Hyderabad--Telangana/homes?adults=1&refinement_paths%5B%5D=%2Fhomes&tab_id=home_tab&query=Hyderabad%2C%20Telangana&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-10-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click&place_id=ChIJx9Lr6tqZyzsRwvu6koO3k64"

r = requests.get(website_url) 
soup = BeautifulSoup(r.text, "lxml")
names_list = []
prices_list = []
rating_list = []    
desc_list = []

for i in range(1,10):
    page = soup.find("a", class_ = "l1ovpqvx c1ytbx3a dir dir-ltr").get("href")
    next_page = "https://www.airbnb.co.in"+page

    website_url = next_page
    r = requests.get(website_url) 
    soup = BeautifulSoup(r.text, "lxml")

    names = soup.find_all("div", class_ = "t1jojoys dir dir-ltr")

    for i in names:
        name = i.text
        names_list.append(name)

    prices = soup.find_all("div", class_ = "pquyp1l dir dir-ltr")

    for i in prices:
        price = i.text
        prices_list.append(price)

    rating = soup.find_all("span", class_ = "r1dxllyb dir dir-ltr")

    for i in rating:
        rate = i.text
        rating_list.append(rate)

    desc = soup.find_all("span", class_ = "t6mzqp7 dir dir-ltr")

    for i in desc:
        data = i.text
        desc_list.append(data)

print(len(names_list))
print(len(prices_list))
print(len(rating_list))
print(len(desc_list))

df = pandas.DataFrame({"Name":names_list, "Price": prices_list, "Rating": rating_list, "Description": desc_list})

df.to_excel("Airbnb.xlsx")
print(df)




    


