import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


headers = {"User-Agent": UserAgent().random}    

class Parser:

    def __init__(self):
        self.link = [
            "https://www.radioparts.com.au/category/consumer-electronics",
            "https://www.radioparts.com.au/category/av-accessories",
            "https://www.radioparts.com.au/category/public-address",
            "https://www.radioparts.com.au/category/tv-and-satellite",
            "https://www.radioparts.com.au/category/communications",
            "https://www.radioparts.com.au/category/security-and-intercoms",
            "https://www.radioparts.com.au/category/appliances-and-lighting",
            "https://www.radioparts.com.au/category/cables-and-cable-accessories",
            "https://www.radioparts.com.au/category/it-supplies",
            "https://www.radioparts.com.au/category/power",
            "https://www.radioparts.com.au/category/components",
            "https://www.radioparts.com.au/category/service"
                ]


    @staticmethod
    def parsing(html):

        def dressing_function():
            # ныряет
            pass

        def receiving_function(link):
            # получает

            if BeautifulSoup(link.text, "")
            session = HTMLSession()

            response = session.get(link)
            

        print("Начинаем парсить")

        bs = BeautifulSoup(html, "html.parser")

        links = [link.find("a").attrs["href"] for link in bs.find_all("div", {"class": "cv-zone-category product"})]

        for link in links:
            internal_link = requests.get(f"https://www.radioparts.com.au{link}", headers=headers)
            if BeautifulSoup(internal_link.text, "html.parser").find("div", {"class": "cv-zone-category product" }):
                dressing_function()
                print("true block")
            else:
                receiving_function(f"https://www.radioparts.com.au{link}")
                print("false block")



    def loader(self):
        for link in self.link:
            print("Загружаем ссылку - ", link)
            session = requests.get(link, headers=headers)
            print("Статус код", session.status_code)
            self.parsing(session.text)



def main():

    Parser().loader()
    # driver.close()


if __name__ == "__main__":
    main()
