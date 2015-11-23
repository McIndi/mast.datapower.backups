import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname), "rb")as fin:
        return fin.read()

setup(
    name="mast.datapower.backups",
    version="2.0.0",
    author="Clifford Bressette",
    author_email="cliffordbressette@mcindi.com",
    description=(
        "A utility to help manage backups and checkpoints for IBM DataPower"),
    license="GPLv3",
    keywords="DataPower backup checkpoint",
    url="http://github.com/mcindi/mast.backups",
    namespace_packages=["mast", "mast.datapower"],
    packages=['mast', 'mast.datapower', 'mast.datapower.backups'],
    entry_points={
        'mast_web_plugin': [
            'backups = mast.datapower.backups:WebPlugin'
        ]
    },
    package_data={
        "mast.datapower.backups": ["docroot/*"]
    },
    incude_package_data=True,
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: GPLv3",
    ],
)
