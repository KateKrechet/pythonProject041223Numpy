import numpy as np
from PIL import Image

img = np.array(Image.open('city.jpg'))
print(img[0, 0])
imgR = img.copy()
# GB = 0,убираем все цвета, кроме красного, 0 - R,1 - G,2 - B
imgR[:, :, (1, 2)] = 0

img1 = Image.fromarray(imgR)
img1.save('R.png', format='PNG')

imgG = img.copy()
imgG[:, :, (0, 2)] = 0
img1 = Image.fromarray(imgG)
img1.save('G.png', format='PNG')

imgF = img.copy()
imgF[:, :, (1)] = 0
img1 = Image.fromarray(imgF)
img1.save('F.png', format='PNG')

imgGRAY = img.copy()
imgGrayNew = np.mean(imgGRAY, axis=2).astype(np.uint8)
img1 = Image.fromarray(imgGrayNew)
img1.save('Gray.png', format='PNG')

imgGB = img.copy()
imgGB[:160, :90, (0, 2)] = 0
imgGB[160:, 90:, (0, 1)] = 0
imgGB[:160, 90:, (1, 2)] = 0
imgGB[160:, :90, (2)] = 0
# gray_region = np.average(imgGB[320:, :213, :], axis=-1)
# imgGB[320:, :213, :] = np.stack([gray_region] * 3, axis=-1)
img1 = Image.fromarray(imgGB)
img1.save('GB.png', format='PNG')
