import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2
import matplotlib.image as mpimg

args = sys.argv

print(args[0])

img = mpimg.imread(args[1])
plt.imshow(img)
plt.show()

