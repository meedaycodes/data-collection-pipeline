URL = "https://www.hl.co.uk"
COOKIES_URL = '//*[@id="acceptCookieButton"]'
SHARES_PATH = '//*[@id="nav16516"]'
MARKET_PATH = '//*[@id="markets_uk"]'
FTSE250_TABLE_PATH = '/html/body/main/div/div/div[2]/div[5]/div[1]/div[1]/table/tbody/tr[2]/td[1]/a'
TABLE_ROW_PATH ='//tr'
STOCK_DATA_PATH ='//td'
STOCK_EPIC_PATH = '//td[1]'
COMPANY_NAME_PATH = '//td[2]'
CURRENT_PRICE_PATH = '//td[3]'
UNIT_CHANGE_PATH = '//td[4]'
PCT_CHANGE_PATH = '//td[5]'
PAGES_TO_CRAWL = ["https://www.hl.co.uk/shares/stock-market-summary/ftse-250",
 "https://www.hl.co.uk/shares/stock-market-summary/ftse-250?page=1","https://www.hl.co.uk/shares/stock-market-summary/ftse-250?page=2",
 "https://www.hl.co.uk/shares/stock-market-summary/ftse-250?page=3"
]
TABLE_PATH_FOR_NEW_PAGE = '/html/body/main/div/div/div[3]/div/div[4]/div[1]/div/table/tbody'