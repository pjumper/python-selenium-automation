class Page:

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    #def verify_text(self, expected_text, *locator):
        #expected_text = self.driver.find_element(*locator).text
        #assert expected_text == actual_result, f'Expected {expected_text} but got {actual_result}'

    #def verify_cart(self,*locator):
        #empty_cart =