import sys
import os
import numpy as np
from calculate_frame import calculate_frame
myDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.split(myDir)[0]
sys.path.append(parentDir)
from basic_tools.tools import read_image,write_image

def high_pass_filter(file,height,width):
    filter=[[0,1,0],[1,5,1],[0,1,0]]
    (type, cols, rows, max_pixels, pixels_data) = read_image(file)
    filtered_image_pixels= [[0 for c in range(int(cols))] for r in range(int(rows))]
    for i in range(int(rows)):
        for j in range(int(cols)):
            frame=calculate_frame(i,j,width,height,pixels_data,cols,rows)
            for a in range(height):
                for b in range(width):
                    filtered_image_pixels[i][j]=filtered_image_pixels[i][j]+int(frame[a][b])*filter[a][b]
    write_image("P2", cols, rows, max_pixels, filtered_image_pixels)
                        
            
            
            
                        
                        
                       
                                            
            

        

    
high_pass_filter("images/mona_lisa.ascii.pgm",3,3)