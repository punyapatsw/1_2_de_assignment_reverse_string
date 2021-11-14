"""Package configuration."""
from setuptools import find_packages, setup

setup(
    name="1_2_de_assignment_reverse_string",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
