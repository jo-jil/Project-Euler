fib = [1,2,3]
x = 2
t = 0
sum = 2

while(t < 4000000):
    t = (fib[x] + fib[x - 1])
    fib.append(t)
    print(fib[x])
    x = x + 1
    if ((fib[x-1])%2 is 0):
        sum = sum + fib[x-1]
        print("hello")


print(sum)
