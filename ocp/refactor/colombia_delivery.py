

from ocp.refactor.i_delivery import IDelivery
from ocp.refactor.order import Order


class ColombiaDelivery(IDelivery):

    def calculate_cost(self, order: Order):
        result = order.total * 0.01
        if order.weight <= 2:
            result += 9900
        else:
            result += order.weight * 5000

        return result