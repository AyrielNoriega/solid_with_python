
from ocp.refactor.factory import Factory
from ocp.refactor.order import Order


class Store:
    def __init__(self):
        pass


    def calculate_delivery_cost(self, order: Order) -> float:
        if order == None:
            return -1

        delivery = Factory.__instance.get(order.country)
        result = delivery.calculate_cost(order)

        return result