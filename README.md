## Data-Collection-Project-with-Selenium
- The project was developed to get FTSE 250 (An Index on the Uk markets) component's information from a website and store them as files on the local machine with potential use for further analytical purpose
- Selenium was adopted as the preferred scrappimg tool due to its dynamic nature and its versatility for surfing through websites easily
### Setting up the Driver
- Firefox webdriver was selected for this project, thus i had to download the geckodriver.exe file and place that in the same folder as the project.
- It is also important that the geckodriver is visible on the system variable path
- The code below shows how the driver  was set initialized for the project
```
driver_service = Service("drivers\geckodriver.exe")
driver_options = Options()
driver_options.binary_location=r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(service=driver_service, options=driver_options)
web_page = driver.get("https://www.hl.co.uk")
```
### Creating the Selenium Scrapper Bot
- OOP approach was used to create a scrapper class for this project, the class was further propagated with 8 methods (excluding the init method) with each method performing a specific function. The first job was to get pass the cookies on the website, that was handled with the accept_cookies() . Other methods were used to target and extract the certain information about each company
- The page_crawler() method was used to navigate through the pages of the FTSE250  index market. The method returns a list of webpages url that contains information about companies not available on the first page. view the code of the page_crawler method below
```
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
```
### Instantiating the SCrapper Class && Calling it Methods
- I created an instance of the scrapper class and calling it methods was done in a sequential pattern
- First a function was created that  calls the object methods  responsible for accepting cookies and navigates to the first FTSE250 index table
- The second function calls the methods that targets and extract the required information
- The third function calls the last method of the class which crawls through the url list and performs the second function for each url page it visits
- The last function on the scrapper.py script gathers this 3 functions above within it and runs the file if the condition below it equates to true.
### Storing the extracted Data
- file storedata.py handles the functions that calls the scrapper.py and stores the extracted information as a csv or json file


## Thank You!!
