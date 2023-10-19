from setuptools import setup, find_packages

setup(
    name='dirbuilder',
    version='0.2',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['dirbuilder=dirbuilder.__main__:main'],
    },
    install_requires=[
        'openai',
        'dotenv'
    ],
    url='https://github.com/m-c-frank/dirbuilder',
    license='GOS License',
    author='Martin Christoph Frank',
    author_email='martin7.frank7@gmail.com',
    description='A utility to translate structured text into directory structures.'
)
