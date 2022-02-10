from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = r"C:\UsersChromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2342298324&f_LF=f_AL&geoId="
           "105072130&keywords=web%20development%20intern&location=Poland")

sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(5)
email_field = driver.find_element_by_id("username")
email_field.send_keys("emai@emial.com")
password_field = driver.find_element_by_id("password")
password_field.send_keys("Helloworld")
password_field.send_keys(Keys.ENTER)

message_button = driver.find_element_by_class_name("msg-overlay-bubble-header")
message_button.click()

#Locate the apply button
time.sleep(5)
apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
apply_button.click()

#If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
phone = driver.find_element_by_class_name("fb-single-line-text__input")
if phone.text == "":
    phone.send_keys("123123123")

#Submit the application
try:
    submit_button = driver.find_element_by_css_selector("footer button")
    submit_button.click()
    next_button = driver.find_element_by_class_name('jobs-search-results__list-item')
    next_button.click()
except ElementClickInterceptedException:
    x_button = driver.find_element_by_class_name('artdeco-modal__dismiss')
    x_button.click()
    time.sleep(1)
    discard_button = driver.find_element_by_xpath('//button[@class="artdeco-button--primary"]')
    discard_button.click()