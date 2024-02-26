# from fake_useragent import UserAgent
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC

from requests_html import HTMLSession


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

    def settings(self):
       global session
       session = HTMLSession()
        # global driver

        # options = webdriver.FirefoxOptions()
        # # options.add_argument("--headless")
        # options.add_argument("--width=800")
        # options.add_argument("--height=600")
        # options.set_preference("general.useragent.override", UserAgent().random)
        # driver = webdriver.Firefox(options=options)
        # driver.implicitly_wait(10) # seconds



    def loader(self):

        for link in self.link:
            response = session.get(link)
            # print(link)
            print(response.html.absolute_links)
        # for link in self.link:
            # driver.get(link)
        # elem = driver.find_element(By.NAME, "q")
        # elem.clear()
        # elem.send_keys("pycon")
        # elem.send_keys(Keys.RETURN)

def main():
    Parser().settings()
    Parser().loader()
    # driver.close()


if __name__ == "__main__":
    main()
