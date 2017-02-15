from setuptools import setup

setup(
    name='flaskr',
    version='0.1',
    long_description=__doc__,
    packages=['flaskr'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)
