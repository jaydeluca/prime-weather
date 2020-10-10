from setuptools import find_packages, setup

setup(
    name='app',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask-restx>=0.1.1',
        'python-dotenv',
        'marshmallow==3.2.0',
        'flask-accepts==0.17.0',
        'requests',
        'json_logging',
        'elastic-apm[flask]'
    ],
    extras_require={"dotenv": ["python-dotenv"]},
)