#formula : sqrt((x2 - x1)^2 + (y2 - y1)^2).
x1= int(input("enter X1 value"))
x2= int(input("enter X2 value"))
y1= int(input("enter y1 value"))
y2= int(input("enter y2 value"))
result=(((x2-x1)**2 + (y2-y1)**2)**0.5)
print("the distance between two points",(x1,x2),"and",(y1,y2),"=",result)

#2.2
num1=int(input("Enter the first Number"))
num2=int(input("Enter the Second Number"))
sum=num1+num2
print("The Sum of Two numbers is", sum)

#2.3
import sys
sys.argv = ['add.py', '10', '20']
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
print("Sum =", num1 + num2)
