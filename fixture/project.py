from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            wd.get("http://localhost/mantisbt/manage_proj_page.php")

    def get_project_list(self):
        wd = self.app.wd
        self.open_project_page()
        self.project_cache = []
        for element in wd.find_elements_by_xpath("//td/a[contains(@href,'manage_proj_edit_page.php?project_id=')]"):
            text = element.text
            id = element.get_attribute("href").replace(
                'http://localhost/mantisbt/manage_proj_edit_page.php?project_id=', '')
            self.project_cache.append(Project(id=id, name=text))
        return list(self.project_cache)

    def get_project_list_new(self):
        wd = self.app.wd
        self.open_project_page()
        self.project_cache = []
        for element in wd.find_elements_by_xpath("//td/a[contains(@href,'manage_proj_edit_page.php?project_id=')]"):
            text = element.text
            id = element.get_attribute("href").replace(
                'https://localhost/mantisbt/manage_proj_edit_page.php?project_id=', '')
            self.project_cache.append(Project(id=id, name=text))
        return list(self.project_cache)

    def create(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_css_selector('input[value="Create New Project"]').click()
        self.enter_text(project)
        wd.find_element_by_css_selector('input[value="Add Project"]').click()
        self.project_cache = None

    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.open_project_page()
        self.open_project_page_by_id(id)
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()
        self.project_cache = None

    def enter_text(self, project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)

    def open_project_page_by_id(self, id):
        wd = self.app.wd
        wd.get(self.app.base_url+'manage_proj_edit_page.php?project_id='+str(id))