
class Car:

    def __init__(self, name, model, mfg_year, speed_x, speed_y,speed_z, x_coor, y_coor, z_coor):
        self.name = name
        self.model = model
        self.mfg_year = mfg_year
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.speed_z = speed_z
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.z_coor = z_coor

    def speed_increment(self, ax, ay, az):
        if self.speed_x >= 0 :
           
            self.speed_x = self.speed_x + ax
        else:   
            self.speed_x = self.speed_x - ax
        if self.speed_y >= 0 :    
            self.speed_y = self.speed_y + ay
        else:
            self.speed_y = self.speed_y - ay
        if self.speed_z >= 0 : 
             self.speed_z = self.speed_z + az
        else:   
            self.speed_z = self.speed_z - az   
    def speed_decrement(self, ax, ay, az):
        if self.speed_x >= 0 :
           
            self.speed_x = self.speed_x - ax
        else:   
            self.speed_x = self.speed_x + ax
        if self.speed_y >= 0 :    
            self.speed_y = self.speed_y - ay
        else:
            self.speed_y = self.speed_y + ay
        if self.speed_z >= 0 :
           
            self.speed_z = self.speed_z - az
        else:   
            self.speed_z = self.speed_x + az    
    def move(self):
        self.x_coor = self.x_coor + self.speed_x
        self.y_coor = self.y_coor + self.speed_y
        self.z_coor = self.z_coor + self.speed_z

    def detect_collision(self,c2):
        if self.x_coor == c2.x_coor and self.y_coor == c2.y_coor and self.z_coor == c2.z_coor:
            return True
        return False
    
    def walls(self, Width, Height):
        if self.x_coor < 0 or self.x_coor > Width:
            self.speed_x *= -1
        if self.y_coor < 0 or self.y_coor > Height:
            self.speed_y *= -1
    def time_to_collision(self,c2): 
        a=(abs(self.x_coor-c2.x_coor))/abs((self.speed_x-c2.speed_y))
        b=(abs(self.y_coor-c2.y_coor))/abs((self.speed_y-c2.speed_y))
        b=(abs(self.z_coor-c2.z_coor))/abs((self.speed_z-c2.speed_z))      
        if a==b:
            return a

















