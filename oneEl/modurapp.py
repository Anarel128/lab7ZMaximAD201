import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def parc(url, n):
    headers = {"User-Agent":UserAgent().random}
    urlf = url
    response = requests.get(urlf, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    data = soup.find_all("tr", {"class": "wrap"})
    main_l = []
    b = 0
    for data in data:
        if b < n:
            name = data.find("strong").text.replace("\n","")
            main_l.append(name)
            b+=1


    return main_l

