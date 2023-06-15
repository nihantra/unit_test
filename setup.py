from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in unit_test/__init__.py
from unit_test import __version__ as version

setup(
	name="unit_test",
	version=version,
	description="Unit Test",
	author="Nihantra C. Patel",
	author_email="n.patel.serpentcs@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
