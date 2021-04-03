from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Reversify allows you to reverse text and audio'
LONG_DESCRIPTION = 'A package that allows you to reverse text and audio'

# Setting up
setup(
    name="Reversify",
    version=VERSION,
    author="Krmogi(Krishay R.)",
    author_email="<krishayras@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pyttsx3', 'pyaudio'],
    keywords=['python', 'reversify', 'audio', 'reverse-audio'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
