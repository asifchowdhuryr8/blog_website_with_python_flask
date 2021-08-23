# start server from vs code and run this file from another vs code
from selenium import webdriver

chrome_driver_path = "D:/Chrome Web Driver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get("http://192.168.1.199:5000/register")


name = driver.find_element_by_name("name")
name.send_keys("My_Name")

email = driver.find_element_by_name("email")
email.send_keys("asifchowdhuryrafi@yahoo.com")

password = driver.find_element_by_name("password")
password.send_keys("My_Password_123")

add = driver.find_element_by_id("register")
add.click()


# driver.close()
