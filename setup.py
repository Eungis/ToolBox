# /setup.py
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ToolCadeau", # Replace with your own username
    version="0.0.1",
    author="Eungis",
    author_email="eungizoa@gmail.com",
    description="self-made python package utils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Eungis/ToolBox",
    packages=setuptools.find_packages(exclude=[]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
