from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='/Users/user/Automation/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/')

driver.find_element(By.XPATH, "//span[text()='& Orders' and @class='nav-line-2']").click()

# Verify the Sign In Header
expected_text = "Sign in"
actual_text = driver.find_element(By.XPATH, "//h1[contains(text(), 'Sign in')]").text
assert expected_text == actual_text, f"Expected header to be {expected_text} but got  {actual_text}"


# Verify Email input field
email = driver.find_element(By.XPATH, "//input[@id='ap_email']")
assert email, f"Email field is not available"
pass

