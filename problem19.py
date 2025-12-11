# python program to check armstrong number for an interval
lower=int(input('enter lower interval:'))
upper=int(input('enter upper inter val:'))
print('armstrong numbers betwwen',lower,'and',upper,'are:')
for num in range (lower,upper+1):
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        cube=digit**3
        sum=sum+cube
        temp=temp//10
    if num==sum:
        print(num)  

