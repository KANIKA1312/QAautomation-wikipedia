# 1. Using Selenium WebDriver, open the web browser.

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime
from time import sleep

# s = Service(executable_path='D:\PythonCourse\chromedriver.exe')
# driver = webdriver.Chrome(service=s)

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

# ----------------variables----------------
wiki_url = 'https://en.wikipedia.org/wiki/Main_Page'
wiki_title = 'Wikipedia, the free encyclopedia'

# 2. Maximize the browser window.

driver.maximize_window()


# 3. Navigate to https://en.wikipedia.org/ (Links to an external site.) web URL

def setUp():
    driver.implicitly_wait(20)
    print('')
    print('-----------------Launch Wikipedia-------------')
    print('')
    driver.get('https://en.wikipedia.org')

    # 4. Check URL and title are as expected.

    assert driver.find_element(By.ID, 'Welcome_to_Wikipedia').is_displayed()
    assert driver.current_url == wiki_url
    assert driver.title == wiki_title
    print('Wikipedia Launched Successfully!!')
    print('')
    print('This is the Wikipedia URL : ', driver.current_url)
    print('This is the Wikipedia title : ', driver.title)
    print('')
    sleep(1)


# 5. In a search field, find Python (programming language) and click on it.
def search_python_programminglanguage():
    driver.find_element(By.ID, 'searchInput').click()
    sleep(0.25)
    driver.find_element(By.ID, 'searchInput').send_keys('Python (programming language)')
    sleep(0.75)
    # driver.find_element(By.XPATH, '//span[contains(.,"Python (programming language)")]').click()
    # sleep(0.75)  #Second Method

    driver.find_element(By.ID, 'searchInput').send_keys(Keys.ARROW_DOWN)
    sleep(0.75)
    driver.find_element(By.ID, 'searchInput').send_keys(Keys.ARROW_DOWN)
    sleep(0.75)
    driver.find_element(By.ID, 'searchInput').send_keys(Keys.ENTER)
    sleep(0.25)

    # 6. Check that the title Python (programming language) is displayed.

    assert driver.find_element(By.ID, 'firstHeading').is_displayed()

    print('This is the Python (programming language) URL : ', driver.current_url)
    print('This is the Python (programming language) title : ', driver.title)
    print('')

    # 7. Click by the Wikipedia main image (logo) and close the browser.

    driver.find_element(By.CLASS_NAME, 'mw-wiki-logo').click()
    sleep(0.75)
    print('***********Back on Home Page****************')
    print('')


def tearDown():
    if driver is not None:
        print('-----------------~~~~~~-------------------')
        print('test is Complete at : ', datetime.datetime.now())
        sleep(2)
        driver.close()
        driver.quit()


setUp()
search_python_programminglanguage()
tearDown()
