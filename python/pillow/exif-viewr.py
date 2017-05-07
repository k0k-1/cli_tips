# example: $ python exif-viewer.py ../img/cicada.jpg

import sys
from PIL import Image, ExifTags

if (len(sys.argv) != 2):
    print ('usage: $ python', sys.argv[0], 'filename')
    quit()

im = Image.open(sys.argv[1])

for key, value in im._getexif().items():
    if key != 37500:
        print ('\033[31m', end='')                          # red
        print (ExifTags.TAGS.get(key, repr(key)), end=':')  # key -> tags
        print ('\033[00m\033[34m', end='')                  # blue
        print (repr(value))                                 # value
        print ('\033[00m', end='')
