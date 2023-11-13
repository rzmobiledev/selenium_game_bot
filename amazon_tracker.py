from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                            'like Gecko) Chrome/119.0.0.0 Safari/537.36"')
chrome_options.add_argument('Accept-Language="en-US,en;q=0.9"')
chrome_options.add_argument('sec-fetch-site="cross-site"')
chrome_options.add_argument('sec-fetch-mode="navigate"')
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(chrome_options)
driver.get(url="https://www.amazon.com/GAMEPOWER-Headset-Virtual-Surround-Speaker/dp/B09L8BKSSB/ref=sr_1_2?_encoding=UTF8&content-id=amzn1.sym.12129333-2117-4490-9c17-6d31baf0582a&keywords=gaming%2Bheadsets&pd_rd_r=0851a698-66bb-4200-ab0f-70f405d7ab84&pd_rd_w=7KcLo&pd_rd_wg=dFIvg&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=PNSXM70JFGDGHB51V5YD&qid=1699842544&sr=8-2&th=1")

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
print(f"The price is {price_dollar}.{price_cents}")

# driver.close()
driver.quit()