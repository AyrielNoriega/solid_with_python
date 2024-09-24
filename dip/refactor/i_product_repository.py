

from abc import ABC, abstractmethod
from typing import List
from srp.symptom.product import Product


class IProductRepository(ABC):
    '''esta define los metodos que todo ProductRepository debe implementar'''

    @abstractmethod
    def save(self):
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[Product]:
        raise NotImplementedError
