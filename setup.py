import setuptools

setuptools.setup(
    name='pyics',
    version='0.1.0',
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
        'urllib3[secure]'
    ]
)
