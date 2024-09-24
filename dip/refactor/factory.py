


from typing import Optional
from dip.refactor.i_product_repository import IProductRepository
from dip.symptom.product_repository import ProductRepository


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


    def get(self, type: str) -> IProductRepository:
        result: Optional[IProductRepository] = None
        if type == 'default':
            result: IProductRepository = ProductRepository()

        return result