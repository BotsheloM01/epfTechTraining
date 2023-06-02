# Problem One
#Declare your constant variable
maximumNo = 1000
#intialize the variable that will be used for incrementing the multiples of these two numbers.
sum = 0
total=0

# finding multiples of 3 or 5 below 1000
for i in range(0,maximumNo):
    if i%3==0 or i%5==0:
        total += i      
print (total)