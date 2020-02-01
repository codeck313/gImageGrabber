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

from bs4 import BeautifulSoup
from imggrabber import imgTools
import os
import urllib.request as ulib
import urllib.error as ulibError
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import re
import platform


def build_url(search):
    # google image url
    url1 = "https://www.google.com/search?q={}"
    url2 = "&client=ubuntu&hs=rss&channel=fs&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiwg5njq_fiAhVBqo8KHWAGD1kQ_AUIECgB&biw=880&bih=864"
    urlJoin = url1+url2
    url = urlJoin.format(imgTools.searchTermUrl(
        search))
    print("Using URL : ", url)
    return url


def browser(url, test=False):  # Using Browser to get the extended source code
    print("Loading the Web-Browser")
    pathDIR = os.path.abspath(__file__)

    if platform.system() == 'Windows':
        print("Working on Windows")
        pathFinder = re.compile(r'[\w\d:\\]+(?=lib)')
    elif platform.system() == 'Linux':
        print("Working on Linux")
        pathFinder = re.compile(r'[\w\d:\/]+(?=lib)')

    pathList = pathFinder.findall(pathDIR)
    path = pathList[0]

    try:
        pathchrome = ""
        print("Trying to load Chrome")
        if platform.system() == 'Windows':
            pathchrome = path+"driver\chromedriver.exe"
        elif platform.system() == 'Linux':
            pathchrome = path+"driver/chromedriver"
        driver = webdriver.Chrome(
            executable_path=pathchrome)
        print("Chrome Browser opened")

    except Exception:
        print("****Cant Open Chrome****")

        try:
            pathfirefox = ""
            print("Trying to load Firefox now")

            if platform.system() == 'Windows':
                pathfirefox = path+"driver\geckodriver.exe"
            elif platform.system() == 'Linux':
                pathfirefox = path+"driver/geckodriver"

            driver = webdriver.Firefox(
                executable_path=pathfirefox)
            print("Firefox Browser opened")

        except Exception:
            print("****Cant Open Firefox****")
            print("****Exiting Now****")
            sys.exit()

    print("Opening the URL")
    driver.get(url)
    element = driver.find_element_by_tag_name("body")
    print("Scrolling Started")
    if test:
        print("Running test")
        for i in range(5):
            element.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.3)

    else:
        for j in range(2):
            for i in range(50):
                element.send_keys(Keys.PAGE_DOWN)
                time.sleep(0.3)
            print("--A brief Pause--")
            time.sleep(1)
    time.sleep(0.5)
    temp = driver.page_source.encode('utf-8')
    print("Closing Browser")
    driver.close()
    return temp


def imageLink(html):  # get images from url
    page = BeautifulSoup(html, 'html.parser')
    print("Data handed to Beautifull Soup")

    # webpage parsing
    data = {}
    print("Formatting and creating Dictionary")
    for div in page.findAll('div', {'class': 'rg_meta notranslate'}):
        link = imgTools.editURL(div.string)
        type = imgTools.editType(div.string)
        data[link] = type
    print("Dictionary Created")
    print("Got", len(data), "links")
    return data


def saveImages(data, name, onlyType='', startingnos=0, prefix=""):
    if onlyType is '':
        onlyType = ' '
    data = imgTools.invDict(data)
    print("Making Root Directory")
    directory = name.replace(' ', '_')
    if not os.path.isdir(directory):
        os.mkdir(directory)

    print("Saving pictures now")
    if onlyType == ' ':
        print("Saving all Types")
        for type in data.keys():
            for i, link in enumerate(data[type]):
                if type == '':
                    typeDirec = 'Forced jpg'
                    if not os.path.isdir(directory+"/"+typeDirec):
                        os.mkdir(directory+"/"+typeDirec)
                    savepath = os.path.join(
                        directory, typeDirec, (prefix+'{:06}.jpg'.format(i+startingnos)))
                    print(link, "save as", (prefix+str(i+startingnos)+".jpg"))
                    try:
                        ulib.urlretrieve(link, savepath)
                    except (ulibError.HTTPError, ulibError.URLError) as e:
                        print(str(e))
                        continue
                else:
                    if not os.path.isdir(directory+"/"+type):
                        os.mkdir(directory+"/"+type)
                    savepath = os.path.join(
                        directory, type, (prefix+'{:06}.{}'.format((i+startingnos), type)))
                    try:
                        ulib.urlretrieve(link, savepath)
                    except (ulibError.HTTPError, ulibError.URLError) as e:
                        print(str(e))
                        pass
                    print(link, "save as", (prefix+str(i+startingnos)+"."+type))
    elif onlyType in data:
        print("Saving only", onlyType)
        for i, link in enumerate(data[onlyType]):
            if not os.path.isdir(directory+"/"+onlyType):
                os.mkdir(directory+"/"+onlyType)
            savepath = os.path.join(
                directory, onlyType, (prefix + '{:06}.{}'.format((i+startingnos), onlyType)))
            print(link+" save as "+prefix+str(i+startingnos)+"."+onlyType)
            try:
                ulib.urlretrieve(link, savepath)
            except (ulibError.HTTPError, ulibError.URLError) as e:
                print(str(e))
                continue
    else:
        print("****No picture found with '"+onlyType+"' Extension****")
