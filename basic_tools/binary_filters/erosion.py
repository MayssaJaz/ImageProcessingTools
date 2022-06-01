import numpy as np


def erosion(data, size):
    if (size % 2 == 0):
        size += 1
        
    width,height,max_l,image = data[0],data[1],data[2],data[3]

    border = size//2
    newIMG =np.zeros((height,width),np.int32)
    for i in range(height):
        newIMG[i] = image.flatten('C')[i*width:width*(i+1)]
    
    for i in range(border,height-border):
        for j in range(border,width-border):
            pixels = []
            for k in range(i-border,i+border+1):
                for f in range(j-border,j+border+1):
                    pixels.append(image[k][f])
            pixels.sort()
            if(pixels[pow(size,2) - 1] == 255):
                newIMG[i][j] = 255 

    return width,height,max_l,newIMG