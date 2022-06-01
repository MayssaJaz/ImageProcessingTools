import numpy as np


def average_filter(data, size):
    if (size % 2 == 0):
        size += 1
    filt = np.ones((size,size),np.int32)

    width,height,max_l,image = data[0],data[1],data[2],data[3]
    avg = 1 / pow(size,2)
    border = size//2
    newIMG =np.zeros((height,width),np.int32)
    for i in range(height):
        newIMG[i] = image.flatten('C')[i*width:width*(i+1)]

    for i in range(border,height-border):
        for j in range(border,width-border):
            sum_l = 0
            for k in range(i-border,i+border+1):
                for f in range(j-border,j+border+1):
                    sum_l += newIMG[k][f] * filt[k - i][f - j]    
           
            newIMG[i][j] = int(sum_l * avg) 
            
    
    for i in range(height):
        if(i < border):
            for j in range(width):
                newIMG[i][j] = 0
                newIMG[height - i -1][j] = 0
        else:
            for j in range(border):
                newIMG[i][j] = 0
                newIMG[i][width - j  -1] = 0
    return width,height,max_l,newIMG