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

