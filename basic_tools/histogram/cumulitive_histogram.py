from matplotlib import pyplot as plt


def Cumulitive_histogram(data):
    max_l,image = data[2],data[3]
    flat_image = image.flatten('C')
    plt.hist(flat_image, bins = max_l, cumulative = True, histtype = 'step', density = True, color = 'blue')
    plt.xlabel('Grey level')
    plt.ylabel('Cumulitive percentage')
    # plt.show()