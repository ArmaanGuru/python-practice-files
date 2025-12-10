# solving quadratic equation with hepl of python
# The quadratic equation is of the form ax^2+bx+c=0
import cmath
a=float(input('enter value of a:'))
b=float(input('enter value of b:'))
c=float(input('enter value of c:'))
# discriminant
d=b*b-4*a*c
# finding two solutions
root1=(-b-cmath.sqrt(d))/(2*a)
root2=(-b+cmath.sqrt(d))/(2*a)
print('the roots are:',root1,'and',root2)