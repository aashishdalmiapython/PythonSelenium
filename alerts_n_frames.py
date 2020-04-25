from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(executable_path=r"D:\Next\Automation\Drivers\geckodriver.exe")
url = "https://softwaretestingbootcamp.blogspot.com/p/automation.html"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(30)
time.sleep(10)
alert_click = driver.find_element_by_xpath("//button[@onclick='myFunction()']").click()
time.sleep(5)
driver.switch_to_alert().accept()
time.sleep(5)
#driver.quit()
driver.get("https://softwaretestingbootcamp.blogspot.com/p/automation-testing-model.html")
xpath = "/html/body/div[1]/div/div/main/div/div[1]/div/div/div/div[2]/div[2]/div/div/table/tbody/tr/td/button"
driver.find_element_by_xpath(xpath).click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div/div/main/div/div[1]/div/div/div/div[2]/div[2]/div/div/table/tbody/tr/td/div/form/div/div/button[1]").click()
time.sleep(5)
driver.quit()



