# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="bs4",
    version="0.0.1",
    author="Leonard Richardson",
    author_email='leonardr@segfault.org',
    url="https://pypi.python.org/pypi/beautifulsoup4",
    download_url="http://www.crummy.com/software/BeautifulSoup/bs4/download/",
    description="Screen-scraping library",
    long_description="""Use `beautifulsoup4 <https://pypi.python.org/pypi/beautifulsoup4>`_ instead.""",    # noqa
    license="MIT",
    install_requires=['beautifulsoup4'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 3',
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Text Processing :: Markup :: XML",
        "Topic :: Text Processing :: Markup :: SGML",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
