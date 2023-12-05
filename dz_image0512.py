import numpy as np
from PIL import Image

img = np.array(Image.open('cat.jpg'))

imgcat = img.copy()
imgcat[:110, :, (0, 1)] = 0
imgcat[111:220, :, (1, 2)] = 0
imgcat[221:330, :, (0, 2)] = 0

img1 = Image.fromarray(imgcat)
img1.save('cat_mod.png', format='PNG')