from setuptools import setup

setup(
    name="private_lib",
    version="0.1.0",
    py_modules=["private_lib"],
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "hello = private_lib.hello:cli",
        ],
    },
)
