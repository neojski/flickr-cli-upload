flickr-cli-upload
=================
Simple script to let me upload tons of photos into flickr and organize them automatically in the following fashion:

./upload.py /home/me/photos/vacation/poland/cracov/happy.jpg

Will create image happy.jpg with tags:
  home me photos vacation poland cracov

Images will be private by default.

dependencies
============
[python-flickr-api](https://github.com/alexis-mignon/python-flickr-api)

usage
=====
1. run ./authorize.py
2. you can now use ./upload.py
