# class circle:
#     pi =3.14
#     def __init__(self,radius):
#         self.radius = radius
#     def area_of_circle(self):
#         return self.pi*self.radius*self.radius

# num = int(input("enter the number for checking a area of circle: "))
# circle_1 =circle(num)
# print("area of circle is : ",circle_1.area_of_circle())

class recatangle:
    def __init__(self,h,l):
        self.l =l
        self.h = h
    def area_of_rectangle(self):
        area = self.l*self.h
        return area

num_1=int(input("enter the height of rectangle: "))
num_2=int(input("enter the length of rectangle: "))
recatngle_1 = recatangle(num_1,num_2)
print("area of rectangle : ",recatngle_1.area_of_rectangle())
