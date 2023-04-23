from abc import *
from typing import List

from app.api.Order.Domain.Entity.Order import Order


class OrderRepository(metaclass=ABCMeta):
    @abstractmethod
    def find_order_by_user_id(self, post_id, user_id) -> Order:
        pass

    @abstractmethod
    def find_orders_by_post_id(self, post_id) -> List[Order]:
        pass

    @abstractmethod
    def save(self, order: Order):
        pass

    @abstractmethod
    def delete(self, post_id, user_id):
        pass
