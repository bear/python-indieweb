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
        me            = 'http://127.0.0.1:9999'
        redirect_uri  = 'http://localhost:9999/success'
        client_id     = 'tester'
        r = ninka.indieauth.discoverAuthEndpoints(me)

        assert 'authorization_endpoint' in r

        authURL = None
        for url in r['authorization_endpoint']:
            authURL = url
            break

        assert authURL is not None
        assert authURL.scheme == 'https'
        assert authURL.netloc == 'indieauth.com'
        assert authURL.path   == '/auth'

        url = ParseResult(authURL.scheme, 
                          authURL.netloc,
                          authURL.path,
                          authURL.params,
                          urllib.urlencode({ 'me':            me,
                                             'redirect_uri':  redirect_uri,
                                             'client_id':     client_id,
                                             'scope':         'post',
                                             'response_type': 'id'
                                           }),
                          authURL.fragment).geturl()

        r = requests.get(url, verify=True)

        assert r.status_code == 200
