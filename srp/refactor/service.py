

from typing import List
from srp.refactor.product_repository import ProductRepository
from srp.symptom.product import Product


class Service:
    '''
    Service class: la responsabilidad de esta clase es la lógica de negocio.
    El acceso a datos es responsabilidad de la clase ProductRepository.
    '''
    __file_name_db = "products.txt"

    def __init__(self):
        self.__init_database()
        self.__product_repository = ProductRepository()


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
        self.__product_repository.save(new_product)

        return True


    def list_products(self) -> List[Product]:
        '''List all products in DB products.txt file'''

        products = self.__product_repository.list()
        return products


    def __init_database(self):
        '''Create products.txt file if not exists'''
        try:
            with open(self.__file_name_db, "x") as file:
                print("DB products.txt file created")
        except FileExistsError:
            pass