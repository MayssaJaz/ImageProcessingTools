import numpy as np

def calculate_frame(i,j,width,height,pixels_data,cols,rows):
    filter=(height,width)
    filter = np.zeros(filter) 
    if(i < height -int(height)/2):
        if (j < width):
            for a in range(int(height/2)-i,height):
                for b in range(int(width/2)-j,width):
                    filter[a][b]=pixels_data[a+i-int(height/2)][b+j-int(width/2)]
                    
        elif (j+width < int(cols)+int(width/2)+1):
            for a in range(int(height/2),height):
                for b in range(width):
                    filter[a][b]=pixels_data[a+i-int(height/2)][b+j-int(width/2)]
        else:
            for a in range(int(height/2)-i,height):
                for b in range (int(cols)-j+int(width/2)):
                    filter[a][b]=pixels_data[a+i-int(height/2)][b+j-int(width/2)]
    elif(i+ int(height/2)>int(rows)-1):
        if (j < width):
            for a in range(int(rows)-i+ int(height/2)):
                for b in range (int(width/2)+j+1):
                    filter[a][b-j+int(width/2)]=pixels_data[a+i-int(height/2)][b]           
        elif (j+width < int(cols)+int(width/2)+1):
            for a in range(int(rows)-i+ int(height/2)):
                for b in range(width):
                    filter[a][b]=pixels_data[a+i-int(height/2)][b+j-int(width/2)]
        else:
            for a in range(int(rows)-i+ int(height/2)):
                for b in range (int(cols)-j+int(width/2)):
                    filter[a][b]=pixels_data[a+i-int(height/2)][b+j-int(width/2)]
    else:
        if (j < width):
            for a in range(height):
                for b in range (int(width/2)+j+1):
                    filter[a][b-j+int(width/2)]=pixels_data[a+i-int(height/2)][b]           
        elif (j+width < int(cols)+int(width/2)+1):
            for a in range(height):
                for b in range(width):
                    filter[a][b]=pixels_data[a+i-int(height/2)][b+j-int(width/2)]
        else:
            for a in range(height):
                for b in range (int(cols)-j+int(width/2)):
                    filter[a][b]=pixels_data[a+i-int(height/2)][b+j-int(width/2)]
                    
    return (filter)