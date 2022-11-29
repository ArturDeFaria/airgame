import cv2 as cv
import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
from skimage import io

img = Image.open('pessoa.jpeg')
convertImagem= img.resize((92,92), Image.BILINEAR)
img=convertImagem.resize(img.size, Image.NEAREST)
img2= ImageOps.grayscale(img)

i1= io.imread(img)

plt.imshow(i1)
#cv.imshow("sd",img)
#cv.waitKey(0)








