#declare your constant
n = 600851475143
i = 2

while n != 1:
    remainder = n%i
    if remainder == 0:
        n = n/i
        print(i)
    else:
        i += 1
    
