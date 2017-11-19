from setuptools import setup
from setuptools import find_packages
import re as regex


def long_description():
    with open('README.md') as file:
        return file.read()

def get_version():
    with open('apex/__init__.py') as file:
        return regex.search(r'^__version__\s*=\s*"(.*)"$', file.read(), regex.MULTILINE).group(1)

setup(
    name='apex-framework',
    version=get_version(),
    description='A bot framework for Python',
    long_description=long_description(),
    url='https://lucia.moe',
    author='Valeth',
    author_email='a010@protonmail.com',
    license='GPL-3.0',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Communications :: Chat',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='bot discord framework',
    packages=find_packages(exclude=['tests*']),
    install_requires=[],
    python_requires='>=3.6',
    extras_require={
        'discord': ['discord.py'],
        'systemd': ['systemd']
    },
    scripts=[
        'bin/apex'
    ]
)
