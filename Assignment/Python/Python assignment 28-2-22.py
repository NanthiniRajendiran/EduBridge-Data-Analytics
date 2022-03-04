#!/usr/bin/env python
# coding: utf-8

# # python assingment

# # 1. write a python class named circle constructed by a radius  and two method which will compute the area and the perimeter of a circle
# 
# 

# # class Circle():
#     def __init__(self, r):
#         self.radius = r
# 
#     def area(self):
#         return self.radius**2*3.14
#     
#     def perimeter(self):
#         return 2*self.radius*3.14
# 
# NewCircle = Circle(8)
# print(NewCircle.area())
# print(NewCircle.perimeter())

# # 2.write a  python class named rectangle constructed by a length and width and a method which will compute the area of a triangle

# In[2]:


class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width
newRectangle = Rectangle(int(input()),int(input())
print(newRectangle.rectangle_area())


# # 3.write a python class which has two methods get_string and print_string.get_string accept a string from the user and print_string the string in upper case

# In[4]:


class IOString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input()

    def print_String(self):
        print(self.str1.upper())

print("Type in a statement and this program will make it upper case!")

str1 = IOString()
str1.get_String()
str1.print_String()


# In[ ]:




