"""import sys
import requests
from bs4 import BeautifulSoup



sys.stdout = open("test.txt", "w")



URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()"""
import sys
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re


##### Web scrapper for infinite scrolling page #####
driver = webdriver.Chrome()
driver.get("https://archive.org/search.php?query=collection%3A%28pastpages%29&and[]=year%3A%222018%22")
time.sleep(10)  # Allow 2 seconds for the web page to open
scroll_pause_time = 5 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
last_height = driver.execute_script("return document.body.scrollHeight;")   # get the screen height of the web

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    i=0
    new_height = driver.execute_script("return document.body.scrollHeight")
    while(new_height==last_height):
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        i+=1
        if(i==50):
            break
    

    if new_height == last_height:
        break
    last_height = new_height
    


soup = BeautifulSoup(driver.page_source, "html.parser")

items = soup.find_all("div", class_="item-ttl C C2")
sys.stdout = open("onf1.txt", "w")
base = "archive.org"

for item in items:
    link = item.find('a')['href']
    print(base+link)

"""
results = soup.find(id="ikind--week")
job_elements = results.find_all("div", class_="card-content")

for parent in soup.find_all(class_="y8HYJ-y_lTUHkQIc1mdCq _2INHSNB8V5eaWp4P0rY_mE"):
    a_tag = parent.find("a", class_="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE")
print("test")
for parent in soup.find_all(class_="C234"):
    a_tag = parent.find("a", class_="item-ttl")
    base = "archive.org"
    link = a_tag.attrs['href']
    url = urljoin(base, link)
    urls.append(url)
print(urls)

for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    print (link.get('href'))
print("end")"""