import requests
from bs4 import BeautifulSoup
import pandas

url = "https://ticker.finology.in"
r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

table = soup.find("table", class_ = "table table-sm table-hover screenertable")

headers = table.find_all("th")

header_list =[]
for i in headers:
    header = i.text
    header_list.append(header)

df = pandas.DataFrame(columns=header_list)

data = table.find_all("tr")

for i in data[1:]:
    row = i.find_all("td")
    data_row = [tr.text for tr in row]
    l = len(df)
    df.loc[l] = data_row

df.to_excel("data.xlsx")