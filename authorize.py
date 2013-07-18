#!/usr/bin/env python2
import flickr_api

flickr_api.set_keys(api_key = '9dc2e46ce1e917d3f2ef09b087b80fc5', api_secret = '56349739605a5e37')

a = flickr_api.auth.AuthHandler(callback='oob')
perms = 'write'
url = a.get_authorization_url(perms)
print url

accepted = 'n'
while accepted.lower() == 'n':
  accepted = raw_input('Have you authorized me? (y/n) ')
  oauth_verifier = raw_input('What is the PIN? ')

#set the oauth_verifier token
a.set_verifier(oauth_verifier)
a.save('auth', include_api_keys=True)

print a.access_token # debug
