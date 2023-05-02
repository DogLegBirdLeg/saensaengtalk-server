from abc import *


class TokenDao(metaclass=ABCMeta):
    @abstractmethod
    def find_token_by_user_id(self, user_id):
        pass

    @abstractmethod
    def find_token_by_refresh_token(self, refresh_token):
        pass

    @abstractmethod
    def save(self, user_id, access_token, refresh_token, registration_token):
        pass

    @abstractmethod
    def delete(self, user_id):
        pass

    @abstractmethod
    def update_access_token(self, user_id, access_token):
        pass

    @abstractmethod
    def update_registration_token(self, user_id, registration_token):
        pass
