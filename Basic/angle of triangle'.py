import math
side1=int (input("lenght of AB : "))
side2=int(input("lenght of BC : "))
side3=pow(side1,2)+pow(side2,2)
side4=side3/2
angle=math.atan(side4/side2)
print("angle is : ",angle*(180/3.14))
