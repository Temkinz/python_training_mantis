from model.project import Project
import random
import string


def random_project_name(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_create_project(app):
    app.session.login("administrator", "root")
    old_projects = app.project.get_project_list()
    new_project = Project(name=random_project_name("project_", 10))
    app.project.create(new_project)
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(new_project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)