from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    requirements_lst:List[str]=[]
    try:
        with open('requirements.txt') as file:
            lines = file.readlines()
            for line in lines:
                requirements = line.strip()
                # in the requirements at the lat line after enter we are going to have -e .
                if requirements and requirements!='-e .':
                    requirements_lst.append(requirements)
    except FileNotFoundError:
        print('requiremnets.text file not found')
    return requirements_lst

setup(name="NetworkSecurity",
      version="0.0.1",
      author="Nazanin Moradinasab",
      packages=find_packages(),
      install_requires=get_requirements()
      )
