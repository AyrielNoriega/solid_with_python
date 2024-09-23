from typing import List
from isp.refactor.model.task import Task
from isp.refactor.repository.i_task_repository import ITaskRepository


class TeamMemberService:
    def __init__(self, repository: ITaskRepository):
        self.data_repository = repository

    def save_task(self, task: Task) -> bool:
        result = True
        if task is None:
            result = False
        else:
            self.data_repository.create_task(task)

        return result


    def get_completed_tasks(self, user_id: int) -> List[Task]:
        tasks = self.data_repository.list_completed_tasks_by_user(user_id)
        return tasks
