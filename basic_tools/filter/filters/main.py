
import sys
import os
myDir = os.path.dirname(os.path.abspath(__file__))
parentDir = os.path.split(myDir)[0]
sys.path.append(parentDir)
from median_filter import median_filter
from random_filter import random_filter
from average_filter import average_filter
from basic_tools.tools import write_image
from signal_noise_ratio import signal_noise_ratio 

(type,max_pixels,cols, rows,pixels_data,filtered_image_pixels)=average_filter('images/mona_lisa.ascii.pgm',5,5)
write_image(type,cols,rows,max_pixels,filtered_image_pixels)
signal_noise_ratio('images/mona_lisa.ascii.pgm',cols, rows,pixels_data,filtered_image_pixels)
(type,max_pixels,cols, rows,pixels_data,filtered_image_pixels)=median_filter('images/mona_lisa.ascii.pgm',5,5)
signal_noise_ratio('images/mona_lisa.ascii.pgm',cols, rows,pixels_data,filtered_image_pixels)


