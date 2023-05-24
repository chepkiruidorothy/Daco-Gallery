
from io import BytesIO
from django.core.files import File
from PIL import Image
from colorthief import ColorThief


SQUARE_IMG_SIZE = (600,600)
LANDSCAPE_IMG_SIZE = (600,400)
PORTRAIT_IMG_SIZE = (480,600)




def resize_image(image, quality):
    """
        resizes and reduces image quality.
    """
    im = Image.open(image)
    im_width, im_height = im.size
    size = None

    if im_width == im_height:
        #image is a square
        size = SQUARE_IMG_SIZE
    if im_width > im_height:
        #image is landscape
        size = LANDSCAPE_IMG_SIZE
    if im_width < im_height:
        # image is portrait
        size = PORTRAIT_IMG_SIZE


    im = im.convert('RGB') # convert mode to RGB so we an use JPEG later
    im = im.resize(size, Image.ANTIALIAS)  # resize image
    thumb_io = BytesIO() # create a BytesIO object
    im.save(thumb_io, 'JPEG', quality=quality, progressive=True, optimize=True) # save image to BytesIO object
    new_image = File(thumb_io, name=image.name) # create a django friendly File object

    return new_image

def get_dominantcolor(image):
    color_thief = ColorThief(image)
    # get the dominant color
    dominant_color = color_thief.get_color(quality=1)
    return dominant_color
