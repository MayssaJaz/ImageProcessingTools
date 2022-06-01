from histogram_tools import calculate_histogram
from tools import read_image
import numpy as np
import math


def egalisation_histogram(file):
    (_, cols, rows, max_pixels, pixels_data)=read_image(file)
    histogram = calculate_histogram(file)
    p = np.zeros (int(len(histogram)), dtype=object)
    for i in range (int(len(histogram))):
        p[i]=(histogram[i])/(int(cols)*int(rows))
    p_accumulés=np.zeros(int(len(histogram)), dtype=object)
    p_accumulés[0]=p[0]
    for i in range (1,int(len(histogram))):
        p_accumulés[i]=(p_accumulés[i-1])+p[i]
    #hp=(int(cols)*int(rows))/(int(max_pixels)+1)
    a = np.zeros (int(len(histogram)), dtype=object)
    n1 = np.zeros (int(len(histogram)), dtype=object)
    histogram_egalise = np.zeros (int(len(histogram)), dtype=object)
    for i in range (int(len(histogram))):
        a[i]=(int(max_pixels))*p_accumulés[i]
        n1[i]=math.floor(a[i])
        histogram_egalise[n1[i]]+=histogram[i]
    return histogram_egalise

    
    
    
    