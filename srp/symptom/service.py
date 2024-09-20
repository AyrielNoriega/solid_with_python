

from typing import List
from srp.symptom.product import Product


class Service:
    __file_name_db = "products.txt"

    def __init__(self):
        self.__init_database()

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

        # guardar producto en archivo products.txt
        with open(self.__file_name_db, "a") as file:
            file.write(f"{new_product.id},{new_product.name},{new_product.price}\n")

        # save product
        return True


    def list_products(self) -> List[Product]:
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
