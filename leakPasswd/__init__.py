#!/usr/bin/env python
# encoding: UTF-8

__author__ = 'lauix'
__version__ = "1.1"

import requests

'''
blog : http://www.fucksec.com/
'''

URL = 'http://passwd.fucksec.com/api/'


def findBreach(name):
    data = {
        'name': name
    }
    r = requests.post(URL + 'findBreach', data=data)
    return r.json()


def queryBreachs():
    r = requests.post(URL + 'queryBreachs')
    return r.json()


def findAccount(account):
    data = {
        'account': account
    }
    r = requests.post(URL + 'findAccount', data=data)
    return r.json()
