from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import requests
import time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


headers = {"User-Agent": UserAgent().random}    

options = webdriver.ChromeOptions()
options.add_argument("--headless")
# options.add_argument("--width=800")
# options.add_argument("--height=600")
options.add_argument(f"User-Agent={UserAgent().random}")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(100) # seconds

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

            html = requests.get(link, headers=headers)

            while True:
                if BeautifulSoup(html.text, "html.parser").find("button", {"class": "btn cv-refresh"}):
                    print("Обнаружена кнопка")
                    driver.get(link)
                    time.sleep(5)
                    iframe = driver.find_element(By.CSS_SELECTOR, "#cv-zone-pagecontent-after")
                    ActionChains(driver).scroll_to_element(iframe).perform()
                    time.sleep(5)
                    driver.find_element(By.CSS_SELECTOR, ".cv-refresh").click()
                    time.sleep(5)
                    main_page = driver.find_element(By.TAG_NAME, "html")
                    html = main_page.get_attribute("innerHTML")
                    bs = BeautifulSoup(html, "html.parser").find_all("div", {"class": "product"})
                    print(len(bs))
                else:
                    break

                driver.close()
                
                exit()


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
