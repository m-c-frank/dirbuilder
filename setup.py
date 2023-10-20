from setuptools import setup, find_packages

setup(
    name='dirbuilder',
    version='0.1.3',
    packages=find_packages(),
    include_package_data=True,  # This line is important
    package_data={
        'dirbuilder': ['uniformatter.ppt'],  # Include our .ppt file
    },
    entry_points={
        'console_scripts': ['dirbuilder=dirbuilder.__main__:main'],
    },
    install_requires=[
        'openai',
    ],
    url='https://github.com/m-c-frank/dirbuilder',
    license='GOS License',
    author='Martin Christoph Frank',
    author_email='martin7.frank7@gmail.com',
    description='A utility to translate structured text into directory structures.'
)
