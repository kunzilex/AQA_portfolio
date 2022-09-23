import random

from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators
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


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTONS).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                print(item.text)
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.element_is_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element_by_xpath(self.locators.TITLE_ITEM)
            data.append(title_item.text)
        print(data)
        return str(data).replace(' ', '').replace('doc', '').replace('.','').lower()

    def get_output_result(self):
        result_list = self.element_is_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        print(data)
        return str(data).replace(' ', '').lower()
