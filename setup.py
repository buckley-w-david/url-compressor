from setuptools import find_packages, setup

setup(
    name='url_compressor',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'Flask-WTF',
        'dahuffman',
        'click',
        'gunicorn'
    ],
)
