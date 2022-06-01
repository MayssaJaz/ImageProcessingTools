from binary_filters.dilatation import dilatation
from binary_filters.erosion import erosion


def opening(data,size):
    data_eros = erosion(data,size)
    width,height,max_l,ouv_image = dilatation(data_eros,size)
    
    return width,height,max_l,ouv_image
