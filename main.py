from selenium import webdriver

chrome_driver_path = r"C:\Users\Chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# gets the website
driver.get("https://www.python.org")
dates = driver.find_elements_by_css_selector(".blog-widget .shrubbery time")
events = driver.find_elements_by_css_selector(".blog-widget .shrubbery li a")
events_dictionary = {}
for _ in range(len(dates)):
    events_dictionary.update(
        {_:
             {"times": dates[_].text,
              "event":events[_].text
              }
         }
    )
print(events_dictionary)
# event_dict = {key, value for (key, value) in website()}
# find_element_by_name()
# find_element_by_class_name()
# find_element_by_css_selector(".documentation-widget a")
# find_element_by_xpath('"xpath"')

driver.quit()
# driver.close() quits tab
# driver.quit() quits browser
