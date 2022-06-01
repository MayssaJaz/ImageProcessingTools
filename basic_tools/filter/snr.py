import math
from histogram.histogram import stat_image
import numpy as np


def SNR(orig_data,new_data):
    mean,var = stat_image(orig_data)

    width,height,image = orig_data[0],orig_data[1],orig_data[3]
    image_new = new_data[3]

    S = 0
    B = 0
    for i in range(height):
        for j in range(width):
            S += (image[i][j] - mean) ** 2
            B += (image_new[i][j] - image[i][j]) ** 2
    if (B == 0):
        return 0.0

    snr = math.sqrt(S / B)
    return snr
