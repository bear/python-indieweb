#!/usr/bin/env python

"""
:copyright: (c) 2015 by Mike Taylor
:license: MIT, see LICENSE for more details.
"""

import unittest
import urllib
from urlparse import ParseResult

import requests
import ninka

class TestEndpoint(unittest.TestCase):
    def runTest(self):
        me = 'http://127.0.0.1:9999'
        r = ninka.discoverMicropubEndpoints(me)

        assert 'micropub' in r

        micropubURL = None
        for url in r['micropub']:
            micropubURL = url
            break

        assert micropubURL is not None
        assert micropubURL.scheme == 'http'
        assert micropubURL.netloc == '127.0.0.1:9999'
        assert micropubURL.path   == '/micropub'

        # url = ParseResult(micropubURL.scheme, 
        #                   micropubURL.netloc,
        #                   micropubURL.path,
        #                   micropubURL.params,
        #                   urllib.urlencode({ 'me':            me,
        #                                      'redirect_uri':  redirect_uri,
        #                                      'client_id':     client_id,
        #                                      'scope':         'post',
        #                                      'response_type': 'id'
        #                                    }),
        #                   micropubURL.fragment).geturl()

        # r = requests.get(url, verify=True)

        # assert r.status_code == 200


# POST /micropub HTTP/1.1
# Host: bear.im
# Accept: */*
# Authorization: Bearer 159d4823-de7d-4717-9e4b-401da86a413b
# Content-Length: 30
# Content-Type: application/x-www-form-urlencoded

# h=entry&content=test&slug=test
