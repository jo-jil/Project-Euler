import math

def primeFactors(n):
    for i in range(2, int(math.sqrt(n)) + 2, 2):
        # while i divides n , print i and divide n
        #print(i)
        while n % i == 0:
            print(i)
            n = n / i
        else:
            print(n)


#print(int(math.sqrt(600851475143)) + 1, 2)
#print(600851475143 % 775147)
n = 13195
primeFactors(n)
