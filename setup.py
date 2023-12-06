from setuptools import find_packages, setup
from typing import List

REQUAIREMENT_FILE_NAME="requirements.txt"
HYPEN_E_DOT = "-e ."
def get_requirements()->List[str]:

    with open(REQUAIREMENT_FILE_NAME) as requirement_file:
        requirements_list = requirement_file.readlines()
    requirements_list = [requirement_name.replace("\n","") for requirement_name in requirements_list]

    if HYPEN_E_DOT in requirements_list:
        requirements_list.remove(HYPEN_E_DOT)
    return requirements_list


setup(
    name="sensor",
    version="0.0.2",
    author="shubhangi",
    author_email="shubhangikumbhar2208@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)