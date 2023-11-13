from selenium import webdriver
from selenium.webdriver.common.by import By

# keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                            'like Gecko) Chrome/119.0.0.0 Safari/537.36"')
chrome_options.add_argument('Accept-Language="en-US,en;q=0.9"')
chrome_options.add_argument('sec-fetch-site="cross-site"')
chrome_options.add_argument('sec-fetch-mode="navigate"')
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {n: {"time": event_times[n].text, "name": event_names[n].text} for n in range(len(event_times))}

print(events)

driver.quit()