from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.full_name).send_keys(full_name)
        self.element_is_visible(self.locators.email).send_keys(email)
        self.element_is_visible(self.locators.current_address).send_keys(current_address)
        self.element_is_visible(self.locators.permanent_address).send_keys(permanent_address)
        self.element_is_visible(self.locators.submit).click()
        return full_name, email, current_address, permanent_address

    def check_field_forms(self):
        full_name = self.element_is_present(self.locators.created_full_name).text.split(':')[1]
        email = self.element_is_present(self.locators.created_email).text.split(':')[1]
        current_address = self.element_is_present(self.locators.created_current_address).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.created_permanent_address).text.split(':')[1]
        return full_name, email, current_address, permanent_address


