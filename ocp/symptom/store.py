
from ocp.symptom.country_enum import CountryEnum


class Store:
    def __init__(self):
        pass


    def calculate_delivery_cost(self, order: Order) -> float:
        if order == None:
            return -1

        result = 0.0
        if order.country == CountryEnum.Colombia:
            result = order.total * 0.01
            if order.weight <= 2:
                result += 9900
            else:
                result += order.weight * 5000

        elif order.country == CountryEnum.Mexico:
            result = 98.0
        return result