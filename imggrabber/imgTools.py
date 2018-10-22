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

import re


def searchTermUrl(searchTerm):  # Making the Search term Google URL friendly
    searchTerm = searchTerm.split()
    searchTerm = '+'.join(searchTerm)
    return searchTerm


def editURL(text):  # String to URL function
    ouTXT = re.compile('"ou":"[\\w\\d:/.\\-]+')
    URL = re.compile('"ou":"')
    TXT = ouTXT.findall(text)
    return URL.sub("", TXT[0])


def editType(text):  # URL type function
    ityTXT = re.findall('"ity":"[\\w]+', text)
    ityTXT = ''.join(ityTXT)
    extension = re.sub('"ity":"', '', ityTXT)
    return extension


def invDict(dictData):  # inverts unique and non-unique dictionary
    newdict = {}
    for k, v in dictData.items():
        newdict.setdefault(v, []).append(k)
    print("Dictionary Inverted")
    return newdict
