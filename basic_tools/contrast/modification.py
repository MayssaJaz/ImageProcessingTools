import numpy as np

class Point:
    def __init__(self,x,y,max_n,func):
        self.x = fix_point(x,max_n,func)
        self.y = fix_point(y,max_n,func)
        
def fix_point(x,max_n,func):
    if (x < 0): 
        func(f"{x} not in 0 - {max_n} ( {x} < 0 ) ------> fixing to 0")
        return 0
    if (x > max_n):
        func(f"{x} not in 0 - {max_n} ( {x} > {max_n} ) ------> fixing to {max_n}")
        return max_n
    return x

def check_points(A,B):
    if(A.x < B.x):
        return True
    else: return False

def contrast_modifier(A,B,data):
 
    width,height,max_l,image = data[0],data[1],data[2],data[3]

    new_GL =np.zeros(max_l+1,np.int32)
    for i in range(len(new_GL)):
        if(A.x != 0 ):
            if(i < A.x):
                new_GL[i] = i * (A.y//A.x)

            if(i < B.x):
                new_GL[i] = i * ((B.y - A.y)//(B.x - A.x)) + ( A.y - ((B.y - A.y)//(B.x - A.x)) * A.x )

            if(i >= B.x):
                new_GL[i] = i * ((max_l - B.y)//(max_l - B.x)) + ( B.y - ((max_l - B.y)//(max_l - B.x)) * B.x  )
        elif(A.y != 0):
            if(i <= B.x):
                new_GL[i] = i * ((B.y - A.y)//(B.x - A.x)) + A.y

            if(i > B.x):
                new_GL[i] = i * ((max_l - B.y)//(max_l - B.x)) + ( B.y - ((max_l - B.y)//(max_l - B.x)) * B.x  )
        else:
            if(i <= B.x):
                new_GL[i] = i * (B.y//B.x)

            if(i > B.x):
                new_GL[i] = i * ((max_l - B.y)//(max_l - B.x)) + ( B.y - ((max_l - B.y)//(max_l - B.x)) * B.x  )

    flat_image = image.flatten('C')
    
    for i in range(len(flat_image)):
        if(new_GL[flat_image[i]] > max_l):
            flat_image[i] = max_l
        else:
            flat_image[i] = new_GL[flat_image[i]]

    final_image =np.zeros((height,width),np.int32)
    for i in range(height):
        final_image[i] = flat_image[i*width:width*(i+1)]
    

    return (width,height,max_l,final_image)

