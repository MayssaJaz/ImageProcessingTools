import cv2


def read_image(file):
    with open(file, 'r', encoding='utf-8') as f:
        file_list = list(f)
        type = file_list[0]
        i = 1
        while (file_list[i][0] == '#'):
            i = i + 1
        cols_rows_line = file_list[i].split()
        cols = cols_rows_line[0]
        rows = cols_rows_line[1]
        i = i + 1
        max_pixels = file_list[i]
        i = i + 1
        """pixels_array = file_list[i:]
        converted_list = []
        for element in pixels_array:
            converted_list.append(element.strip())
        listToStr = ' '.join([str(elem) for elem in converted_list])
        splittedArray = listToStr.split(' ')
        cleanSplittedArray = [a for a in splittedArray if a not in ['']]
        pixels_data = []
        for row in range(int(rows)):
            pixels_data.append(cleanSplittedArray[int(
                row) * int(cols):int(cols) * (int(row) + 1)])
        """
        pixels_data = []
        for line in file_list[i]:
            pixels_data.extend([int(c) for c in line.split()])
        return (type, cols, rows, max_pixels, pixels_data)


def write_image(name, cols, rows, max_pixels, pixels_data):
    with open('images/readme.ascii.pgm', 'w') as f:
        f.write('P2\n')
        f.write(cols + ' ' + rows + '\n')
        f.write(max_pixels + '\n')
        for i in range(int(rows)):
            f.write(' '.join([str(elem) for elem in pixels_data[i]]) + '\n')
        f.close()
    image = cv2.imread('images/readme.ascii.pgm', -1)
    cv2.imshow("Sheep", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def calculate_average(file):
    pixels_sum = 0
    (_, cols, rows, _, pixels_data) = read_image(file)
    for i in range(int(rows)):
        for j in range(int(cols)):
            pixels_sum = int(pixels_data[i][j]) + pixels_sum
    average = pixels_sum / (int(rows) * int(cols))
    print('The average is equal to', average)
    return (cols, rows, pixels_data, average)


def calculate_standard_deviation(file):
    (cols, rows, pixels_data, average) = calculate_average(file)
    pixels_dev = 0
    for i in range(int(rows)):
        for j in range(int(cols)):
            pixels_dev = pow((int(pixels_data[i][j]) - average), 2) + pixels_dev
    standard_deviation = pixels_dev / (int(rows) * int(cols))
    print('The standard deviation is equal to', standard_deviation)
    return standard_deviation
