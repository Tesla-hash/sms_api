#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
# see LICENSE file (it's BSD)


from setuptools import setup

setup(
    name="pyGSM",
    version="0.1",
    license="BSD",

    author="Tesla",
    author_email="adam.mckaig@gmail.com",

    maintainer="",
    maintainer_email="",
    install_requires=["pyserial","pytz"],

    description="Python interface to GSM modems",
    url="",
    packages=["pygsm", "pygsm.message"]
)
