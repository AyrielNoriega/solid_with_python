

from dip.refactor.factory import Factory
from dip.symptom.product import Product
from dip.symptom.service import Service


class Program:
    def __init__(self):
        repository = Factory().__instance.get('default')
        service = Service(repository)

        product = Product(
            product_id=1,
            name="Product 1",
            price=100.0
        )

        print(service.calculate_product_tax(product))
        service.save_product(product)

        products = service.list_products()
        for product in products:
            print(f"Id: {product.product_id}, name: {product.name}")


if __name__ == "__main__":
    Program()
    input("Press any key to continue...")
