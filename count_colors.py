#!/usr/bin/env python

from PIL import Image
import argparse
import pprint

parser = argparse.ArgumentParser()
parser.add_argument('path')
args = parser.parse_args()


im = Image.open(args.path)

pixels = list(im.getdata())
width, height = im.size

print('Loaded image of size %s.' % str(im.size))

color_frequency = {}
# Classify colors.
for pixel in pixels:
  pixel_string = str(pixel[:3])
  if color_frequency.has_key(pixel_string):
    color_frequency[pixel_string] += 1
  else:
    color_frequency[pixel_string] = 1

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(color_frequency)

# Sanity check.
print('Total colors: %d.' % len(color_frequency))
print('[Sanity] Total tiles: %d.' % sum(color_frequency.values()))
