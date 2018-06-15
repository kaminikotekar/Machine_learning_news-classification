# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 19:20:08 2018

@author: Kamini
"""

def url_mod(url):
    if "https://" not in url:
        url_new="https://"+url
        return url_new
    else:
        return url