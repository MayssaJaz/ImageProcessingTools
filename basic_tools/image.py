
class ImageModel: 
    
    def __init__(self):
        self.isread = False
    
    def setData(self,width,height,gray_level,data,file_name):
        self.width = width
        self.height = height
        self.gray_level = gray_level
        self.file_name = file_name
        self.data = data

    def setAttributes(self,width,height,gray_level,data):
        self.width = width
        self.height = height
        self.gray_level = gray_level
        self.data = data

    def set_is_read(self,isread):
        self.isread = isread
    
    def get_data(self):
        return (self.width,self.height,self.gray_level,self.data)

    def get_num_pixels(self):
        return self.width * self.height
    
    