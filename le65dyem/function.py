import numpy as np
import ipywidgets import interact, fixed
import PIL  import Image

def imshow(X, resize = None):
    
    img = Image.open(X)
    
    
    wpercent = (resize/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    
    img.show()
    
    
ipywidgets.interact(imshow, resize=(0,2000))