from binary_filters.dilatation import dilatation
from binary_filters.erosion import erosion


def closing(data,size):
    data_dilat = dilatation(data,size)
    width,height,max_l,ouv_image = erosion(data_dilat,size)

    return width,height,max_l,ouv_image