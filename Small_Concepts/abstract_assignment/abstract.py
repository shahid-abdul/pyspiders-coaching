from abc import ABC,abstractmethod
# class Banking(ABC):
#     @abstractmethod
#     def payment(self):
#         pass

class FD_Account:
    @abstractmethod
    def interest(self):
        pass
    @abstractmethod
    def calculations(self):
        pass

