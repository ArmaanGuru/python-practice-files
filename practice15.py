# program to find the factorial of number
num=int(input('enter a number:'))
if num<0:
    print('factorial doea not exsist for negative number s')
elif num==0:
    print('the factorial of o is 1')
else:
    factorial=1
    for i in range(1,num+1):
        factorial=factorial*i
    print('the factorial of num ',num,'is',factorial)
