from abc import ABC, ABCMeta, abstractmethod

class ViewInterface(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def render(self, gRenderer):
        pass

    @abstractmethod
    def handleEvent(self, e):
        pass

    @abstractmethod
    def init(self):
        pass

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
