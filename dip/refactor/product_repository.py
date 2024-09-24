

from typing import List
from dip.refactor.i_product_repository import IProductRepository
from srp.symptom.product import Product


class ProductRepository(IProductRepository):
    __file_name_db = "products.txt"


    def __init__(self) -> None:
        self.__init_database()


    def save(self, new_product: Product) -> None:
        '''Save product in  DB products.txt file'''
        with open(self.__file_name_db, "a") as file:
            file.write(f"{new_product.id},{new_product.name},{new_product.price}\n")


    def list(self) -> List[Product]:
        '''List all products in DB products.txt file'''

        # read products from file
        products = []
        with open(self.__file_name_db, "r") as file:
            for line in file:
                product_data = line.split(",")
                product = Product(
                    id=int(product_data[0]),
                    name=product_data[1],
                    price=float(product_data[2])
                )
                products.append(product)

        # return products
        return products


    def __init_database(self):
        '''Create products.txt file if not exists'''
        try:
            with open(self.__file_name_db, "x") as file:
                print("DB products.txt file created")
        except FileExistsError:
            pass
