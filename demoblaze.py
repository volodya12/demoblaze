from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import pytest

service = Service(executable_path="C:\\Users\\volod\\Downloads\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.demoblaze.com")
driver.maximize_window()

driver.implicitly_wait(5)

# Sign up
def test_signUp(getData):
    driver.find_element_by_xpath("//div[@id='navbarExample']//li[8]//a").click()
    driver.find_element_by_xpath("//input[@id='sign-username']").send_keys(getData["randUser"])
    driver.find_element_by_xpath("//input[@id='sign-password']").send_keys(getData["randPass"])
    driver.find_element_by_xpath("//div[@id='signInModal']/div/div/div[3]/button[2]").click()

    # Accept Alert
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    driver.switch_to.alert.accept()

# Log in
def test_logIn(getData): 
    driver.find_element_by_xpath("//a[@id='login2']").click()
    driver.find_element_by_xpath("//input[@id='loginusername']").send_keys(getData["randUser"])
    driver.find_element_by_xpath("//input[@id='loginpassword']").send_keys(getData["randPass"])
    driver.find_element_by_xpath("//button[contains(text(),'Log in')]").click()

@pytest.fixture(params=[
{
"randUser":"jungle", 
"randPass":"loki123",
"fieldName":"jungle",
"fieldCountry":"USA",
"fieldCity":"Tacoma",
"fieldCard":"123456789",
"fieldMonth":"January",
"fieldYear":"2022"
},

{
"randUser":"jeep321", 
"randPass":"Kyle123",
"fieldName":"jeep321",
"fieldCountry":"USA",
"fieldCity":"Tacoma",
"fieldCard":"123456789",
"fieldMonth":"January",
"fieldYear":"2022"
}
])

# Execute Data Set
def getData(request):
    return request.param

# Adding 1st product into shopping cart
driver.find_element_by_xpath("//a[contains(text(),'Samsung galaxy s7')]").click()

# Add to Cart
driver.find_element_by_class_name("btn-success").click()

# Accept Alert
WebDriverWait(driver, 5).until(EC.alert_is_present())
driver.switch_to.alert.accept()

# Back page
driver.back()

# Adding 2nd product into shopping cart
driver.find_element_by_xpath("//a[contains(text(), 'Nexus 6')]").click()

# Add to Cart
driver.find_element_by_class_name("btn-success").click()

# Validate alert text on pop-up
alert = driver.switch_to.alert
alertText = alert.text
assert "Product added" in alertText

# Accept Alert
WebDriverWait(driver, 5).until(EC.alert_is_present())
driver.switch_to.alert.accept()

# Click on Cart
driver.find_element_by_id("cartur").click()

# Verify Cart have 2 items
count = len(driver.find_elements_by_xpath("//tbody[@id='tbodyid']"))
assert count == 2

# Place Order
driver.find_element_by_class_name("btn-success").click()

# Fill the form for order
def test_form(getData):
    driver.find_element_by_id("name").send_keys(getData["fieldName"])
    driver.find_element_by_id("country").send_keys(getData["fieldCountry"])
    driver.find_element_by_id("city").send_keys(getData["fieldCity"])
    driver.find_element_by_id("card").send_keys(getData["fieldCard"])
    driver.find_element_by_id("month").send_keys(getData["fieldMonth"])
    driver.find_element_by_id("year").send_keys(getData["fieldYear"])

    # Click Cancel
    driver.find_element_by_class_name("btn-secondary").click()

def getData(request):
    return request.param

# Delete Items in Cart
driver.find_element_by_xpath("//a[text()='Delete']").click()
driver.find_element_by_xpath("//a[text()='Delete']").click()

# Log out
driver.find_element_by_xpath("//div[@id='navbarExample']//li[6]//a").click()

# Log in Again
driver.find_element_by_xpath("//div[@id='navbarExample']//li[8]//a").click()
driver.find_element_by_id("loginusername").send_keys("jeep321")
driver.find_element_by_id("loginpassword").send_keys("Kyle123")
driver.find_element_by_class_name("btn-primary").click()

# Click on Cart
driver.find_element_by_id("cartur").click()

# Verify Cart is empty
count = len(driver.find_elements_by_xpath("//tbody[@id='tbodyid']"))
assert count == 0

# Go Back 
driver.back()

# Add to Cart
driver.find_element_by_class_name("btn-success").click()

# Validate alert text on pop-up
alert = driver.switch_to.alert
alertText = alert.text
assert "Product added" in alertText

# Accept Alert
WebDriverWait(driver, 5).until(EC.alert_is_present())
driver.switch_to.alert.accept()

# Click on Cart
driver.find_element_by_id("cartur").click()

# Delete Items in Cart
driver.find_element_by_xpath("//a[text()='Delete']").click()

# Verify Cart is empty
count = len(driver.find_elements_by_xpath("//tbody[@id='tbodyid']"))
assert count == 0

# Log out
driver.find_element_by_xpath("//div[@id='navbarExample']//li[6]//a").click() 






