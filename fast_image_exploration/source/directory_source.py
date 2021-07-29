import os
from .data_source import DataSource

class DirectoryDataSource(DataSource):

    def __init__(self, path):
        # Input is file with image filenames
        if os.path.isfile(path):
            with open(path, 'r') as file:
                self.images = file.read().splitlines()
            # Append the directory of the file
            self.images = [os.path.join(os.path.split(path)[0], image) for image in self.images]
        # Input is the parent directory containing images
        elif os.path.isdir(path):
            self.images = []
            for dirname, _, filenames in os.walk(path):
                for filename in filenames:
                    image = os.path.join(dirname, filename)
                    self.images.append(image)
        # Exception case
        else:
            raise TypeError("Invalid input path")

    def list_images(self):
        return self.images

    def get_image(self, id):
        pass