import os
import json
import nibabel as nib
from PIL import Image
from pydicom import dcmread
import numpy as np

from .data_source import DataSource


class DirectoryDataSource(DataSource):

    def __init__(self, path, case):
        self.case = case
        self.init_file = path
        # Input is file with image filenames
        if os.path.isfile(path):
            self.data = {}
            with open(path, 'r') as file:
                lines = file.read().splitlines()
                for line in lines:
                    image, label = line.split(',', 1)
                    image = image.strip()
                    label = label.strip()
                    self.data[image] = label
        # Input is not a filename
        else:
            raise TypeError("Invalid input path")

    def list_images(self):
        return list(self.data.keys())

    def save_dataset(self):
        dir, file = os.path.split(self.init_file)
        out_file = os.path.join(dir, "modified_" + file)
        with open(out_file, 'w') as f:
            for image in self.data.keys():
                f.write("{}, {}\n".format(image, self.data[image]))

    def drop_image(self, filename):
        self.data.pop(filename, None)

    def get_image(self, filename):
        # Append the working directory if necessary
        if not os.path.isfile(filename):
            filename = os.path.join(os.path.split(self.init_file)[0], filename)

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
        if self.case == "detection":
            return np.array(json.loads(self.data[image]))
        return self.data[image]
