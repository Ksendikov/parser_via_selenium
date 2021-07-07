import time
import csv
from selenium import webdriver
from selenium.webdriver import ActionChains


# we re-initialize the driver in order to add headers and user agent
def __init__(self):
    options = webdriver.FirefoxOptions()
    options.add_argument('headless')
    options.add_argument('--user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0')
    self.driver = webdriver.Firefox(options=options)


# scrolling of the page
def slow_scroll_mouse(len_scroll, max_range):
    len_scroll_mouse = len_scroll
    for timer in range(0, max_range):
        browser.execute_script(f'window.scrollTo(0,{len_scroll_mouse})')
        len_scroll_mouse += len_scroll
        time.sleep(0.3)


# returns [[name-price], [...], ...] list
def create_list(table_column_1, table_column_2):
    lists_name_price = []
    for row in table_rows:
        lists_name_price.append([row.text.split()[table_column_1], row.text.split()[table_column_2]])
    return lists_name_price


# writing the obtained values to a file
def writing_table_items(lists_name_price):
    for element_name_price in lists_name_price:
        with open('data.csv', 'a') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(
                element_name_price
            )


browser = webdriver.Firefox()
browser.get('https://www.nseindia.com')
time.sleep(2)
browser.implicitly_wait(2)
browser.delete_all_cookies()

#initialize the hover and click path
market_data_hover = browser.find_element_by_xpath('//*[@class="nav-link dd-link"][contains (text(), "Market Data")]')
pre_open_market_click = browser.find_element_by_xpath('//*[@class = "nav-link"][contains (text(), "Pre-Open Market")]')

#simulate the scenario of clicking a click on an element
actions = ActionChains(browser)
actions.move_to_element(market_data_hover).move_to_element(pre_open_market_click).click().perform()
time.sleep(2)

#scroll page
slow_scroll_mouse(50, 10)

#search table rows
table_rows = browser.find_elements_by_xpath('//tr[@class = ""]')

# writing to file
writing_table_items(create_list(0, 5))
browser.delete_all_cookies()


go_home_page = browser.find_element_by_xpath('//*[@class="navbar-brand mr-auto"]').click()
time.sleep(2)

slow_scroll_mouse(50, 8)
time.sleep(3)
browser.delete_all_cookies()

go_nifty_bank = browser.find_element_by_xpath('//*[@href="#NIFTY BANK"]').click()
time.sleep(2)
browser.delete_all_cookies()

path_view_all = browser.find_element_by_xpath('//*[@id="tab4_gainers_loosers"]/div[@class="link-wrap"]/a'
                                              '[@href="/market-data/live-equity-market?symbol=NIFTY BANK"]')
browser.execute_script("arguments[0].click();", path_view_all)
time.sleep(2)

slow_scroll_mouse(50, 4)
browser.implicitly_wait(3)
time.sleep(2)


select_hover = browser.find_element_by_xpath('//*[@id="equitieStockSelect"]').click()
nifty_alpha_click = browser.find_element_by_xpath('//*[@value="NIFTY ALPHA 50"]').click()