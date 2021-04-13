#!/bin/env python
# -*- coding: utf-8 -*-
"""Python example running inside a virtual environment."""


print('Image processing using PIL (pillow) and numpy of an image downloaded with requests')
from PIL import Image, ImageFilter
import requests
import numpy as np
from io import BytesIO
import os
import sys

url = 'https://upload.wikimedia.org/wikipedia/commons/b/b6/Image_created_with_a_mobile_phone.png'
response = requests.get(url)
inim = Image.open(BytesIO(response.content))
print('Read image from URL: %s' % url)

print('Downsize image to width 256')
width = 256
height = int(width * (inim.height / inim.width))
im = inim.resize((width, height))

print('Edge detection')
edges = im.filter(ImageFilter.FIND_EDGES)

print('Pixellating image')
# Resize down to width 32 using BILINEAR interpolation
width = 64
height = int(width * (im.height / im.width))
small = im.resize((16,16), resample=Image.BILINEAR)
# Scale up using NEAREST interpolation
pixellated = small.resize(im.size, Image.NEAREST)

print('Converting image to grey scale')
gray = im.convert('L')

print('Stacking all images into a numpy array and saving as a PIL image')
out = Image.fromarray( np.hstack( [im, edges, pixellated, gray.convert('RGB')] ) )

outfile = os.path.dirname(__file__) + '/out.png'
if not os.path.exists(outfile):
    out.save(outfile)
    print('Wrote file out.png')
else:
    print('Error: outfile already exists ... skipping writing file')

print('')


print('Computing geographic distances between cities using haversine package')
import haversine

cph_latlon = (55.676, 12.568)
rome_latlon = (41.903, 12.496)
cph_rome_dist_km = haversine.haversine(cph_latlon, rome_latlon)

print('Distance between Copenhagen and Rome (in a straight line) is %i km' % cph_rome_dist_km)
print('')


print('Computing the time of next time Mars rises in London in using ephem and pytz (for local time)')
import ephem
import pytz

mars = ephem.Mars()
london = ephem.Observer()
london.lat = '51.510'
london.lon = '-0.118'
rising_utc = london.next_rising(mars).datetime().replace(tzinfo=pytz.utc)
setting_utc = london.next_setting(mars).datetime().replace(tzinfo=pytz.utc)
print('Mars rises next time in London at %s UTC' % rising_utc)
print('Mars sets next time in London at %s UTC' % setting_utc)
print('Mars rises next time in London at %s (local time)' % rising_utc.astimezone(pytz.timezone('Europe/London')))
print('Mars sets next time in London at %s (local time)' % setting_utc.astimezone(pytz.timezone('Europe/London')))
