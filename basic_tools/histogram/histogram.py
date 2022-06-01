import numpy as np
import matplotlib.pyplot as plt
import math



def stat_image(data):

    image = data[3]
    flat_image = image.flatten('C')

    mean = np.mean(flat_image)
    var = np.var(flat_image)

    return (mean,var)

def histogram(data):
    image = data[3]
    flat_image = image.flatten('C')
    plt.hist(flat_image,bins=data[2])
    plt.xlabel('Grey level')
    plt.ylabel('Number of points')
    # plt.show()

def entropy(data):
    width,height,max_l,image = data[0],data[1],data[2],data[3]
    nb_pixels = height*width
    ent = 0
    hist = [0] * (max_l + 1)
    for h in range(height):
        for w in range(width):
            hist[image[h][w]] += 1
    
    for g in range(max_l + 1):
        p = hist[g] / nb_pixels
        if (p != 0):
            ent += p * math.log2(1 / p)
    return ent