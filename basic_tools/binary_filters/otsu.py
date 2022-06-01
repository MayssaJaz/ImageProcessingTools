import numpy as np
def otsu(data):
    width,height,max_l,image = data[0],data[1],data[2],data[3]

    flat_image = image.flatten("C")

    pixel_number = width * height
    mean_weigth = 1.0/pixel_number

    his, bins = np.histogram(flat_image, np.array(range(0, max_l+1)))
    final_thresh = -1
    final_value = -1
    for t in bins[1:-1]:
        Wb = np.sum(his[:t]) * mean_weigth
        Wf = np.sum(his[t:]) * mean_weigth

        mub = np.mean(his[:t])
        muf = np.mean(his[t:])

        value = Wb * Wf * (mub - muf) ** 2

        if value > final_value:
            final_thresh = t
            final_value = value
    
    final_image = flat_image.copy()
    final_image[flat_image > final_thresh] = 255
    final_image[flat_image < final_thresh] = 0
    newIMG =np.zeros((height,width),np.int32)
    for i in range(height):
        newIMG[i] = final_image[i*width:width*(i+1)]

    return width,height,max_l,newIMG
