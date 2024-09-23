from abc import ABC, abstractmethod
from typing import List
from isp.symptom.model.project import Project


class IProjectRepository(ABC):
    @abstractmethod
    def create_project(self, project: Project):
        raise NotImplementedError

    @abstractmethod
    def list_projects_by_user(self, user_id: int) -> List[Project]:
        raise NotImplementedError
