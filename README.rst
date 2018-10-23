=====================
Google Image Grabber
=====================


It provides tools to grab images from a google search by extracting the links of
the images and downloading original  images.

This module is written for windows 10 on 64-bit processor.
It uses Selenium to open browser so as to scroll down to get more images than
possible otherwise. Thus it **needs a browser** to work correctly. This is on *default*
set to use *chrome browser* in case of inability to open it Firefox will be used.
The package comes with chromedriver and geckodriver with it.

Installation
============

To install gImageGrabber do as follow:

.. code-block:: console

    $ pip install gImageGrabber

There are two python files *imgScrape* and *imgTools*.

*imgScrape* has all the utilities needed to run the script but if you want to have additional control over the functions
you could explore *imgTools*.

Importing
============

To import this module to your script do this :

.. code-block:: python

    from gimagegrabber import imgScrape
    from gimagegrabber import imgTools


Functions
=========

Building URL
------------

:code:`imgScrape.build_url(search)`

This is to compose a google search URL for your search term.
To specify your search term use :code:`search` argument of the function to build the URL.

**Usage** :

.. code-block:: python

    from gimagegrabber import imgScrape

    searchTerm = "kamikaze eminem"

    url = imgScrape.build_url(searchTerm)
    print(url) #FOR DEBUG PURPOSE


Getting Source Data
--------------------

:code:`imgScrape.browser(url, test=False)`

This to start a browser windows and scroll down the webpage
to let more pictures load.It returns a raw source code data of the webpage encoded in *utf-8* format.
It takes 2 arguments :code:`url` and :code:`test` .

1. :code:`url` is the url of the page it needs to open.

2. :code:`test` is to make the browser scroll down less thus taking less time
   to return the source code. This is useful when you are writing or
   debugging something in your script.


It uses Chrome or Firefox to work so make sure you have Google chrome or Firefox
installed at their default directory.

Sometimes you might need to click on **show more images** on webpage to load even more images

If you cant seem to open browser make sure you are on 64-bit OS and that you have chrome
or Firefox installed.

If you are on 32-bit processor you need to use Firefox and you also have to download 32 bit
driver from `here <https://github.com/mozilla/geckodriver/releases>`_ and replace it with the
already present **geckodriver.exe** saved in **driver folder** of the gImageGrabber Module folder.

**Usage** :

.. code-block:: python

    from gimagegrabber import imgScrape

    searchTerm = "kamikaze eminem"

    url = imgScrape.build_url(searchTerm)
    raw_data = imgScrape.browser(url)
    print(raw_data) #FOR DEBUG PURPOSE


Extracting Links
----------------

:code:`imgScrape.imageLink(html)`

This extracts the original link of the images from the :code:`html`(source code) provided.
:code:`html` is the source code of the google image search page.
It returns a dict with format **[ link : file extension ]** . If you want
it in **[file extension : link]** you can use :code:`imgTools.invDict()`` function from imgTools

**Usage** :

.. code-block:: python

    from gimagegrabber import imgScrape
    from gimagegrabber import imgTools

    searchTerm = "kamikaze eminem"
    debug = False

    url = imgScrape.build_url(searchTerm)
    raw_data = imgScrape.browser(url,debug)
    links = imgScrape.imageLink(raw_data)
    print(links) #FOR DEBUG PURPOSE
    print(imgTools,invDict(links)) #FOR DEBUG PURPOSE

Saving Images
-------------

:code:`imgScrape.saveImages(data, name, onlyType)``

This saves all the images given to it in a list of format
**[link: file extension]**.

It takes 3 arguments:

1. :code:`data`  This is to provide  dictionary containing links to images in format **[link: file extension]**.

2. :code:`name`  This is to provide the name for the folder under which images will be saved.

3. :code:`onlyType`  If you want only a particular file extension then use this mention
   that. If not, then pass it a empty string or just don't use that argument.

The format in which it saves images is

::

    Root folder
    |-- Search Term
        |-- file extension(eg 'jpg')
            |-- 000001.jpg
            |-- 000002.jpg

**Usage** :

.. code-block:: python

    from gimagegrabber import imgScrape

    searchTerm = "Kamikaze"
    extension = '' #save all types of images

    url = imgScrape.build_url(searchTerm)
    raw_data = imgScrape.browser(url)
    links = imgScrape.imageLink(raw_data)
    imgScrape.saveImages(links,searchTerm,extension)


Example Code
============
This code is included in the package as :code:`simpleScript.py`.

.. code-block:: python

    from imggrabber import imgScrape

    # Search term
    search = 'kamikaze eminem'
    fType = ''  # if you want all the files them make it empty string
    debug = False

    html = imgScrape.browser(imgScrape.build_url(search), debug)
    data = imgScrape.imageLink(html)
    imgScrape.saveImages(data, search, fType)


Author
=======

Saksham Sharma
