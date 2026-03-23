from enum import Enum
from abc import ABC, abstractmethod

from .mail import Mail

class TransferType(Enum):
    CLI = "cli"

class Address(ABC):
    def __init__(self, transfer_type: TransferType):
        self.transfer_type = transfer_type
    
    @abstractmethod
    async def knock(self, mail: Mail):
        pass

class Address_CLI(Address):
    def __init__(self, log_func: callable):
        super().__init__(TransferType.CLI)
        self.log_func = log_func

    async def knock(self, mail: Mail):
        self.log_func(mail)