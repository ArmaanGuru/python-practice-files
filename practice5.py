# python program to swap two numbers with using third variable
x=float(input('enter value of x:'))
y=float(input('enter value of y:'))
temp=x
x=y
y=temp
print('value of x after swapping:',x)
print('value of y after swapping:',y)
# python program to swap two numbers without using third variable
x=23
y=43
x,y=y,x
print('value of x is:',x)
print('value of y is:',y)