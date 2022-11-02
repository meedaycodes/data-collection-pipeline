from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from storedata import store_data_as_csv, store_data_as_json
import settings

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
        web_page =self.driver.get(settings.URL)
        
    def accept_cookies(self):
        '''
        This function presses on the cookies button
        
        Arguments : None
        
        Returns: A page without the cookies pop up window
        '''
        self.driver.implicitly_wait(2)
        cookies_path = self.driver.find_element(by= By.XPATH, value= settings.COOKIES_URL)
        cookies_path.click()

    def get_ftse250_table(self):
        '''
        This function navigates to the first FTSE250 link on the first page

        Arguments: None

        Returns:  FTSE250 table of the first page
        '''
        self.driver.implicitly_wait(5)
        shares_path = self.driver.find_element(by=By.XPATH, value=settings.SHARES_PATH).click()
        market_path = self.driver.find_element(by=By.XPATH, value=settings.MARKET_PATH)
        ftse_250_path = self.driver.find_element(by=By.XPATH, value=settings.FTSE250_TABLE_PATH).click()
        table_path= self.driver.find_elements(by=By.XPATH, value=settings.TABLE_ROW_PATH)

    def get_stock_epic(self):
        '''
        This function gets the epic or acronym of each company on the FTSE250
        
        Arguments: None
        
        Returns: Gets each company's epic and appends it to the "stock_code" of stock_info dictionary
        '''
        self.driver.implicitly_wait(5)
        stock_data = self.driver.find_elements(by=By.XPATH, value=settings.STOCK_DATA_PATH)
        epic = self.driver.find_elements(by=By.XPATH, value=settings.STOCK_EPIC_PATH)
        for info in epic[4:-4]:
            info=info.text
            stock_info["stock_code"].append(info)

    def get_comp_name(self):
        '''
        This function gets the name of each company on the FTSE250
        
        Arguments: None
        
        Returns: Gets each company's name and appends it to the "comp_name" of stock_info dictionary
        '''
        self.driver.implicitly_wait(5)
        stock_data = self.driver.find_elements(by=By.XPATH, value=settings.STOCK_DATA_PATH)
        comp_name = self.driver.find_elements(by=By.XPATH, value=settings.COMPANY_NAME_PATH)
        for name in comp_name[2:-2]:
            name=name.text
            stock_info["comp_name"].append(name)

    def get_current_price(self):
        '''
        This function gets the current stock price of each company on the FTSE250
        
        Arguments: None
        
        Returns: Gets each company's stock price appends it to the "current_price" list of stock_info dictionary
        '''
        self.driver.implicitly_wait(5)
        stock_data = self.driver.find_elements(by=By.XPATH, value=settings.STOCK_DATA_PATH)
        curr_price = self.driver.find_elements(by=By.XPATH, value= settings.CURRENT_PRICE_PATH)
        for price in curr_price[2:-2]:
            price=price.text
            stock_info["current_price"].append(price)

    def get_unit_change_in_price(self):
        '''
        This function gets unit change in stock price of each company on the FTSE250
        
        Arguments: None
        
        Returns: Gets each stock unit price change and appends it to the "unit_day_change" of stock_info dictionary
        '''
        self.driver.implicitly_wait(5)
        stock_data = self.driver.find_elements(by=By.XPATH, value=settings.STOCK_DATA_PATH)
        unit_change = self.driver.find_elements(by=By.XPATH, value=settings.UNIT_CHANGE_PATH)
        for change in unit_change:
            change=change.text
            stock_info["unit_day_change"].append(change)

    def get_pct_change_in_price(self):
        '''
        This function gets the percentage change in stock price of each company on the FTSE250

        Arguments: None
        Returns: Gets each price change as a percentage and appends it to "pct_day_change" list of stock_info dictionary
        
        '''
        self.driver.implicitly_wait(5)
        stock_data = self.driver.find_elements(by=By.XPATH, value=settings.STOCK_DATA_PATH)
        pct_change = self.driver.find_elements(by=By.XPATH, value= settings.PCT_CHANGE_PATH)
        for pct in pct_change:
            pct=pct.text
            stock_info["pct_day_change"].append(pct)

    def page_crawler(self):
        '''
        This function creates a list containing stock information not available in the first page

        Arguments: None

        Returns: It returns the  list containing webpages that provides information on other company not available on the first page 
        '''
        pages_link = []
        self.driver.implicitly_wait(5)
        for page in settings.PAGES_TO_CRAWL:
            page = self.driver.get(page)
            pages_link.append(page)
        return pages_link

    def get_cookies(self):
        '''
        Description: Calls the first 2 methods of the scraper class (accept_cookies && get_ftse250_table)
        
        Arguments: None

        Returns: Navigates to the ftse250 table on gthe first page
        
        '''
        self.accept_cookies()
        self.get_ftse250_table()

    def get_page_data(self):
        '''
        Description: Calls methos 3 to 7 of Scrapper class, navigates the first page and extract the data for each company 
        Arguments: None
        
        Returns: An incomplete stock_info dictionary with stock data of derived from only the first page
        '''
        self.get_stock_epic()
        self.get_comp_name()
        self.get_current_price()
        self.get_pct_change_in_price()
        self.get_unit_change_in_price()

    def get_other_pages(self):
        '''
        Description: Serves as a crawler to get stocks information from pages other than the first page
        Arguments: None
        Returns: A complete stock_info dictionary with stock data from the rest of the webpages appended  to the relevant list
        '''
        for page in self.page_crawler():
            self.driver.implicitly_wait(5)
            page = self.driver.find_element(by=By.XPATH, value=settings.TABLE_PATH_FOR_NEW_PAGE)
            table_path_2 = self.driver.find_elements(by=By.XPATH, value=settings.TABLE_ROW_PATH)
            self.get_page_data()

data = Scraper()

if __name__ == "__main__":
    data.get_cookies()
    data.get_page_data()
    data.get_other_pages()
    store_data_as_json(stock_info)
    store_data_as_csv(stock_info)




