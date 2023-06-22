def find_smallest_multiple():
    multiple = 1
    for i in range(1,20):
        if multiple % i != 0:
            j = 2
            while j <= 20:
                if (multiple * j) % i == 0:
                    multiple *= j
                    break
                print(multiple)
                j += 1
    return multiple
result = find_smallest_multiple()
print("the smallest positive number that is evenly divisible by numbers from 1 to 20 is " + str(result))          