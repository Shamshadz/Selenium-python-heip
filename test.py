from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
#proxy server definition
py = "190.61.88.147:8080"
#configure ChromeOptions class
chrome_options = webdriver.ChromeOptions()
#proxy parameter to options
chrome_options.add_argument('--proxy-server=%s' % py)
#options to Chrome()
driver = webdriver.Chrome(chrome_options= chrome_options)
driver.implicitly_wait(0.6)
driver.get("https://www.tutorialspoint.com/index.htm")
time.sleep(10)