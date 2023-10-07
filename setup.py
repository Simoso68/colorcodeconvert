from setuptools import setup
from colorcodeconvert import metadata

def readfile(file):
    with open(file, "r") as f:
        return f.read()

setup(
    name=metadata["title"],
    version=metadata["version"],
    description="A simple library to convert color codes.",
    long_description=readfile("README.md"),
    long_description_content_type="text/markdown",
    author=metadata["author"],
    maintainer=metadata["author"],
    url=metadata["source"],
    license=metadata["license"],
    keywords=["color", "hex", "rgb"],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Information Technology",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Natural Language :: English"
    ],
    project_urls={
        "Source":"https://github.com/Simoso68/colorcodeconvert",
        "Issues":"https://github.com/Simoso68/colorcodeconvert/issues"
    },
    python_requires=">=3.6"
)