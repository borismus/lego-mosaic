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
  pixel_string = pixel[:3]
  if color_frequency.has_key(pixel_string):
    color_frequency[pixel_string] += 1
  else:
    color_frequency[pixel_string] = 1

pp = pprint.PrettyPrinter(indent=2)

# Sanity check.
print('Total colors: %d.' % len(color_frequency))
print('[Sanity] Total tiles: %d.' % sum(color_frequency.values()))
items = color_frequency.items()
items = sorted(items, key=lambda item: item[1])

pp.pprint(items)

# Create a new image that is a stacked bar chart of just the colors.
width = len(items)
height = max(color_frequency.values())
im2 = Image.new('RGB', (width, height), 'white')

pixels = im2.load()
for i in range(im2.size[0]):
  for j in range(im2.size[1]):
    if (j < items[i][1]):
      pixels[i, j] = items[i][0]

im2.show()
