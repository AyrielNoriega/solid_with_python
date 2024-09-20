

from ocp.refactor.i_delivery import IDelivery
from ocp.refactor.order import Order


class MexicoDelivery(IDelivery):

    def calculate_cost(self, order: Order):
        result = 98
        return result