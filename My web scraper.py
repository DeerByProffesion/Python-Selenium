from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r"C:\Users\Chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com")

# value = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')

# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()
First_name = driver.find_element_by_name("fName")
First_name.send_keys("Hello")
Last_name = driver.find_element_by_name("lName")
Last_name.send_keys("World")
Email = driver.find_element_by_name("email")
Email.send_keys("Hello123123123123123123123123@World.com")
sign_up = driver.find_element_by_class_name("btn")
sign_up.send_keys(Keys.ENTER)