

from ocp.refactor.colombia_delivery import ColombiaDelivery
from ocp.refactor.i_delivery import IDelivery
from ocp.refactor.mexico_delivery import MexicoDelivery
from ocp.symptom.country_enum import CountryEnum


class Factory:

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Factory, cls).__new__(cls)
        return cls.__instance


    def __init__(self):
        if not hasattr(self, '_initialized'):
            # Inicializa la instancia aquí
            self._initialized = True

        self.delivery_dictionary = dict[CountryEnum, IDelivery]

        self.delivery_dictionary.push(CountryEnum.Colombia, ColombiaDelivery())
        self.delivery_dictionary.push(CountryEnum.Mexico, MexicoDelivery())


    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = Factory()
        return cls.__instance


    def get(self, country: CountryEnum) -> IDelivery:
        result = None

        if self.delivery_dictionary.has_key(country):
            result = self.delivery_dictionary.get(country)

        return result
