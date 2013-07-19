#!/usr/bin/env python2
import flickr_api
import os
import sys

dir = os.path.dirname(__file__)
flickr_api.set_auth_handler(os.path.join(dir, 'auth'))

def perror(string):
  sys.stderr.write(string + '\n')

def upload(name):
  if not os.path.exists(name):
    perror('file %s doesn\'t exist\n' % name)
    sys.exit(2)

  path = os.path.abspath(name)
  tags = ', '.join(os.path.dirname(path).replace(',', '_').strip('/').split('/'))

  try:
    flickr_api.upload(photo_file = path, tags = tags, is_public = 0, is_friend = 0, is_family = 0)
    perror('included tags: %s\n' % tags)
  except:
    sys.exit(3)



# test
if len(sys.argv) != 2:
  print '''upload.py file'''
  sys.exit(1)

upload(sys.argv[1])
