from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://github.com/login")

username_box = browser.find_element_by_id("login_field")
username_box.send_keys("naimishbhagat-wcg")
password_box = browser.find_element_by_id("password")
password_box.send_keys("New290704@")
password_box.submit()

browser.quit()
