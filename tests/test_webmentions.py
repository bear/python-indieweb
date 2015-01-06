#!/usr/bin/env python

"""
:copyright: (c) 2015 by Mike Taylor
:license: MIT, see LICENSE for more details.
"""

import unittest
import ronkyuu

class TestEndpoint(unittest.TestCase):
    def runTest(self):
        result = ronkyuu.discoverEndpoint('http://localhost:9999')
        assert result[0] == 200
        assert result[1] == 'http://localhost:9999/webmention'

class TestWebmention(unittest.TestCase):
    def runTest(self):
        status_code, webmention_url = ronkyuu.discoverEndpoint('http://localhost:9999')

        assert status_code == 200

        result = ronkyuu.sendWebmention('http://boathole.org/testing', 'http://localhost:9999/article2', webmention_url)

        assert result.status_code == 200

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('sourceURL')
#     parser.add_argument('--vouch',           default=None)
#     parser.add_argument('--eventConfigFile', default=None)

#     args = parser.parse_args()
#     cfg  = ronkyuu.discoverConfig(args.eventConfigFile)

#     domains     = [] #cfg.get('domains', [])
#     sourceURL   = args.sourceURL
#     vouchDomain = args.vouch

#     print('Scanning %s for mentions' % sourceURL)
#     if vouchDomain is not None:
#         print('vouch domain present and will be sent')

#     mentions = ronkyuu.findMentions(sourceURL, domains)

#     print(mentions['refs'])

#     for href in mentions['refs']:
#         if sourceURL <> href:
#             print href
#             wmStatus, wmUrl = ronkyuu.discoverEndpoint(href, test_urls=False)
#             if wmUrl is not None and wmStatus == 200:
#                 print('\tfound webmention endpoint %s for %s' % (wmUrl, href))
#                 status_code = ronkyuu.sendWebmention(sourceURL, href, wmUrl, vouchDomain=vouchDomain)

#                 if status_code == requests.codes.ok:
#                     print('\twebmention sent successfully')
#                 else:
#                     print('\twebmention send returned a status code of %s' % status_code)
