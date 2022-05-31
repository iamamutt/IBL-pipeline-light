#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name="ibl-pipeline-light",
    version="0.1.3",
    description="Light version of ibl pipeline to access data in IBL database",
    author="DataJoint",
    author_email="info@datajoint.com",
    packages=find_packages(exclude=[]),
    install_requires=["datajoint", "ibllib"],
)
