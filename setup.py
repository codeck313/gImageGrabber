# Script to Grab the image links from a google search and then downlaoding them
# Copyright (C) 2018  Saksham Sharma
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup
setup(
    name='gImageGrabber',
    version='0.1.16.1',
    author='Saksham Sharma',
    author_email='codeck313@gmail.com',
    packages=['imggrabber'],
    scripts=['bin/simpleScript.py'],
    url='https://pypi.org/project/gImageGrabber',
    project_urls={
        'gImageGrabber Source': 'https://github.com/codeck313/gImageGrabber',
    },
    data_files=[
        ('driver', ['driver/chromedriver.exe', 'driver/geckodriver.exe']),
    ],
    license='GNU General Public License version 3',
    description='Tools to download images from Google search',
    long_description=open('README.rst').read(),
    keywords="google images extractor parser webpage gImageGrabber grabber extract search image python",
    install_requires=[
        "urllib3 == 1.23",
        "beautifulsoup4==4.6.3",
        "selenium==3.14.1",

    ],
    classifiers=[
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Utilities",

    ],
)
