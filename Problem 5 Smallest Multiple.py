test = False
j = 2520
l = 0
ans = 0
while test is False:
    if(j%2 == 0):
        for i in range(1,21):
            if (j%i) == 0:
                l = l +1
        if l == 20:
            test = True
            ans = j
    j = j + 2520
    l = 0
print(ans)
