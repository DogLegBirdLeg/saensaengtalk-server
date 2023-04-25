from abc import *

from logic.auth.domain.Entity.User import User


class UserRepository(metaclass=ABCMeta):
    @abstractmethod
    def find_user_by_id(self, user_id) -> User:
        pass

    @abstractmethod
    def find_user_by_username(self, username) -> User:
        pass

    @abstractmethod
    def save(self, user: User):
        pass
