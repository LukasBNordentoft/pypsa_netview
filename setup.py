from setuptools import setup

setup(
    name='pypsa_netview',
    version='0.1.0',    
    description='Package for visualizing PyPSA Networks',
    url='https://github.com/LukasBNordentoft/pypsa_netview',
    author='Lukas B. Nordentoft',
    packages=['pypsa_netview'],
    install_requires=['pandas',
                      'numpy',  
                      'schemdraw',
                      'pypsa',
                      ],
    )