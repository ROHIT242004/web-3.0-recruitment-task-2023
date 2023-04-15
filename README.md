## Introduction

Name- Rohit

---
220909

---
Student of Mechanical Engineering

---
Intrested in learning tech and clicking pictures

---
Hometown- Rewari

---
The class maade by me is in python language.

## explanation
at first we declare a class Car which includes properties of a car such as name,model,speed in x ,speed in y etc. in 3d dimension.
```python
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
```
After this we make function 'speed_increment' which increases the speed in one frame and takes acceleration of different directions as input as (ax,ay,az)
```python
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
```

The same goes for speed decrement function

---
Then the next step is to make the 'move()' function. which takes self as input and moves the car by one frame according to the provided velocity and changes the coordinates.
```python
def move(self):
        self.x_coor = self.x_coor + self.speed_x
        self.y_coor = self.y_coor + self.speed_y
        self.z_coor = self.z_coor + self.speed_z
```
Our next function is 'detect_collision' which returns "True" if all the coordinates are same as updated by move or as they were in the class simuntaneously.Else it returns "False".
```python
def detect_collision(self,c2):
        if self.x_coor == c2.x_coor and self.y_coor == c2.y_coor and self.z_coor == c2.z_coor:
            return True
        return False
```
At last we define a function which returns the time of cars colliding if these do else it does not return anything. we take the absolute value of the relative distance in each direction and divide it by absolute value of the relattive speed of the corresponding direction and if all these values are equal then we return the value of any one of these else wee return nothing.
```python
def time_to_collision(self,c2): 
        a=(abs(self.x_coor-c2.x_coor))/abs((self.speed_x-c2.speed_y))
        b=(abs(self.y_coor-c2.y_coor))/abs((self.speed_y-c2.speed_y))
        b=(abs(self.z_coor-c2.z_coor))/abs((self.speed_z-c2.speed_z))      
        if a==b:
            return a
```

