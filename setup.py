from setuptools import setup

setup(name='mrcnn',
      version='0.1.0',
      description='My version derivated from mattersport',
      url='https://github.com/laurentgrenier/mrcnn',
      author='Laurent Grenier',
      author_email='laurent@mooke.io',
      license='MIT',
      packages=['mrcnn'],
      install_requires=[
            'numpy==1.17.3',
            'pandas==0.25.3',
            'matplotlib==3.1.1',
            'scikit-image==0.16.2',
            'imgaug==0.2.6',
            'keras==2.2.4',
            'tensorflow-gpu==1.15.0',
            'albumentations==0.3.3',
            'IPython[all]'
      ],
      zip_safe=False)

