# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 18:03:27 2018

@author: Kamini
"""

from urllib.request import urlopen
from urllib.error import URLError
import urllib.request


def url_check(url):
    """
    Checks that a given URL is reachable.
    :param url: A URL
    :rtype: bool
    """
    try:
        request = urllib.request.Request(url)
        request.get_method = lambda: 'HEAD'
        urllib.request.urlopen(request)
        return True
        
    except ValueError:
        return False

    except urllib.request.HTTPError:
        return False