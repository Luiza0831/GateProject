from abc import ABC,abstractmethod

class Poarta(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def generateFile(self):
        pass

    @abstractmethod
    def readFile(self):
        pass