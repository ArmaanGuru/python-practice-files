# program to display multiplication table of a given number
num=int(input('enter a number:'))
for i in range(1,11):
    print(f'{num}x{i}={num*i}')
# with while loop
num=int(input('enter a number:'))
i=1
while i>=10:
    print(f'{num}x{i}={num*i}')
    i+=1