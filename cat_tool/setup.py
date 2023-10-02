from setuptools import setup, find_packages

setup(
    author="prashant",
    author_email="uchiha.rana62@gmail.com",
    description="""A UNIX command `cat` implementation in python https://codingchallenges.fyi/challenges/challenge-cat""",
    version="0.0.1",
    name="cat",
    py_modules=find_packages(),
    packages=["unix_cat"],
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "py_cat = unix_cat.pycat:py_cat",
        ],
    },
)