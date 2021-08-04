import matplotlib.pyplot as plt
import matplotlib.patches as patches
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

    def images(self):
        return self.source.list_images()

    def view_image(self, id):
        image = self.source.get_image(id)
        label = self.source.get_label(id)
        fig, ax = plt.subplots()
        ax.imshow(image)
        if self.case == "classification":
            plt.title("Class {}".format(label))
        if self.case == "segmentation":
            plt.imshow(label, alpha=0.3)
        if self.case == "detection":
            for bbox in label:
                bbox = patches.Rectangle((bbox[0],
                                          bbox[1]),
                                         bbox[2] - bbox[0],
                                         bbox[3] - bbox[1],
                                         linewidth=1, edgecolor='r', facecolor='none')
                ax.add_patch(bbox)
        plt.show()