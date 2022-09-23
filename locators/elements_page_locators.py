from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # form fields

    full_name = (By.CSS_SELECTOR, "input[id='userName']")
    email = (By.CSS_SELECTOR, "input[id='userEmail']")
    current_address = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    permanent_address = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    submit = (By.CSS_SELECTOR, "button[id='submit']")

    # created form

    created_full_name = (By.CSS_SELECTOR, "#output #name")
    created_email = (By.CSS_SELECTOR, "#output #email")
    created_current_address = (By.CSS_SELECTOR, "#output #currentAddress")
    created_permanent_address = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTONS = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[lass='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")
