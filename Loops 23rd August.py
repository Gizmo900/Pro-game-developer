#print 50 to 100
#for loop
for i in range(50,101):  #creates a loop variable i that takes values 50, 51, …, 100.
                        #range(start, stop) includes start (50) and excludes stop (101), 
                        # so it ends at 100.
    
    print(i)
    
#while loop
counter = 60 # starts a counter at 50.
while counter<=100:
    print (counter)
    counter = counter+1 #increases the counter by 1 so the loop progresses
                        # and eventually stops at 101.

#search the number
numbers = [3,78,90,32,57] #defines a list of integers
search=int(input("Enter the number you want to search "))

for i in range(len(numbers)): # loops over indices i = 0, 1, 2, 3, 4
                              # len() is a built-in function that returns the length of an object
    if search==numbers[i]:
        print("The number is present at index ",i)
        break # exits the for loop immediately after the first match.

else: #(aligned with the for, not the if) is a loop-else: 
      # it runs only if the loop completes without hitting break (i.e., no match found).
        print("The number is not present")    

     



