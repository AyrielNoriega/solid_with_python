from abc import ABC, abstractmethod
from typing import List
from isp.symptom.model.user import User


class IUserRepository(ABC):
    @abstractmethod
    def create_user(self, user: User):
        raise NotImplementedError

    @abstractmethod
    def list_users(self) -> List[User]:
        raise NotImplementedError

    @abstractmethod
    def delete_user(self, user: User):
        raise NotImplementedError
