from setuptools import find_packages, setup 
from typing import List 

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]: 
    requirements = []
    with open(file_path) as file_obj: 
        requirements = file_obj.readlines() 
        requirements = [req.replace('\n','') for req in requirements] 
        if HYPEN_E_DOT in requirements: 
            requirements.remove(HYPEN_E_DOT)
    return requirements 

setup(
    name = 'Diamond Price Prediction', # project name
    version = '0.0.1', # required by pypi to keep track of updates 
    author = 'Tanya Shekhawat', 
    author_email= '9tanya18@gmail.com', 
    install_requires = get_requirements('requirements.txt'), # ['pandas', 'sklearn'] #what all things u need to install before making this package 
    packages = find_packages()
)
