from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from settings import URL

stock_info = {"stock_code":[], "comp_name":[],"current_price":[],
 "unit_day_change":[], "pct_day_change":[]}





class Scraper:
    '''
    This class represents a scrapper 
    
    Attributes: None

    '''
    def __init__(self):

        self.driver_service = Service("drivers\geckodriver.exe")
        self.driver_options = Options()
        self.driver_options.binary_location=r"C:\Program Files\Mozilla Firefox\firefox.exe"
        self.driver = webdriver.Firefox(service=self.driver_service, options=self.driver_options)
        web_page =self.driver.get(URL)
        
    def accept_cookies(self):
        '''
        This function presses on the cookies button
        
        Arguments : driver
        
        Returns: A page without the cookies pop up window
        '''
        self.driver.implicitly_wait(2)
        cookies_path = self.driver.find_element(by= By.XPATH, value='//*[@id="acceptCookieButton"]')
        cookies_path.click()

    def get_ftse250_table(self):
        '''
        This function navigates to the first FTSE250 link on the first page

        Arguments: self.driver

        Returns:  FTSE250 table of the first page
        '''
        self.driver.implicitly_wait(5)
        shares_path = self.driver.find_element(by=By.XPATH, value='//*[@id="nav16516"]').click()
        market_path = self.driver.find_element(by=By.XPATH, value='//*[@id="markets_uk"]')
        ftse_250_path = self.driver.find_element(by=By.XPATH, value='/html/body/main/div/div/div[2]/div[5]/div[1]/div[1]/table/tbody/tr[2]/td[1]/a').click()
        table_path= self.driver.find_elements(by=By.XPATH, value='//tr')

    def get_stock_epic(self):
        '''
        This function gets the epic or acronym of each company on the FTSE250
        
        Arguments: self.driver
        
        Returns: 
        '''
        self.driver.implicitly_wait(5)
        stock_data = self.driver.find_elements(by=By.XPATH, value='//td')
        epic = self.driver.find_elements(by=By.XPATH, value= '//td[1]')
        for info in epic[4:-4]:
            info=info.text
            stock_info["stock_code"].append(info)

    def get_comp_name(self):
        self.driver.implicitly_wait(5)
        stock_data = self.driver.find_elements(by=By.XPATH, value='//td')
        comp_name = self.driver.find_elements(by=By.XPATH, value= '//td[2]')
        for name in comp_name[2:-2]:
            name=name.text
            stock_info["comp_name"].append(name)

    def get_current_price(self):
        self.driver.implicitly_wait(5)
        stock_data = self.driver.find_elements(by=By.XPATH, value='//td')
        curr_price = self.driver.find_elements(by=By.XPATH, value= '//td[3]')
        for price in curr_price[2:-2]:
            price=price.text
            stock_info["current_price"].append(price)

    def get_unit_change_in_price(self):
        self.driver.implicitly_wait(5)
        stock_data = self.driver.find_elements(by=By.XPATH, value='//td')
        unit_change = self.driver.find_elements(by=By.XPATH, value= '//td[4]')
        for change in unit_change:
            change=change.text
            stock_info["unit_day_change"].append(change)

    def get_pct_change_in_price(self):
        self.driver.implicitly_wait(5)
        stock_data = self.driver.find_elements(by=By.XPATH, value='//td')
        pct_change = self.driver.find_elements(by=By.XPATH, value= '//td[5]')
        for pct in pct_change:
            pct=pct.text
            stock_info["pct_day_change"].append(pct)

    def page_crawler(self):
        pages_link = []
        self.driver.implicitly_wait(5)
        page_n = self.driver.get("https://www.hl.co.uk/shares/stock-market-summary/ftse-250")
        page_1 = self.driver.get("https://www.hl.co.uk/shares/stock-market-summary/ftse-250?page=1")
        page_2 = self.driver.get("https://www.hl.co.uk/shares/stock-market-summary/ftse-250?page=2")
        page_3 = self.driver.get("https://www.hl.co.uk/shares/stock-market-summary/ftse-250?page=3")
        pages_link.append(page_n)
        pages_link.append(page_1)
        pages_link.append(page_2)
        pages_link.append(page_3)
        return pages_link


   # @classmethod
    def get_cookies(self):
        self.accept_cookies()
        self.get_ftse250_table()

data = Scraper()
data.get_cookies()


# def get_page_data(data):
#     data.get_stock_epic(data.driver)
#     data.get_comp_name(data.driver)
#     data.get_current_price(data.driver)
#     data.get_pct_change_in_price(data.driver)
#     data.get_unit_change_in_price(data.driver)

# def get_other_pages_data(data):
#     for page in data.page_crawler(data.driver):
#         data.driver.implicitly_wait(5)
#         page = data.driver.find_element(by=By.XPATH, value='/html/body/main/div/div/div[3]/div/div[4]/div[1]/div/table/tbody')
#         table_path_2 = data.driver.find_elements(by=By.XPATH, value='//tr')
#         get_page_data(data)

# def run_scrapper_bot():
#     get_cookies()
#     get_page_data(data)
#     get_other_pages_data(data)


if __name__ == "__main__":
    run_scrapper_bot()




