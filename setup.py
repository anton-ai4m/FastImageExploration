from setuptools import setup, find_packages

setup(name='fast_image_exploration',
      version='0.0.4',
      description='A library for imaging dataset exploration',
      url='https://github.com/anton-ai4m/FastImageExploration',
      author='Anton Shemyakov',
      author_email='anton@ai4medicine.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'pydicom',
          'nibabel',
          'numpy',
          'pillow',
          'matplotlib'
      ],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'])