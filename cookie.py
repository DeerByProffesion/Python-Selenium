from selenium import webdriver
from datetime import datetime, timedelta
import time
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r"C:\Users\Chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")


cookie = driver.find_element_by_id("cookie")

now = int(str(time.time()).split(".")[0])
now_2 = int(str(time.time()).split(".")[0])
running = True

while running:
    try:
        money = int(driver.find_element_by_id("money").text)
    except ValueError:
        money = int(str(money).strip(","))

    cookie.click()

    if int(str(time.time()).split(".")[0]) == now_2+1:
        now_2 =+ int(str(time.time()).split(".")[0])+1
        if money >= 123456789:
            timemachine = driver.find_element_by_id("buyTime machine")
            timemachine.click()
        elif money >= 1000000:
            portal = driver.find_element_by_id("buyPortal")
            portal.click()
        elif money >= 50000:
            alchemy = driver.find_element_by_id("buyAlchemy lab")
            alchemy.click()
        elif money >= 7000:
            shipment = driver.find_element_by_id("buyShipment")
            shipment.click()
        elif money >= 2000:
            mine = driver.find_element_by_id("buyMine")
            mine.click()
        elif money >= 500:
            factory = driver.find_element_by_id("buyFactory")
            factory.click()
        elif money >= 100:
            grandma = driver.find_element_by_id("buyGrandma")
            grandma.click()
        elif money >= 15:
            cursor = driver.find_element_by_id("buyCursor")
            cursor.click()
    if int(str(time.time()).split(".")[0]) > now+50:
        running = False