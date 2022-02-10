from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = r"C:\Users\Chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.speedtest.net/pl")

time.sleep(2)
consent = driver.find_element_by_xpath('//*[@id="_evidon-banner-acceptbutton"]')
consent.click()
time.sleep(2)
click_start = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                           'div[1]/a/span[4]')
click_start.click()
time.sleep(60)
download_data = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                             'div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
download_data_text = download_data.text
upload_data = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                           'div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
upload_data_text = upload_data.text
print(download_data_text)
print(upload_data_text)

driver.get("https://twitter.com/home")

time.sleep(2)
login_email = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form'
                                           '/div/div[1]/label/div/div[2]/div/input')
login_email.send_keys("email@email.com")
login_password = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]'
                                              '/form/div/div[2]/label/div/div[2]/div/input')
login_password.send_keys("Helloworld")
login = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div'
                                     '/div[3]/div/div/span/span')
login.click()
time.sleep(2)
tweet = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/'
                                     'div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/'
                                     'div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
tweet.send_keys(f"Hello Internet prowider! my internet download is {download_data_text} and upload is {upload_data_text} do something boi")
send_tweet = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/'
                                          'div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div'
                                          '[2]/div[3]/div/span/span')
send_tweet.click()