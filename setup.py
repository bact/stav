"""
Setup script for STAV

https://github.com/bact/stav
"""
from setuptools import find_packages, setup

readme = """
STAV: System Trustworthiness and Accountability Vocabulary

# Install

```sh
pip install stav
```
"""

setup(
    name="stav",
    version="0.1",
    description="STAV: System Trustworthiness and Accountability Vocabulary",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Arthit Suriyawongkul",
    author_email="suriyawa@tcd.ie",
    url="https://github.com/bact/stav",
    packages=find_packages(),
    python_requires=">=3",
    include_package_data=True,
    license="MIT",
    keywords=[
        "accountability",
        "trustworthiness",
        "artificial intelligence",
        "documentation",
        "law",
        "regulations",
        "vocabulary",
        "ontology",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Intended Audience :: Legal Industry",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Documentation",
        "Topic :: System :: Software Distribution",
    ],
    project_urls={
        "Source Code": "https://github.com/bact/stav",
        "Bug Tracker": "https://github.com/bact/stav/issues",
    },
)
