from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Replace these with your Facebook login credentials
username = "YourFacebookEmail@example.com"
password = "YourFacebookPassword"

# Create a new ChromeDriver instance
driver = webdriver.Chrome()

# Open Facebook
driver.get("https://www.facebook.com/login.php")

# Find the username and password fields and login
username_field = driver.find_element("id", "email")
password_field = driver.find_element("id", "pass")

username_field.send_keys(username)
password_field.send_keys(password)

password_field.send_keys(Keys.RETURN)
time.sleep(5)
driver.get("https://www.facebook.com/profile.php")
time.sleep(10)
driver.quit()
