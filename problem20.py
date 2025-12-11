# program to sm of natural nmbers
num=int(input('enter a number:'))
if num<0:
    print('please enter a positive number') 
else:
    sum=0
    while num>0:
        sum+=num
        num-=1
    print('the sum is',sum)