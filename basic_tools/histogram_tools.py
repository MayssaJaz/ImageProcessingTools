from tools import read_image
import numpy as np


def calculate_histogram(file):
    (_, cols, rows, max_pixels, pixels_data)=read_image(file)
    histogram = np.zeros(int(max_pixels)+1, dtype=object) 
    for i in range (int(rows)):
            for j in range (int(cols)):
                histogram[int(pixels_data[i][j])]=(histogram[int(pixels_data[i][j])])+1
    return histogram

def calculate_cumulative_histogram(file):
    histogram=calculate_histogram(file)
    cumulative_histogram = np.zeros(int(len(histogram)), dtype=object) 
    cumulative_histogram[0]=(histogram[0])
    for i in range (1,len(histogram)):
        cumulative_histogram[i]=cumulative_histogram[i-1]+histogram[i]
    return cumulative_histogram
        

  