from abc import ABC, abstractmethod


class DataSource(ABC):

    @abstractmethod
    def list_images(self):
        pass

    @abstractmethod
    def get_image(self, id):
        pass

    @abstractmethod
    def get_label(self, id):
        pass

    @abstractmethod
    def drop_image(self, id):
        pass

    @abstractmethod
    def save_dataset(self):
        pass