from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def delete_cache(driver):
	driver.execute_script("window.open('');")
	time.sleep(2)
	driver.switch_to.window(driver.window_handles[-1])
	time.sleep(2)
	driver.get('chrome://settings/clearBrowserData')
	time.sleep(2)
	actions = ActionChains(driver) 
	actions.send_keys(Keys.TAB * 3 + Keys.DOWN * 3) # send right combination
	actions.perform()
	time.sleep(2)
	actions = ActionChains(driver) 
	actions.send_keys(Keys.TAB * 7 + Keys.ENTER) # confirm
	actions.perform()
	time.sleep(2) # wait some time to finish
	driver.close() # close this tab
	driver.switch_to.window(driver.window_handles[0]) # switch back

delete_cache()