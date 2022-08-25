import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent":
           "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv: 1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"}


for count in range(1,8):
    sleep(3)
    url = f"https://www.olx.ua/d/obyavlenie/karkasy-abazhurov-na-zakaz-IDP7XTL.html"

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")

    urls_people = soup.find_all("div", class_="css-r8u9sk")
    print(urls_people)

    # for i in urls_people:
    #
    #     name = i.find("h4", class_="card-title").text.strip()
    #     price = i.find("h5").text
    #     url_img = "https://scrapingclub.com" + i.find("img", class_="card-img-top img-fluid").get("src")
    #     print(name, price, url_img)