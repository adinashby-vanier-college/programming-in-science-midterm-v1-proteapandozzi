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
   j = ""
   for i in range(n):
    if i == 0:
        j += "*" + "\n"
    elif i == 1:
       j += "**" + "\n"
    elif i == (n - 1):
        j += "*" * n + "\n"
    else:
       j += "*" + (i - 1) * " " + "*" + "\n"

    return j.rstrip()
#print(hollow_right_triangle(5))

#                n:    p:
#*******(7)      0     4
# *****(5)       1     3
#  ***(3)        2     2
#   *(1)         3     1

# pattern = 2p+1
#spaces =i

#output in terminal of this code:
#*******
# *****
#  ***
#   *



def inverted_pyramid(n):
    j = ""
    for i in range(n):
        if n <= 2:
           j += "The pyramid height should be at least 3." + "\n"
           break       
        else:
           j += i * " "
           j += "*" * ((2 * (n - i)) -  1) + "\n"
    
    return j.rstrip()


 
 
print(inverted_pyramid(2))


    
    
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