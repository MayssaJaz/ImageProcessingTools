import numpy as np
import random

def add_noise(data):
    width,height,max_l,image = data[0],data[1],data[2],data[3]
    flat_image = image.flatten('C')
    for i in range(len(flat_image)):
        r = random.randint(0,20)
        if(r == 0):
            flat_image[i] = 0
        elif(r == 20):
            flat_image[i] = max_l
    
    newIMG =np.zeros((height,width),np.int32)
    for i in range(height):
        newIMG[i] = flat_image[i*width:width*(i+1)]

    return (width,height,max_l,newIMG)