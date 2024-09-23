

from abc import ABC, abstractmethod
from asyncio import Task
from typing import List

from isp.symptom.model.project import Project
from isp.symptom.model.user import User

# esta interfaz se conoce como una Interfaz gorda, ya que tiene muchos métodos
# además, viola el principio RSP, ya que los métodos de la interfaz no son utilizados por todas las clases que la implementan
class IRepository(ABC):

    # user methods
    @abstractmethod
    def create_user(self, user: User):
        raise NotImplementedError

    @abstractmethod
    def list_users(self) -> List[User]:
        raise NotImplementedError

    @abstractmethod
    def delete_user(self, user: User):
        raise NotImplementedError

    # project methods
    @abstractmethod
    def create_project(self, project: Project):
        raise NotImplementedError

    @abstractmethod
    def list_projects_by_user(self, user_id: int) -> List[Project]:
        raise NotImplementedError

    # task methods
    @abstractmethod
    def create_task(self, task: Task):
        raise NotImplementedError

    @abstractmethod
    def list_completed_tasks_by_user(self, user_id: int) -> List[Task]:
        raise NotImplementedError

    @abstractmethod
    def delete_task(self, task: Task):
        raise NotImplementedError
