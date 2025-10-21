import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    area = round(math.pi * radius ** 2, 2) 

    return area
#print(area_of_circle(5))
    
    #return 0.0

# Q2: Hollow Right Triangle

#        n:
#*       0 
#**      1
#* *     2
#****    3

#*       0 
#**      1
#* *     2
#*  *    3
#*****   4



def hollow_right_triangle(n):
    #return ""
   j += ""
   for i in range(n):
    if i == 0:
        j += "*" + "\n"
    elif i == (n - 1):
        j += "*" * n + "\n"
    else:
       j += "*" + (i - 1) * " " + "*" 

    return j
#print(hollow_right_triangle(4))

#             n:
#*******      0
# *****       1
#  ***        2
#   *         3


def inverted_pyramid(n):
    j += ""
    for i in range(n):
       


 
 
 
 print(inverted_pyramid(4))


    
    
    #return ""

# ----------------------------------------------------------------
# print(area_of_circle(5))
# print()

# print(hollow_right_triangle(3))
# print()

# print(hollow_right_triangle(4))
# print()

# print(hollow_right_triangle(5))
# print()

# print(inverted_pyramid(3))
# print()

# print(inverted_pyramid(4))
# print()

# print(inverted_pyramid(5))
# print()