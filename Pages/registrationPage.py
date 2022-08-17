from Pages.basePage import BasePage


class Registration(BasePage):
    def __int__(self, driver):
        super().__init__(driver)

    def fill_form(self, name, phone, email, country, city, username, password):
        self.key("registration locator", "name_XPATH", name)
        self.key("registration locator", "phone_XPATH", phone)
        self.key("registration locator", "email_XPATH", email)

        self.select("registration locator", "country_XPATH", country)

        self.key("registration locator", "city_XPATH", city)
        self.key("registration locator", "username_XPATH", username)
        self.key("registration locator", "password_XPATH", password)
       # self.click("registration locator", "submit_XPATH")
