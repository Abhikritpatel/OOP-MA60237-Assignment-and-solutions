import math
from abc import ABC,abstractmethod

class shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    

class circle(shape):
    def __init__(self,radius,pi):
        self.radius=radius
        self.pi=math.pi
        
    def area(self):
        return self.pi*(self.radius**2)
        
        

class rect(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def area(self):
        return self.length*self.breadth
        

class triangle(shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
        
    def area(self):
        return 0.5*self.base*self.height
        

class shapeareacalc():
    
    def calculate_area(self,shape):
        return shape.area()
    
    
def main():
    calculator=shapeareacalc()
    
    while True:
        print("Shape area calculator Menu")
        print("1. Calculate area of circle")
        print("2. Calculate area of rectangle")
        print("3. Calculate area of triangle")
        print("4. Quit")

        choice=input("Enter your choice (1-4): ")

        shape_object=None

        if choice=='1':
            try:
                radius=float(input("Enter the radius of the circle: "))
                shape_object=circle(radius,math.pi)
            except ValueError:
                print("Invalid input. Please enter a numeric value for radius.")

        elif choice=='2':
            try:
                length=float(input("Enter the length of the rectangle: "))
                breadth=float(input("Enter the breadth of the rectangle: "))
                shape_object=rect(length,breadth)
            except ValueError:
                print("Invalid input. Please enter numeric values for length and breadth.")

        elif choice=='3':
            try:
                base=float(input("Enter the base of the triangle: "))
                height=float(input("Enter the height of the triaingle: "))
                shape_object=triangle(base,height)
            except ValueError:
                print("Invalid input. Please enter numeric values for base and height.")

        elif choice=='4':
            print("Exiting the program")
            break

        if shape_object is not None:
            area=calculator.calculate_area(shape_object)
            print(f"The area is {area}")



if __name__=="__main__":
    main()