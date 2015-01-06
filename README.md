Indieweb
========

A Flask Application to test/explore Indieweb features

Currently the following Indieweb items are implemented:

* [Webmention](http://indiewebcamp.com/webmention)
  * Receive inbound webmention
  * Vouch stub
* [Micropub Endpoint](http://indiewebcamp.com/micropub)
  * Handle an inbound Micropub event
* [Token Endpoint](http://indiewebcamp.com/token-endpoint)
  * Verify a given access token is valid
  * Generate an access token
* [IndieAuth Login](http://indiewebcamp.com/indieauth)
  * Supports using indieauth.com as an authorization service


To run locally:
    python indieweb.py --logpath . --port 9999 --host 127.0.0.1 --config ./indieweb.cfg

Contributors
============
* bear (Mike Taylor)

Requires
========
Python v2.7+ but see requirements.txt for a full list
