from abc import ABC, abstractmethod

class DatasetReport(ABC):

    @abstractmethod
    def generate(self, source):
        pass