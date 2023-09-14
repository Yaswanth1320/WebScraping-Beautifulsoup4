import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://www.howstat.com/cricket/statistics/IPL/BattingMostAgg.asp?q=3"

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

table = soup.find("table", class_ = "TableLined")


row_1 = table.find_all("tr")[0]
cols = row_1.find_all('td')
header_list =[]

for j in cols:
    data = j.text.strip()
    header_list.append(data)


df = pd.DataFrame(columns=header_list)
    
rows = table.find_all("tr")
row_list =[]

for i in rows[1:51]:
    cols =i.find_all('td')
    row_list=[j.text.strip() for j in cols]
    l = len(df)
    df.loc[l] = row_list
    

df.to_excel("IPL_Most_runs.xlsx")

