def write_pgm(data,name):
    
    width,height,max_l,image = data[0],data[1],data[2],data[3]

    f = open(name, "w")
    
    f.write("P2\n")
    f.write("# This is my image\n")
    f.write(f"{width} {height}\n")

    flat_image = image.flatten('C')
    
    f.write(f"{max_l}\n")

    for i in flat_image:
        f.write(f'{i} ')

    f.close()

