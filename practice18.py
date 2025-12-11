
# python program to check armstrong number
num=int(input('enter a number:'))
sum=0
temp=num
while temp>0:
    digit=temp%10
    cube=digit**3
    sum=sum+cube
    temp=temp//10
if num==sum:
    print(num,'it is an armstrong number')
else:           
    print(num,'it is not an armstrong number')