import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2
import matplotlib.image as mpimg
import time

args = sys.argv

print(args[0])

for i in range(10):
    img = cv2.imread("OIP{0}.png".format(i),0)
    cv2.imwrite('OIPgray{0}.png'.format(i), img)