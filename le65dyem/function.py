import numpy as np
from ipywidgets import interact, fixed
from PIL  import Image

def imshow(X, resize = None):
    ##resize is the basewith of the new picture
    img = Image.open(X)
    
    if resize is None:
        img.show()
    else:
        wpercent = (resize/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))

        img = img.resize((resize,hsize), Image.ANTIALIAS)

        img.show()
    
    
interact(imshow, X= 'somepicture',resize=(0,1000))