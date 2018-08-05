import time
from selenium import webdriver


driver = webdriver.Chrome('/Users/apolo.siskos/chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://app.bionic-ads.com/'); #Website. In this case https://app.bionic-ads.com/ was an example. 
time.sleep(1) # Let the user actually see something!
inputElement = driver.find_element_by_id("email")
inputElement.send_keys("not.not@not.com") #Add a valid email
time.sleep(1)
inputElement = driver.find_element_by_id("password")
inputElement.send_keys("not") #Add a valid password
time.sleep(1)
element = driver.find_element_by_xpath("//a[@id='loginSubmit']")
element.click()
time.sleep(5)
element = driver.find_element_by_xpath("//li[@class='advertiser-subnav-campaigns ']")
element.click()
time.sleep(5)
campaignKey = driver.find_element_by_id("campaigns-filter-search-master")
time.sleep(3)
campaignKey.send_keys("55289")
time.sleep(3)

from selenium.webdriver.common.keys import Keys
#driver.find_element_by_id("campaigns-filter-search-master").send_keys(keys.ENTER)

visitcampaignPage = driver.find_element_by_class_name("clickable")
time.sleep(1)
visitcampaignPage.click()
time.sleep(2)


mediaPlan = driver.find_element_by_class_name("subnav-mediaplan")
time.sleep(2)
mediaPlan.click()
time.sleep(3)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


#Total Budget
totalBudget = wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#media-grid-right > div.nxm-tr.nxm-drop.media-plan-drop.mpSummary.summary-row.no-filter > div.nxm-td.col-total-media-cost.text-right > div > span.summary.number"))).text

#Agency Comp
agencyComp = wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#media-grid-right > div.nxm-tr.nxm-drop.media-plan-drop.mpSummary.summary-row.no-filter > div.nxm-td.col-agency-compensation.text-right > div > span.summary.number"))).text

#Result (Total Budget - Agency Comp)
print(int(round(float(totalBudget.replace(",", "")))-round(float(agencyComp.replace(",", "")))))

#Start Date
startDate = wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#media-grid-right > div.nxm-tr.nxm-drop.media-plan-drop.mpSummary.summary-row.no-filter > div.nxm-td.col-flight-dates > div > div:nth-child(1) > span"))).text
print(startDate)

#End Date
endDate = wait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#media-grid-right > div.nxm-tr.nxm-drop.media-plan-drop.mpSummary.summary-row.no-filter > div.nxm-td.col-flight-dates > div > div:nth-child(2) > span"))).text
print(endDate)

time.sleep(5)

driver.quit()


