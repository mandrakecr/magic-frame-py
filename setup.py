from setuptools import setup, find_packages

setup(
    name="magic-frame-py",
    version="0.1.0",
    description="Common set of APIs for my projects",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="MandrakeCR",
    author_email="mandrake@debugcamp.com",
    url="https://www.debugcamp.com/magic-frame-py",  # Replace with your private repo URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)