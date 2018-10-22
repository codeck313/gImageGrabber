from setuptools import setup
setup(
    name='gImageGrabber',
    version='0.1.9',
    author='Saksham Sharma',
    author_email='codeck313@gmail.com',
    packages=['imggrabber', 'imggrabber.test'],
    scripts=['bin/simpleScript.py'],
    url='https://pypi.org/project/gImageGrabber',
    project_url={
        'gImageGrabber Source': 'https://github.com/codeck313/gImageGrabber',
    },
    data_files=[
        ('driver', ['driver/chromedriver.exe', 'driver/geckodriver.exe']),
    ],
    license='GNU General Public License version 3',
    description='Tool download orignal resolution images from Google search',
    long_description=open('README.rst').read(),
    keywords="google images extractor parser webpage gImageGrabber grabber extract",
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
