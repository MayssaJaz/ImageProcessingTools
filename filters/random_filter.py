from random import randint
import sys
import os
myDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.split(myDir)[0]
sys.path.append(parentDir)
from basic_tools.tools import read_image,write_image

def random_filter(file):
    (type, cols, rows, max_pixels, pixels_data) = read_image(file)
    modified_pixels = [[0 for i in range(int(cols))] for j in range(int(rows))]
    print(len(modified_pixels))
    for i in range (int(rows)):
            for j in range (int(cols)):
                random_number=randint(0, 20)
                if (random_number ==0):
                    modified_pixels[i].append(0)
                elif (random_number == 20):
                    modified_pixels[i].append(255)
                else:
                    modified_pixels[i].append(pixels_data[i][j]) 
    return (type,max_pixels,cols, rows,pixels_data,modified_pixels)
    
            
                
    

