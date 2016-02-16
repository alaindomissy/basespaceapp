from setuptools import setup  #, find_packages

setup(name='basespaceapp',
      version='0.0.0',
      description='template for basespace native app.',
      url='https://github.com/alaindomissy/basespaceapp',
      author='Alain Domissy',
      author_email='alaindomissy@gmail.com',
      license='MIT',
      # packages=find_packages(exclude=["tests"]),
      packages=['basespaceapp'],
      install_requires=[
            'six',                        # ==1.10.0',

            # 'decorator==4.0.6',
            # 'path.py==8.1.2',
            # 'pyparsing==2.0.3',

            # 'python-dateutil==2.4.2',
            # 'pytz==2015.7',
      ],
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
      ],
      zip_safe=False)
