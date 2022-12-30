from selenium import webdriver

driver = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
driver = webdriver.Chrome(options=chrome_options)
driver.execute_cdp_cmd("Network.setCacheDisabled", {"cacheDisabled":True})