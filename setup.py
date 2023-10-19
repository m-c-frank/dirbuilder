from setuptools import setup, find_packages

setup(
    name='dirbuilder',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'openai',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'dirbuilder=dirbuilder.create_directories:main',
        ],
    },
)
