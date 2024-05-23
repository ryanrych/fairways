from setuptools import setup, find_packages
setup(
    name='Fairways',
    version='1.0.0',
    author='Ryan Rychlak',
    author_email='ryanjrychlak@gmail.com',
    description='A wrapper for the Fairways API golf course database',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11.7',
)
