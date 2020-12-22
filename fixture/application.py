from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.base_url = base_url

    def open_main_page(self):
        wd = self.wd
        if not wd.current_url.endswith("/addressbook/"):
            wd.get(self.base_url)

    def go_to_home_page(self):
        wd = self.wd
        if not wd.current_url.endswith("/addressbook/"):
            wd.find_element_by_link_text("home").click()

    def quit(self):
        wd = self.wd
        wd.quit()

    def is_not_valid(self):
        try:
            self.wd.current_url()
            return True
        except:
            return False
