
from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.full_name).send_keys('cjehjc')
        self.element_is_visible(self.locators.email).send_keys('wbcjh@jcw.com')
        self.element_is_visible(self.locators.current_address).send_keys('ekjcklwe')
        self.element_is_visible(self.locators.permanent_address).send_keys('dtd')
        self.element_is_visible(self.locators.submit).click()

    def check_field_forms(self):
        full_name = self.element_is_present(self.locators.created_full_name).text.split(':')[1]
        email = self.element_is_present(self.locators.created_email).text.split(':')[1]
        current_address = self.element_is_present(self.locators.created_current_address).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.created_permanent_address).text.split(':')[1]
        return full_name, email, current_address, permanent_address

