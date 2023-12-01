from setuptools import setup, find_packages

setup(
    name='fastapimongogen',
    version='0.0.1',
    author='Agustin Vivancos',
    author_email='agusvc@gmail.com',
    description='FastAPI Mongo Generator with manage.py superpowers',
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'pymongo',
        'uvicorn',
        'pydantic',
        'motor',
        'python-dotenv',
        'pydantic',
        'odmantic',
        'fastapi-users',
        
    ],
)
