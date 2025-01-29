from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mgen_management/__init__.py
from mgen_management import __version__ as version

setup(
    name="mgen_management",
    version=version,
    description="Mgen Management",
    author="Fat7allah",
    author_email="fat7allah.habbani@gmail.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
