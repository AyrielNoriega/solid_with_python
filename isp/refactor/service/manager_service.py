from isp.symptom.i_repository import IRepository
from isp.symptom.model.project import Project


class ManagerService(object):
    def __init__(self, repository: IRepository):
        self.data_repository = repository


    def create_project(self, project: Project):
        result = True
        if project is None:
            result = False
        else:
            self.data_repository.create_project(project)

        return result


    def get_projects(self, user_id: int):
        projects = self.data_repository.list_projects_by_user(user_id)
        return projects