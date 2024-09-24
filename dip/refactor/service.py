

from typing import List
from dip.refactor.i_product_repository import IProductRepository
from srp.symptom.product import Product


class Service:

    def __init__(self, repository: IProductRepository):
        self.repository = repository


    def calculate_product_tax(self, product: Product) -> float:
        # validate product
        if product == None:
            return 0.0

        TAX: float = 0.19
        product_tax = product.price * TAX
        return product_tax


    def save_product(self, new_product: Product) -> bool:
        '''Save product in  DB products.txt file'''

        # validate product
        if new_product == None or new_product.id < 0 or new_product.name == None:
            return False

        # guardar producto usando el repositorio
        self.repository.save(new_product)

        return True


    def list_products(self) -> List[Product]:
        '''List all products in DB products.txt file'''

        products = self.repository.list()
        return products
