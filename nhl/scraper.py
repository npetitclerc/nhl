#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''scraper.py

Utility functions for reading tables. 

'''

from bs4 import BeautifulSoup
import urllib2
import re
import logging
import urlparse



def get_soup(url):
    '''Returns a BeautifulSoup object from the given URL'''

    try: 
        html = urllib2.urlopen(url).read()
        soup = BeautifulSoup(html, 'lxml')
    except Exception as e:
        logging('Could not load {}, {}'.format(url, e.message))
        raise e

    return soup  


def get_qp_from_href(row, name, href_string):
    '''Returns a query parameter value from the href value

    Example:
    With href_string = '/ice/player.htm?id=8471675'

    The function returns 8471675

    '''
    p = "^" + href_string
    anchor_tag = row.find(href=re.compile(p))  

    if anchor_tag:
        href = anchor_tag.attrs['href']
        query = urlparse.parse_qs(urlparse.urlparse(href).query)    
        param = query.get(name, None)
        if param:
            return param[0]  


         

