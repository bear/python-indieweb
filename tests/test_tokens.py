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
        r = ninka.discoverTokenEndpoints(me)

        assert 'token_endpoint' in r

        tokenURL = None
        for url in r['token_endpoint']:
            tokenURL = url
            break

        assert tokenURL is not None
        assert tokenURL.scheme == 'http'
        assert tokenURL.netloc == '127.0.0.1:9999'
        assert tokenURL.path   == '/token'

        url = ParseResult(tokenURL.scheme, 
                          tokenURL.netloc,
                          tokenURL.path,
                          tokenURL.params,
                          urllib.urlencode({ 'me':    me,
                                             'scope': 'post'
                                           }),
                          tokenURL.fragment).geturl()

        r = requests.get(url)

        # token GET with no access_token present
        assert r.status_code == 400

        # token POST

        # token GET with valid access_token


# POST /micropub HTTP/1.1
# Host: bear.im
# Accept: */*
# Authorization: Bearer 159d4823-de7d-4717-9e4b-401da86a413b
# Content-Length: 30
# Content-Type: application/x-www-form-urlencoded

# h=entry&content=test&slug=test
