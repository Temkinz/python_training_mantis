class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_main_page()
        # fill the form
        self.change_field_value("username", username)
        self.change_field_value("password", password)
        # click login button
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def change_field_value(self, field, text):
        wd = self.app.wd
        wd.find_element_by_name(field).click()
        wd.find_element_by_name(field).clear()
        wd.find_element_by_name(field).send_keys(text)

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        wd.implicitly_wait(1)
        wd.find_element_by_name("username")

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in_as_username(self, username):
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("td.login-info-left span").text

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as_username(username):
                return
            else:
                self.logout()
        self.login(username, password)
