import os
import nibabel as nib
from PIL import Image
from pydicom import dcmread
import numpy as np

from .data_source import DataSource

class DirectoryDataSource(DataSource):

    def __init__(self, path, case):
        self.case = case
        # Input is file with image filenames
        if os.path.isfile(path):
            self.data = {}
            with open(path, 'r') as file:
                lines = file.read().splitlines()
                for line in lines:
                    image, label = line.split(',')
                    image = image.strip()
                    label = label.strip()
                    # Append the directory of the file if necessary:
                    if self.case == "segmentation":
                        if not os.path.isfile(label):
                            label = os.path.join(os.path.split(path)[0], label)
                    if os.path.isfile(image):
                        self.data[image] = label
                    else:
                        self.data[os.path.join(os.path.split(path)[0], image)] = label
        # Input is not a filename
        else:
            raise TypeError("Invalid input path")

    def list_images(self):
        return list(self.data.keys())

    def get_image(self, filename):
        if filename.endswith('.dcm'):
            img = dcmread(id)
            return img.pixel_array
        if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
            image = Image.open(filename)
            return np.asarray(image)
        if filename.endswith('.nii'):
            img = nib.load(filename)
            return np.array(img.dataobj)
        raise TypeError("Image format not supported. Use one of dicom / nifty / png / jpg")

    def get_label(self, image):
        # If label is an image stored as a filename, load image
        if self.case == "segmentation":
            return self.get_image(self.data[image])
        return self.data[image]