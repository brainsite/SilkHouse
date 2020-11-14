import os
from PIL import Image


def my_thumbnail(uri):
    # http://matthiaseisen.com/pp/patterns/p0202/
    path = '.' + uri
    folder, filename = os.path.split(path)
    thumbnail_path = os.path.join(folder, 'thumbnail.jpg')

    original = Image.open(path)
    # width, height = original.size
    # left = width/4
    # top = height/4
    # right = 3 * width/4
    # bottom = 3 * height/4
    left = 0
    top = 0
    right = 100
    bottom = 100

    cropped_example = original.crop((left, top, right, bottom))
    cropped_example.save(thumbnail_path)
