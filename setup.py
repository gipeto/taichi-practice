from setuptools import setup

setup(name='taichi-practice',
      version='0.1',
      description='Collection of experiments using the taichi language',
      url='https://github.com/gipeto/taichi-practice',
      author='Javier Perez',
      author_email='202426+gipeto@users.noreply.github.com',
      license='MIT',
      packages=['taichi-practice'],
      install_requires=['taichi-nightly'],
      zip_safe=False)