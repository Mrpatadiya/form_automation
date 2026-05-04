from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/text-box"

    name_input = (By.ID, "userName")
    email_input = (By.ID, "userEmail")
    current_address = (By.ID, "currentAddress")
    submit_button = (By.ID, "submit")

    output_name = (By.ID, "name")
    output_email = (By.ID, "email")

    def open(self):
        self.driver.get(self.url)

    def fill_form(self, name, email, address):
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.visibility_of_element_located(self.name_input)).send_keys(name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.current_address).send_keys(address)

    def submit_form(self):
        self.driver.find_element(*self.submit_button).click()

    def get_output_name(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.visibility_of_element_located(self.output_name)).text

    def get_output_email(self):
        return self.driver.find_element(*self.output_email).text

    def is_email_invalid(self):
        element = self.driver.find_element(*self.email_input)
        return "field-error" in element.get_attribute("class")