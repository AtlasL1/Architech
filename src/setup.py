from setuptools import setup, find_packages

setup(
    name='architech',
    version='0.0.1',
    author='Atlas',
    description='A Python package for AI',
    url='https://github.com/AtlasL1/Architech',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
