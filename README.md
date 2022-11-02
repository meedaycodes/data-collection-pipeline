## Data-Collection-Project-with-Selenium
- The project was developed to get FTSE 250 (An Index on the Uk markets) component's information from a website and store them as files on the local machine with potential use for further analytical purpose
- Selenium was adopted as the preferred scrappimg tool due to its dynamic nature and its versatility for surfing through websites easily
### Setting up the Driver
- Firefox webdriver (geckodriver) was used, thus i had to download the geckodriver.exe file and place that in the same folder as the project.
- It is also important that the geckodriver is visible on the system variable path
- The code below shows how the driver  was  initialized 
```
def __init__(self):
        self.driver_service = Service("drivers\geckodriver.exe")
        self.driver_options = Options()
        self.driver_options.binary_location=r"C:\Program Files\Mozilla Firefox\firefox.exe"
        self.driver = webdriver.Firefox(service=self.driver_service, options=self.driver_options)
        web_page =self.driver.get(settings.URL)
```

### Creating the Selenium Scrapper Bot
- In  order to allow for reusability of the scrapper class, all the variables was saved in setting.py file and imported into the scrapper class file
-  the class was further propagated with 8 methods (excluding the init method) with each method performing a specific function. The first job was to get pass the cookies on the website, that was handled with the accept_cookies() . Other methods were used to target and extract certain information about each company
- The page_crawler() method was used to navigate through the pages of the FTSE250  index market. The method returns a list of webpages url that contains information about companies not available on the first page. view the code of the page_crawler method below
```
def page_crawler(self):
        pages_link = []
        self.driver.implicitly_wait(5)
        for page in settings.PAGES_TO_CRAWL:
            page = self.driver.get(page)
            pages_link.append(page)
        return pages_link
```
### Calling the Scrapper Class Methods
- I created 3 other instance methods that called some other instance methods within the class
- get_cookies(self) calls the 1st and 2nd method of the instance
- get_page_data(self) calls method from 3rd to 7th of the instance
-get_other_pages(self) calls the 8th method of the instance

### Storing the extracted Data
- file storedata.py was imported into the class file and called under the if __name__ is "__main__" condition. The result of calling the
functions within storedata.py is the creation of a csv and json file stored in the scrapped data directory


## Thank You!!
