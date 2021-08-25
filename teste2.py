from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.google.com.br/")
driver.find_element_by_name('q').send_keys("baixaki" + Keys.ENTER)
driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/h3').click()
driver.back()
driver.forward()
driver.refresh()
driver.minimize_window()

driver.quit()
