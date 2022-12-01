import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2
import matplotlib.image as mpimg
import time
import threading as th

def sample_function():
    args = sys.argv

    print(args[0])

    for i in range(10):
        img = cv2.imread("OIP{0}.png".format(i),0)
        cv2.imwrite('OIPgray{0}.png'.format(i), img)

start = time.time()           # 測定開始
sample_function()
elapsed = time.time() - start # 測定終了

print(f"{elapsed * 1000:.1f} ms")  