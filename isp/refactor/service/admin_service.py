from typing import List
from isp.refactor.repository.i_user_repository import IUserRepository
from isp.symptom.model.user import User


class AdminService():
    def __init__(self, repository: IUserRepository):
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


    def delete_user(self, user: User) -> bool:
        result = True
        if user is None:
            result = False
        else:
            self.data_repository.delete_user(user)

        return result