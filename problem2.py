#intialization
first= 0
second= 1
temporary = 0
sum = 0

#this will generate all the numbers in the sequence that are less than 4000000 and calculate the sum of the even numbers
while temporary < 4000000:
    temporary = first + second
    first = second
    second = temporary
     
     #calculate the sum of all the even numbers
    if temporary%2==0:
       sum += temporary
       
       
# display the sum of all the even numbers
print("the sum of all even numbers = " + str(sum)) 
    
       
    
        
