import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def readPGM(path,originalIMG):
    try:
        f = open(path, 'r')
        t = f.readline()
    except UnicodeDecodeError:
        f = open(path, 'rb')
        t = f.readline().decode()
    if t == 'P2\n':
        lines = f.readlines()
        for l in list(lines):
            if l[0] == '#':
                lines.remove(l)
    
        width,height =[int(c) for c in lines[0].split()]
        max_l = int(lines[1])
        data = []
        for line in lines[2:]:
            data.extend([int(c) for c in line.split()])
    
        image =np.zeros((height,width),np.int32)
        for i in range(height):
            image[i] = data[i*width:width*(i+1)]
        data= width,height,max_l,image

    elif t == 'P5\n':
        while True:
            line = f.readline()
            if line[0] != '#':
                break

        width,height =[int(c) for c in line.split()]
        max_l = int(f.readline())
        data = []
        byte = f.read(1)
        while byte:       
            data.append(ord(byte))
            byte = f.read(1)
    
        image =np.zeros((height,width),np.int32)
        for i in range(height):
            image[i] = data[i*width:width*(i+1)]
        
        plt.imshow(Image.fromarray(image)) # Usage example

        data= width,height,max_l,image

    else:
        print("can't read file !")
        return False

    originalIMG.setData(data[0], data[1], data[2],data[3], path)

