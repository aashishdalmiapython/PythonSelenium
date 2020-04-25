from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(executable_path=r"D:\Next\Automation\Drivers\geckodriver.exe")
url = "http://demo.automationtesting.in/Register.html"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(30)

# checkboxes
checkbox1_state = driver.find_element_by_xpath("//input[@value='Cricket']").is_selected()
if checkbox1_state is True:
    print("Cricket checkbox is selected")
else:
    if checkbox1_state is False:
        driver.find_element_by_xpath("//input[@value='Cricket']").click()
        print("Selenium code changes the Cricket checkbox selection to checked")
    else:
        print("Something went wrong")

# links
count = driver.find_elements(By.TAG_NAME,"a")
print("No of links on page =", len(count))
time.sleep(4)
for link in count:
    if link.text == "WebTable":
        print(link.text, "is available")
        #driver.find_element_by_link_text(link.text).click()
        driver.find_element_by_partial_link_text(link.text).click()
        print("link clicked")
        break
driver.quit()














