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

### Testing the Scraper
- Using the unittest module in the scrapper_test.py file i tested four public methods of the scrapper class, one of such methods is provided below which tests that the accept_cookies button is found through the url provided by settings.COOKIES_URL
```@patch('selenium.webdriver.remote.webdriver.WebDriver.find_element')
    def test_accept_cookies(self,
        mock_find_element:Mock):
        self.obj_scraper.accept_cookies()
        mock_find_element.assert_called_once_with(by='xpath', value= settings.COOKIES_URL)
```
### Containerising Using Docker
- following the test i created a docker file to produce a docker image that was thereafter pushed to the docker hub. The image was produced with the following steps
```
FROM python:3.9


# Update the system and install firefox
RUN apt-get update 
RUN apt -y upgrade 
RUN apt-get install -y firefox-esr

# get the latest release version of firefox 
RUN latest_release=$(curl -sS https://api.github.com/repos/mozilla/geckodriver/releases/latest \
    | grep tag_name | sed -E 's/.*"([^"]+)".*/\1/') && \
    # Download the latest release of geckodriver
    wget https://github.com/mozilla/geckodriver/releases/download/$latest_release/geckodriver-$latest_release-linux32.tar.gz \
    # extract the geckodriver
    && tar -xvzf geckodriver* \
    # add executable permissions to the driver
    && chmod +x geckodriver \
    # Move gecko driver in the system path
    && mv geckodriver /usr/local/bin

COPY . . 

RUN pip install --upgrade pip

# install dependencies
RUN pip install -r requirements.txt

CMD ["python", "scrapper.py"]
```
### CI/CD Pipeline for the Docker Image
- I set up the relevant GitHub secrets (on GitHub) that contains the credentials required to push to the Dockerhub account. I then created a GitHub action (workflow) to build the docker image and push it to Dockerhub account everytime a Git push action takes place (trigggered on a "push" to the "main" branch of the repository).

## Thank You!!
