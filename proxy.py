from selenium import webdriver
import time
import random
import config # this is .py file containing all proxies 


## for proxies
def rand_proxy():
    proxy = random.choice(config.proxies)
    return proxy

def main():
    proxy = rand_proxy()
    print(proxy)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument(f'--proxy-server={proxy}')
    driver = webdriver.Chrome(options=chrome_options)
    try:
        resp = driver.get('https://ipinfo.io/json')
        print("response : ",resp)
    except:
        pass
    driver.quit()

for i in range(20):
    main()