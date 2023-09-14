import requests
from bs4 import BeautifulSoup
import pandas as pd

print("Enter the your programming skill")
skill = input(">")
r = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=")
soup = BeautifulSoup(r.text, "lxml")

jobs = soup.find_all("li", class_ = "clearfix job-bx wht-shd-bx")
company_list = []
skills_list = []
date_list = []

for job in jobs:
    skills = job.find("span", class_ = "srp-skills").text.strip()
    if skill in skills: 
        skills_list.append(skills)
        date = job.find("span", class_ = "sim-posted").text.strip()
        date_list.append(date)
        company = job.find("h3", class_ = "joblist-comp-name").text.strip()
        company_list.append(company)
        
        

df = pd.DataFrame({"Company Name":company_list, "Skills": skills_list, "Published Date": date_list})

df.to_excel("jobs1.xlsx")