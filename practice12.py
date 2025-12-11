# program to find the largest number among three numbers 
num1=int(input('enter first number:'))
num2=int(input('enter second number:'))
num3=int(input('enter third number:'))
if (num1>num2) and(num1>num3):
    print(num1,'no. first is the largest number')
elif(num2>num1)and (num2>num3):
    print(num2,'no. second is the largest number')
else:
    print(num3,'no. third is the largest number')