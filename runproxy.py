from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("log-level=3")
chrome_options.add_argument("--headless")


def get_proxies(co=chrome_options):
    driver = webdriver.Chrome(options=co)
    driver.get("https://free-proxy-list.net/")

    PROXIES = []
    ips = driver.find_elements(By.XPATH,"(//tbody)[1]/tr/td[1]")
    ports = driver.find_elements(By.XPATH,"(//tbody)[1]/tr/td[2]")
    https = driver.find_elements(By.XPATH,"(//tbody)[1]/tr/td[7]")
    # googles = driver.find_elements(By.XPATH,"(//tbody)[1]/tr/td[6]")

    for ip,port,http in zip(ips,ports,https):
        if http.text == "yes":
            PROXIES.append(ip.text+":"+port.text)
            print(ip.text+":"+port.text)

    driver.close()
    return PROXIES


ALL_PROXIES = get_proxies()

def proxy_driver(PROXIES, co=chrome_options):

    if len(PROXIES) < 1:
        print("--- Proxies used up (%s)" % len(PROXIES))
        PROXIES = get_proxies()

    pxy = PROXIES[-1]

    proxy = pxy
    print(proxy)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # chrome_options.add_argument(f'--proxy-server={proxy}')
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(120)


    return driver


# --- YOU ONLY NEED TO CARE FROM THIS LINE ---
# creating new driver to use proxy
pd = proxy_driver(ALL_PROXIES)

# code must be in a while loop with a try to keep trying with different proxies
running = True

while running:
    try:
        # mycodehere()
        pass
        # getSearch(url)
        # condition_met = getData(lst)    #condition_met = []
        # print(condition_met)

        # if statement to terminate loop if code working properly
        # # you need to modify condition_met
        # if len(condition_met):
        #     print("condition_met###################################")
        #     running = False
        # elif len(condition_met)==0:
        #     print("proxy fail or recaptcha   &&&&&&&&&&&&&&&&&&&&&&&&&&")
        #     raise Exception

        # you
    except:
        print("new proxy**************************************")
        new = ALL_PROXIES.pop()

        # reassign driver if fail to switch proxy
        pd = proxy_driver(ALL_PROXIES)
        print("--- Switched proxy to: %s" % new)
        time.sleep(1)
