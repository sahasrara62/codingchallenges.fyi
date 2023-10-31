from setuptools import setup

setup(
    author="prashant",
    author_email="uchiha.rana62@gmail.com",
    description="""A cli tool written in python which mimic linux/unix command head behaviour.
    more info visit: https://codingchallenges.fyi/challenges/challenge-wc
    """,
    version="0.0.1",
    name="head_cc",
    py_modules=["main"],
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "cchead = main:main",
        ],
    },
)
