import numpy as np
from collections import Counter

def Histogram_egalisation(data):
    width,height,max_l,image = data[0],data[1],data[2],data[3]

    new_val = width * height // max_l 
    flat_image = image.flatten('C')
    counter_image = Counter(flat_image)

    H_n =np.zeros(max_l+1,np.int32)
    for i in range(max_l+1):
        H_n[i] = counter_image[i]

    P_n = np.zeros(max_l+1,np.float16)
    for i in range(max_l+1):
        P_n[i] = H_n[i]/(width * height)

    Pc_n = np.zeros(max_l+1,np.float16)
    Pc_n[0] = P_n[0]
    for i in range(1,max_l+1):
        Pc_n[i] = Pc_n[i-1]+P_n[i]

    Hp_n = [new_val] * (max_l+1)

    A = np.zeros(max_l+1,np.float16)
    for i in range(max_l+1):
        A[i] = max_l * Pc_n[i]
    
    n1 =  np.zeros(max_l+1,np.int16)
    for i in range(max_l+1):
        n1[i] = int(A[i])
    
    newIMG =np.zeros(height*width,np.int32)
    for i in range(len(flat_image)):
        newIMG[i] = n1[flat_image[i]]
    
    final_image =np.zeros((height,width),np.int32)
    for i in range(height):
        final_image[i] = newIMG[i*width:width*(i+1)]

    return (width,height,max_l,final_image)