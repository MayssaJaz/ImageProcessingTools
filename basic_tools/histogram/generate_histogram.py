from matplotlib import pyplot as plt
from histogram.cumulitive_histogram import Cumulitive_histogram
from histogram.histogram import histogram


def generate_histograms(data):
    
    fig = plt.figure(figsize=(10, 7))
    rows = 1
    columns = 2

    fig.add_subplot(rows, columns, 1)
    histogram(data)
    plt.title("Histogram")

    fig.add_subplot(rows, columns, 2)
    Cumulitive_histogram(data)
    plt.title("Cumulitive Histogram")

    plt.show()

    