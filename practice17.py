# program to print fibonacci series 
num=int(input('enter a number:'))
a,b=0,1
count=0
if num<=0:
    print('please enter a positive integer')
elif num==1:
    print('fibonacci series upto',num,'is:')
    print(a)
else:
    print('fibonacci series upto',num,'is:')
    while count<num:
        print(a)
        c=a+b
        a=b
        b=c    
        count+=1