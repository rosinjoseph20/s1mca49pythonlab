square=lambda s:s*s
triangle=lambda b,h:0.5*b*h
rectangle=lambda l,w:l*w
s=int(input("enter the side of the square:"))
b=int(input("enter the base of the triangle:"))
h=int(input("enter the height of the triangle:"))
l=int(input("enter the length of the rectangle:"))
w=int(input("enter the width of the rectangle:"))
print("area of square:",square(s))
print("area of the triangle:",triangle(b,h))
print("area of the rectangle:",rectangle(l,w))
