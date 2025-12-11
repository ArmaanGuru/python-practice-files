# program to check a prime number in an interval
lower=int(input('enter lower interval:'))
upper=int(input('enter upper interval:'))
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                print('number is not prime',num)
                break
        else:
            print('number is prime',num)