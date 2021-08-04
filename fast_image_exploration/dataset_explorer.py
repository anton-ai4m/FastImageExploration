import matplotlib.pyplot as plt
from .source.directory_source import DirectoryDataSource

class DatasetExplorer():

    def __init__(self, cfg):
        # Case is one of classification, segmentation, detection. Classification by default
        try:
            self.case = cfg['case']
        except KeyError:
            self.case = "classification"
        self.source = DirectoryDataSource(cfg['input_file'], self.case)

    def _count_images(self):
        return len(self.source.list_images())

    def view_image(self, id):
        if self.case == "classification":
            image = self.source.get_image(id)
            label = self.source.get_label(id)
            plt.imshow(image)
            plt.title("Class {}".format(label))
            plt.show()
        if self.case == "segmentation":
            image = self.source.get_image(id)
            label = self.source.get_label(id)
            plt.imshow(image)
            plt.imshow(label, alpha=0.3)
            plt.show()