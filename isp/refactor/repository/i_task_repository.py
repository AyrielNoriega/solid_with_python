from abc import ABC, abstractmethod
from asyncio import Task
from typing import List


class ITaskRepository(ABC):
    @abstractmethod
    def create_task(self, task: Task):
        raise NotImplementedError

    @abstractmethod
    def list_completed_tasks_by_user(self, user_id: int) -> List[Task]:
        raise NotImplementedError

    @abstractmethod
    def delete_task(self, task: Task):
        raise NotImplementedError
