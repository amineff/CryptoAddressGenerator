from abc import ABC, abstractmethod

class WalletService(ABC):

    @abstractmethod
    def get_public_key(self):
        pass

    @abstractmethod
    def generate_address(self):
        pass

    @abstractmethod
    def delete(self):
        pass

