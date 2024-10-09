from setuptools import setup

setup(
    name="skiql",
    version="0.0.1",
    package_dir={"": "src"},
    install_requires=[
        "click",
        "pyodbc",
    ],
    extras_require={"dev": ["pytest", "black", "flake8", "isort"]},
)
