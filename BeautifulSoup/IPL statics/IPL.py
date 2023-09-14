import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.iplt20.com/auction/2021"

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

table = soup.find("table", class_ = "ih-td-tab auction-tbl")

header = table.find_all("th")
header_list =[]

for i in header:
    head = i.text
    header_list.append(head)

df = pd.DataFrame(columns=header_list)

rows = table.find_all("tr")
row = []

for i in rows[1:]:
    first_td = i.find_all("td")[0].find("div", class_ ="ih-pt-ic").text.strip()
    data = i.find_all("td")[1:]
    row= [j.text for j in data]
    row.insert(0,first_td)
    l = len(df)
    df.loc[l] = row

df.to_excel("IPL_2021.xlsx")
