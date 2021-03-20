# -*- encoding: utf-8 -*-
# Source: https://packaging.python.org/guides/distributing-packages-using-setuptools/

import io
import re
from get_version import get_version

from setuptools import find_packages, setup

dev_requirements = [
    'bandit',
    'flake8',
    'pytest',
    'pytest-cov'
]
unit_test_requirements = [
    'pytest',
]
integration_test_requirements = [
    'pytest',
]
run_requirements = [
    'flask',
    'wheel',
    'flask_prometheus_metrics',
    'psycopg2'
]

version = get_version();

with io.open('README.md', encoding='utf8') as readme:
    long_description = readme.read()


setuptools.setup(
    name="flask_profissional",
    version="0.0.1",
    author="Bruno Rozendo",
    author_email="bruno@brunorozendo.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brunorozendo/flask_professional",
    project_urls={
        "Bug Tracker": "https://github.com/brunorozendo/flask_professional/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        'Operating System :: POSIX :: Linux'
    ],
    packages=setuptools.find_packages(where="src/main/python",exclude='src/tests' ),
    python_requires=">=3.9",
    install_requires=run_requirements,
    extras_require={
         'dev': dev_requirements,
         'unit': unit_test_requirements,
         'integration': integration_test_requirements,
    },
    zip_safe=False
)
