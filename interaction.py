from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                            'like Gecko) Chrome/119.0.0.0 Safari/537.36"')
chrome_options.add_argument('Accept-Language="en-US,en;q=0.9"')
chrome_options.add_argument('sec-fetch-site="cross-site"')
chrome_options.add_argument('sec-fetch-mode="navigate"')
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://secure-retreat-92358.herokuapp.com/")

# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# article_count.click()

# all_portals = driver.find_element(By.CSS_SELECTOR, value="#vector-page-tools-dropdown-checkbox")
# all_portals.click()

# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Rizal")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Safril")

email = driver.find_element(By.NAME, value="email")
email.send_keys("rzmobiledev@gmail.com")

submit_btn = driver.find_element(By.TAG_NAME, value="button")
submit_btn.send_keys(Keys.ENTER)

# driver.quit()