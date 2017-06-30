from setuptools import setup, find_packages

setup(
    name='blog',
    version='1.0',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = blog.settings']},
)
