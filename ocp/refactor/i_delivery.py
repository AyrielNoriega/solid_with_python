

from abc import abstractmethod

from ocp.refactor.order import Order


class IDelivery:

    @abstractmethod
    def calculate_cost(self, order: Order):
        pass