import sys
import os
import numpy as np
import math
myDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.split(myDir)[0]
sys.path.append(parentDir)
from basic_tools.tools import calculate_standard_deviation


def signal_noise_ratio(file,cols, rows,pixels_data,filtered_image_pixels):
    numerator=calculate_standard_deviation(file)*int(cols)*int(rows)
    denominator=0
    for i in range(int(rows)):
        for j in range (int(cols)):
            denominator=denominator+pow((int(filtered_image_pixels[i][j])-int(pixels_data[i][j])),2)
    result=math.sqrt(numerator/denominator)
    print ("result",result)
    return result

    

    

    
    