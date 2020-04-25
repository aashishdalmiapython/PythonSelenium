# Packages
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox(executable_path=r"D:\Next\Automation\Drivers\geckodriver.exe")
driver.maximize_window()

# Methods
driver.get(url="http://newtours.demoaut.com/mercurysignon.php")

# implicit wait
driver.implicitly_wait(30)

# Explicit wait  1
wait = WebDriverWait(driver,30)
wait.until(EC.title_is(("Sign-on: Mercury Tours")))

print(driver.title)
print(driver.current_url)
#time.sleep(10)
username=driver.find_element_by_name("userName")
print("Username is present", username.is_displayed())
print("Username is editbale",username.is_enabled())
password=driver.find_element_by_name("password")
print("Password is Present",password.is_displayed())
print("Password is editable",password.is_enabled())
driver.find_element_by_name("userName").send_keys("abctest")
driver.find_element_by_name("password").send_keys("abctest")
driver.find_element_by_name("login").click()
#time.sleep(20)

# Explicit wait  2 (with if condition)
wait.until(EC.presence_of_element_located((By.NAME,"tripType")))

round_trip = driver.find_element_by_xpath("//input[@value='roundtrip']").is_selected()
if (round_trip==True):
    print("Round Trip is", round_trip)
driver.find_element_by_xpath("//input[@value='oneway']").click()
time.sleep(3)

# Explicit wait  3 (with for loop)
radio_locators = ["roundtrip","oneway"]
for r in range(len(radio_locators)):
    locator_presence = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@value='" + radio_locators[r] + "']")))
    value = driver.find_element_by_xpath("//input[@value='" + radio_locators[r] + "']").is_selected()
    if (value == True):
        print (radio_locators[r],  "is selected")
    else:
        print (radio_locators[r],  "is not selected")

# Handle Dropdowns 1
time.sleep(3)
departing_dd_field = Select(driver.find_element_by_name("fromPort"))
departing_dd_field.select_by_index(3)
time.sleep(3)

# Handle Dropdowns 2
on_dd_field = Select(driver.find_element_by_name("fromMonth"))
on_dd_field.select_by_value("2")
time.sleep(3)

# Handle Dropdowns 3
arriving_dd_field =Select(driver.find_element_by_name("toPort"))
arriving_dd_field.select_by_visible_text("Paris")
time.sleep(3)

print(driver.title)
print(driver.current_url)

driver.quit()
