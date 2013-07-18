#!/usr/bin/env python2
import flickr_api
import os
import sys

dir = os.path.dirname(__file__)
flickr_api.set_auth_handler(os.path.join(dir, 'auth'))

def upload(name):
  if not os.path.exists(name):
    print 'file %s doesn\'t exist\n' % name
    sys.exit(2)
  
  print 'starting upload of %s\n' % name
  
  path = os.path.abspath(name)
  tags = ', '.join(os.path.dirname(path).replace(',', '_').strip('/').split('/'))
  
  print 'included tags: %s\n' % tags
  
  flickr_api.upload(photo_file = path, tags = tags, is_public = 0, is_friend = 0, is_family = 0)
  
  print 'file uploaded\n'



# test
if len(sys.argv) <= 1:
  print '''upload.py file1 file2 ...'''
  sys.exit(1)

for name in sys.argv[1:]:
  upload(name)
