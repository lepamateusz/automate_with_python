#! /usr/bin/python3

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = '/path/to/logo'

#Fixed size of logo
logoIm = Image.open(LOGO_FILENAME)
print('Resizing %s...' % (logoIm))
logoIm = logoIm.resize((int(0.2*SQUARE_FIT_SIZE),int(0.2*SQUARE_FIT_SIZE)))
logoWidth, logoHeight = logoIm.size

#folder with photos with logo
os.makedirs('withLogo', exist_ok=True)
#Loop over all files in cwd

for filename in os.listdir('.'):
    if (len(filename.lower().split(".")) != 2):
        continue
    if (filename.lower().split(".")[1] not in ['png', 'jpg', 'gif', 'bmp']) or (filename == LOGO_FILENAME):
    #if not (filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.gif') or filename.endswith('.bmp') ) or filename == LOGO_FILENAME:
        continue
    #skip non-image files and the logo file itself

    im = Image.open(filename)
    width, height = im.size

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE or height > SQUARE_FIT_SIZE:
        #new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE


    # Resize the image.
    print('Resizing %s...' % (filename))
    im = im.resize((width, height))

    #print("Logo size: " + str(logoWidth), str(logoHeight))
    #print("Image size "+ str(im.size))

    # Add logo.
    print('Adding logo to %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    # Save changes:
    im.save(os.path.join('withLogo', filename))
