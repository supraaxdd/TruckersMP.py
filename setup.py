from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="truckersmp.py",
    version="1.0.0.1",
    description="Simple API Wrapper for the TruckersMP API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/supraaxdd/truckersmp-api",
    author="Itz Blinkzy, supraaxdd",
    author_email="legendarystone12@gmail.com, supra6950@gmail.com",
    license="GNU",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    keywords="api wrapper truckersmp",
    python_requires=">=3.7",
    packages=find_packages(),
    install_requires=[],
)