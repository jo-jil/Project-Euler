# This function will return true if its a palindrome and false otherwise
def palin(x,y): 
    num_string = str(x*y)
    reverse_num = ''
    for i in range(0,len(num_string)):
        reverse_num = num_string[i] + reverse_num
    if(reverse_num == num_string):
        return True
    else:
        return False

# This function starts at the highest numbers of i and j and decrements down until there is a valid palindrome
# Then it returns the product of them, which will be the largest palindrome
def check():
    for i in reversed(range(100,1000)):
        for j in reversed(range(100,1000)):
            #Check to see if its a valid palindrome
            if(palin(i,j)):
                return(i*j)
                
                
# Calls the function check which will run through all permutations until there is a valid palindrome
print(check())
