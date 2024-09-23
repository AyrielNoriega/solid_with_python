from typing import List
from isp.symptom.i_repository import IRepository
from isp.symptom.model.user import User


class AdminService:
    def __init__(self, repository: IRepository):
        self.data_repository = repository

    def save_user(self, user: User) -> bool:
        result = True
        # validations and business rules
        if user is None:
            result = False
        else:
            self.data_repository.create_user(user)

        return result
    
    
    def get_users(self) -> List[User]:
        users = self.data_repository.list_users()
        return users