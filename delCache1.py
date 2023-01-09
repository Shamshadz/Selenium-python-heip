

def clearCache():
    driver.get("chrome://settings/clearBrowserData")
    try:
        wait.until(EC.visibility_of_element_located((By.ID, "clearBrowsingDataConfirm"))).click()
    except:
        driver.find_element(By.XPATH, "/html/body/main-view//section/settings-ui//div[2]/settings-main//settings-basic-page//div[1]/settings-section[3]/settings-privacy-page//settings-clear-browsing-data-dialog//cr-dialog[1]/div[4]/cr-button[2]").click()
    sleep(4)