
"""For Loop Practice"""

#Print the sum of all even numbers between 1 and 50.



#Print the multiplication table of any number from 1 to 10.

#Print all numbers between 1 and 100 that are divisible by both 3 and 5.

#Print the first 10 square numbers (1, 4, 9, 16, ...).

#Count how many odd numbers are between 1 and 100. """




#for homework
# 1. Print the sum of all the even numbers between 1 and 50       
sum_even = 0 #Start with sum = 0 
for i in range(2,51,2): 
    
    sum_even = sum_even + i # add each number to sum_even (No += used )
    print("sum of even numbers between one and 50:",sum_even) #show the result

    # 2. multiplication table of a number(example: 7)
num = 7       # we want the table of 7
for i in range(1,11): # go through numbers 1 to 10
    print(f"{num} X {i} = {num*i}") #multiply 7 by each number and print
                                    #The f in the front of the string (f" ...") means f-string (formatted string)
                                  # it allows us to mix the text and variables inside the quote.

#3.Numbers divisible by both 3 and 5 between one and 100.
for i in range (1,101): #check numbers from one to one hundred.
    if i % 3 == 0 and i % 5 == 0:    #% means remainder ; if no remainder for 3 and 5 - divisible
        print(i, end=" ") # print the number on the same line.
print()   # new line

#4 first 10 square numbers 
for i in range(1,11):    # numbers 1 to 10
    print(i**2, end=" ") #**2 means multiply by itself  (square)
print ("new line")












#While Loop Practice

#Print numbers from 1 to 20 using while.
i=1 #start from line one.
while i <= 20: #keep looping while i is less than 20.
    print(i) #Show the current value of i.
    i=i + 1 # increase i by one each time.

#Print numbers from 10 down to 1.
i=10 #start from 10 .
while i >= 1: #keep looping while i is atleast 1.
    print(i) #show the current value of i.
    i=i - 1 #decrease i by one each time.


#Keep asking the user to enter numbers until they type 0.
num=int(input("enter a number(0 to stop):")) # Ask the user for a number
while num !=0: #Repeat as longis not 0
    print("you entered:",num) #show the number is not 0
    num=int(input("enter an number(0 to stop):")) #askes again

#Print the sum of digits of a number (e.g., 123 → 6).
num=int(input("enter a number:"))#ask for a number 
sum_digits=0 #start total sum at 0
while num > 0: #repeat until the number becomes 0
    digit=num % 10 #remove th last digit (remainder after /10)
    sum_digits=sum_digits + digit # add the digit to the sum
    num=num//10 #remove the last digit (integer division)- it is showing only the integer part-ignores the decimal part.
print("Sum of digits:", sum_digits)




