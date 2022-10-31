import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

driver_service = Service("drivers\geckodriver.exe")
driver_options = Options()
driver_options.binary_location=r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(service=driver_service, options=driver_options)
web_page = driver.get("https://www.hl.co.uk")

stock_info = {"stock_code":[], "comp_name":[],"current_price":[], "unit_day_change":[], "pct_day_change":[]}

class Scraper:
    def __init__(self):
        pass
        
    def accept_cookies(self, driver):
        driver.implicitly_wait(2)
        cookies_path = driver.find_element(by= By.XPATH, value='//*[@id="acceptCookieButton"]')
        cookies_path.click()

    def get_ftse250_table(self, driver):
        driver.implicitly_wait(5)
        shares_path = driver.find_element(by=By.XPATH, value='//*[@id="nav16516"]').click()
        market_path = driver.find_element(by=By.XPATH, value='//*[@id="markets_uk"]')
        ftse_250_path = driver.find_element(by=By.XPATH, value='/html/body/main/div/div/div[2]/div[5]/div[1]/div[1]/table/tbody/tr[2]/td[1]/a').click()
        table_path= driver.find_elements(by=By.XPATH, value='//tr')

    def get_stock_epic(self, driver):
        driver.implicitly_wait(5)
        stock_data = driver.find_elements(by=By.XPATH, value='//td')
        epic = driver.find_elements(by=By.XPATH, value= '//td[1]')
        for info in epic[4:-4]:
            info=info.text
            stock_info["stock_code"].append(info)

    def get_comp_name(self, driver):
        driver.implicitly_wait(5)
        stock_data = driver.find_elements(by=By.XPATH, value='//td')
        comp_name = driver.find_elements(by=By.XPATH, value= '//td[2]')
        for name in comp_name[2:-2]:
            name=name.text
            stock_info["comp_name"].append(name)

    def get_current_price(self, driver):
        driver.implicitly_wait(5)
        stock_data = driver.find_elements(by=By.XPATH, value='//td')
        curr_price = driver.find_elements(by=By.XPATH, value= '//td[3]')
        for price in curr_price[2:-2]:
            price=price.text
            stock_info["current_price"].append(price)

    def get_unit_change_in_price(self, driver):
        driver.implicitly_wait(5)
        stock_data = driver.find_elements(by=By.XPATH, value='//td')
        unit_change = driver.find_elements(by=By.XPATH, value= '//td[4]')
        for change in unit_change:
            change=change.text
            stock_info["unit_day_change"].append(change)

    def get_pct_change_in_price(self, driver):
        driver.implicitly_wait(5)
        stock_data = driver.find_elements(by=By.XPATH, value='//td')
        pct_change = driver.find_elements(by=By.XPATH, value= '//td[5]')
        for pct in pct_change:
            pct=pct.text
            stock_info["pct_day_change"].append(pct)

    def page_crawler(self, driver):
        pages_link = []
        driver.implicitly_wait(5)
        page_n = driver.get("https://www.hl.co.uk/shares/stock-market-summary/ftse-250")
        page_1 = driver.get("https://www.hl.co.uk/shares/stock-market-summary/ftse-250?page=1")
        page_2 = driver.get("https://www.hl.co.uk/shares/stock-market-summary/ftse-250?page=2")
        page_3 = driver.get("https://www.hl.co.uk/shares/stock-market-summary/ftse-250?page=3")
        pages_link.append(page_n)
        pages_link.append(page_1)
        pages_link.append(page_2)
        pages_link.append(page_3)
        return pages_link

data = Scraper()

def accept_cookies(data):
    data.accept_cookies(driver)
    data.get_ftse250_table(driver)

def get_page_data(data):
    data.get_stock_epic(driver)
    data.get_comp_name(driver)
    data.get_current_price(driver)
    data.get_pct_change_in_price(driver)
    data.get_unit_change_in_price(driver)

def get_other_pages_data(data):
    for page in data.page_crawler(driver):
        driver.implicitly_wait(5)
        page = driver.find_element(by=By.XPATH, value='/html/body/main/div/div/div[3]/div/div[4]/div[1]/div/table/tbody')
        table_path_2 = driver.find_elements(by=By.XPATH, value='//tr')
        get_page_data(data)

def run_scrapper_bot():
    accept_cookies(data)
    get_page_data(data)
    get_other_pages_data(data)


if __name__ == "__main__":
    run_scrapper_bot()




