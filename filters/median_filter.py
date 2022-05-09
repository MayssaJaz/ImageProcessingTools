import sys
import os
import numpy as np
from calculate_frame import calculate_frame
myDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.split(myDir)[0]
sys.path.append(parentDir)
from basic_tools.tools import read_image,write_image


def median_filter(file,height,width):
    (type, cols, rows, max_pixels, pixels_data) = read_image(file)
    filtered_image_pixels= [[0 for c in range(int(cols))] for r in range(int(rows))]

    #applying filter
    for i in range(int(rows)):
        for j in range(int(cols)):
            frame=calculate_frame(i,j,width,height,pixels_data,cols,rows)
            flat_list=frame.flatten()
            median=np.median(flat_list)
            filtered_image_pixels[i][j]=int(median)
    return (type,max_pixels,cols, rows,pixels_data,filtered_image_pixels)