import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
      name='report_tool',
      version='1.1.0',
      description='Tool for Report Instagram Users',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/Aspoky/report-tool/',
      author='Aspoky',
      author_email = '',
      license='MIT',
      packages=['report_tool'],
      install_requires=[
          'selenium>=3.14.1',
          'fake_useragent>=0.1.11',
      ],
      python_requires='>=3.6.0',
      zip_safe=False)