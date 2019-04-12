from __future__ import absolute_import
from setuptools import setup

setup(
    name="applepay",
    version="0.4.0",
    author="Taras Halturin",
    author_email="halturin@gmail.com",
    description=("A Python library for decrypting Apple Pay payment tokens."),
    license="BSD",
    keywords="applepay payment tokens",
    url="https://github.com/halturin/applepay",
    packages=['applepay', 'tests'],
    install_requires=[],
    setup_requires=['pytest-runner>=2.0,<3dev'],
    tests_require=[
        'pytest>=3.0.6', 'pytz==2016.10', 'pytest-capturelog>=0.7',
        'freezegun>=0.3.8', 'six'
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
