from abc import abstractmethod

from serviceable import Serviceable

class Tires(Serviceable):
    @abstractmethod
    def needs_service(self):
        pass