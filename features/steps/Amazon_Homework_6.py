from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PRIVACY_NOTICE = (By.CSS_SELECTOR, "a[href='https://www.amazon.com/privacy']")

@given('Open Amazon T&C page')
def open_product(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_current_window(context):
        context.current_window = context.driver_window_handle
        print(context.current_window)


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice_link(context):
    context.driver.find.elements(*PRIVACY_NOTICE).click()


@when('Switch to the newly opened window')
def new_opened_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    context.driver.switch_to_window()





