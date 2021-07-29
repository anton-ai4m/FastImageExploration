from abc import ABC, abstractmethod

class DataSource(ABC):

    @abstractmethod
    def list_images(self):
        pass

    @abstractmethod
    def get_image(self, id):
        pass