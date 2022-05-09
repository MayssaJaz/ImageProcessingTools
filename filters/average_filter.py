import sys
import os
import numpy as np
from calculate_frame import calculate_frame
myDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.split(myDir)[0]
sys.path.append(parentDir)
from basic_tools.tools import read_image,write_image


def average_filter(file,height,width):
    (type, cols, rows, max_pixels, pixels_data) = read_image(file)
    filtered_image_pixels= [[0 for c in range(int(cols))] for r in range(int(rows))]

    #applying filter
    for i in range(int(rows)):
        for j in range(int(cols)):
            frame=calculate_frame(i,j,width,height,pixels_data,cols,rows)
            filtered_image_pixels[i][j]=int( int(np.average(frame)))
    write_image(type, cols, rows, max_pixels, filtered_image_pixels)
                        
            
    
average_filter("images/mona_lisa.ascii.pgm",5,5)