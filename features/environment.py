from selenium import webdriver


def browser_init(context):
    """
    :param context: Behave context
    """
    context.driver = webdriver.Chrome(executable_path='/Users/user/Automation/python-selenium-automation/chromedriver')
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()

#By ID
driver.find_element(By.ID, 'ap_email')
driver.find_element(By.ID, 'auth-fpp-link-bottom')

#By XPATH
driver.find_element(By.XPATH, "//input[@class='a-input-text a-span12 auth-autofocus auth-required-field']")
driver.find_element(By.XPATH, "//input[@class='a-button-input']")

#By Xpath, contains
driver.find_element(By.XPATH, "//a[contains(@href, 'ap/forgotpassword?showRememberMe')]")

