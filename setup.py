import json
from pathlib import Path

from setuptools import setup, find_packages


REPO_DIR = Path(__file__).parent.resolve()

with open(REPO_DIR / "README.md") as handle:
    README = handle.read()

with open(REPO_DIR / "metadata.json") as handle:
    METADATA: dict = json.load(handle)

with open(REPO_DIR / "requirements.txt") as handle:
    REQUIREMENTS = [f"{_.strip()}" for _ in handle.readlines() if " " not in _]

with open(REPO_DIR / "requirements_dev.txt") as handle:
    DEV = [f"{_.strip()}" for _ in handle.readlines() if " " not in _]


setup(
    name="aiidalab-sssp-workflow",
    version=METADATA["version"],
    license="MIT License",
    author=METADATA["authors"],
    author_email="aiidalab@materialscloud.org",
    description=METADATA["description"],
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/aiidalab/aiidalab-sssp-workflow",
    python_requires=">=3.6",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: AiiDA",
        "Framework :: Jupyter",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Widget Sets",
    ],
    install_requires=REQUIREMENTS,
    extras_require={"dev": DEV},
)
