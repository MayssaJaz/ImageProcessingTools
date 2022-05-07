from tools import read_image,write_image,calculate_average,calculate_standard_deviation
from histogram_tools import calculate_histogram,calculate_cumulative_histogram
import matplotlib
matplotlib.use('tkagg')
import numpy as np
import matplotlib.pyplot as plt

(type, cols, rows, max_pixels, pixels_data) = read_image("images/mona_lisa.ascii.pgm")
write_image(type, cols, rows, max_pixels, pixels_data)
calculate_average("images/mona_lisa.ascii.pgm")
calculate_standard_deviation("images/mona_lisa.ascii.pgm")
histogram=calculate_histogram("images/mona_lisa.ascii.pgm")
print(histogram)
calculate_cumulative_histogram("images/mona_lisa.ascii.pgm")
x = np.array(range(0, 256))
plt.title("Histogram")
plt.xlabel("Grayscale")
plt.ylabel("Number of pixels")
plt.plot(x, histogram, color = "red", marker = "o", label = "Array elements")
plt.legend()
plt.show()
cumulative_histogram=calculate_cumulative_histogram("images/mona_lisa.ascii.pgm")
print(cumulative_histogram)
calculate_cumulative_histogram("images/mona_lisa.ascii.pgm")
x = np.array(range(0, 256))
plt.title("Cumulative Histogram")
plt.xlabel("Grayscale")
plt.ylabel("Number of pixels")
plt.plot(x, cumulative_histogram, color = "purple", marker = "o", label = "Array elements")
plt.legend()
plt.show()
