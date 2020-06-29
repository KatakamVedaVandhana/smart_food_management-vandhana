from abc import ABC
from abc import abstractmethod

class PresenterInterface(ABC):

    @abstractmethod
    def raise_exception_for_invalid_offset(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_limit(self):
        pass
