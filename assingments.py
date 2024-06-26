# exersize 1

#[Q1]

# # enter the all variable in one line
# name,age,address = input("Enter Your Name:\n"), int(input("Enter Your Age:\n")), input("Enter Your Address:\n")
# # print the variable by format
# print("my name is {}, I am {}. I live in {}".format(name,age,address))

#[Q2]

# # enter the word from user
# word = input("Enter the word:\n")
# # enter the letter to be checked on word
# letter = input("Enter the letter:\n")
# # conut the letter in word, if the letter not the word return 0 
# # if letter return 0 print false mean the letter is not in word
# print((word.count(letter.upper()) or word.count(letter.lower()))  != 0)

#[Q3]

# # use library math
# import math
# # enter the word from user
# word = input("Enter the word:\n")
# # count the number of letter in the word
# length = len(word)
# # count half of lenght to take half of word
# # ceil() use for ex 2.4 => 3 
# halfLen= math.ceil(length /2)
# # take half the word uppercase and ather half lowercase
# result = word[:halfLen].upper() + word[halfLen:].lower()
# # print the result
# print(result)

#[Q4]

# # enter the word from user
# word = input("Enter the word:\n")
# # minus 3 form length
# halfLen= int( len(word) - 3)
# # last three letter will be uppercase
# result = word[:halfLen].lower() + word[-3:].upper() 
# print(result)

#[Q5]

# # enter the name from user
# name = input("Enter your name:\n")
# #reverse the string that accepted from user and  print it 
# print(name[::-1])

#[Q6]

# use datetime and calendar library
# import datetime
# import calendar
# # take the current year ex => 2023
# current_year = datetime.datetime.now().year
# # take the current month ex => 12
# current_month = datetime.datetime.now().month 
# # this line make every week on nest list
# cal = calendar.monthcalendar(current_year, current_month)
# # count How many list in main list and print it
# print("Number of weeks in this month is",len(cal))

#[Q7]

# # use datetime library 
# import datetime
# # enter your birth day
# date_of_birth = datetime.date(2003,8,16)
# # take current data for today
# current_day = datetime.datetime.now().date()
# # minus current day with date of brith and divided by 356
# print((current_day - date_of_birth).days //365)

#[Q8]

# # enter the name from user
# name = input("enter your name:\n")
# # count the number of letter in thw word and convert it to hex
# print(hex(len(name)))

#[Q9]

# name = "he,ll,o w,or,ld"
# print (name.upper().replace(',',"\n"))

#[Q10]

#First Shape:
# print("   __________ ")
# print("  /          \ ")
# print(" /            \ ")
# print("/              \ ")
# print("\              / ")
# print(" \            / ")
# print("  \__________/ ",)

# #Second Shape:

# print("  ******  ")
# print(" **    ** ")
# print("*  0  0  *")
# print("*    O   *")
# print("*        *")
# print(" **    ** ")
# print("  ******  ")

# #Third Shape:

# print("*")
# print("**")
# print("***")
# print("****")
# print("*****")
# print("******")
# print("*******")
# print("********")
# print("*********")
# print("**********")

############################################################################################

#Exersiec2

#[Q1]

# # enter the Number from user
# number = int(input("enter any Number:\n"))
# # check if even or odd
# if number % 2 ==0 :
#     print(f"the square root of number is: {number ** (1/2)}")
# else:
#     print(f"the cube root of number is: {number ** (1/3)}")

#[Q2]

# # enter an form user
# var = input("enter anything to check if number or string:\n")
# # check type of input number or string 
# if var.isnumeric():
#     # if number 
#     print(f"{var} is number")
# else:
#     # if string
#     print(f"{var} is string")


#[Q3]

# Number  = int(input("Enter number \n"))
# type_Root = int(input("enter type of root for ex: square = 2 or cub = 3:\n"))
# if type_Root <= 0:
#     print("Error try again")
# else:
#     print(Number ** (1/type_Root))

#[Q4]

# # enter the word form user
# word = input("enter the word:\n")
# # check the word has whitespace form begin or the end 
# if word.startswith(" ") or word.endswith(" "):
#     # if the word has whitespace 
#     print("the word has whitespace")
#     # remove whitespace
#     word = word.strip()
# else:
#     # if the word hasn't whitespace 
#     print("the word hasn't whitespace")
# print(word)


#[Q5]

# enter word form user
# isNumber = input("enter the letter with number:\n")
# # loop for all letter in the word
# for i in isNumber:
#     # check if the word has number or not
#     if i.isdigit():
#         print("the word has numbers")
#         # if the word has number don't excute the else loop
#         break
# else:
#     # if the word hasn't number 
#     print("word hasn't numbers")


#######################################################################################
#Exersiec3
# [1]
                   #{for}
# num = int(input("Enter a numner:"))
# #Give it a primitive value
# factorial = 1
# # check if the number is negative, positive or zero   
# if num < 0:    
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num+1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)
                 #{while}
# number = int(input("Enter a number: "))
# factorial = 1
# num = number

# if number > 0:
#     while number > 0:
#         factorial *= number
#         number -= 1
#     print(f"The factorial of {num} is", factorial)
# elif  number <0:
#         print("Sorry, factorial does not exist for negative numbers")
# else:
#         print(f"The factorial of {num} is 1",)


#[2]
                   # # {for}
# Give it a primitive value
# prime = True   
# Number = int(input("Enter a Number:"))
# #if it's equal to zero , it's not a prime Number
# if Number == 0 or Number == 1 : 
#     print(Number,"is not a prime Number") 
# #if it's less than zero
# elif Number < 0:
#     print("Sorry, prime does not exist for negative numbers")
# #if it's grater than zero 
# elif Number> 1: 
#     for i in range(2,Number):
#         if Number % i == 0:
#             prime = False
#             break
#     if not prime:
#         print(Number, "is not prime Number")
#     else:
#         print(Number, "is  prime Number")

#                     #{while}
# prime = True   
# Number = int(input("Enter a Number:"))
# # Check if the input equal to zero or one
# if Number == 0 or Number == 1:
#     print(Number, "is not a prime Number") 
# # Check if the input is negative
# elif Number < 0:
#     print("Sorry, prime does not exist for negative numbers")
# # Check if the input is greater than one
# elif Number > 1:
#     i = 2
#     while i < Number:
#         if Number % i == 0:
#             prime = False
#             break
#         i += 1
#     if not prime:
#         print(Number, "is not prime Number")
#     else:
#         print(Number, "is prime Number")

#[3]
#####################################################
# # [shape 1]
# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# while
# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print("*", end=" ")
#         j += 1 # j = j +1
#     print()
#     i += 1
####################################################

####################################################
# [shape 2]
# for i in range(1,4):
#     for j in range(i):
#         print("*", end=" ")
#     print()
#     if i >=3:
#         i -=1
#         for i in range(2,0,-1):
#             for j in range(i):
#                 print("*", end=" ")
#             print()

# while

# i = 1
# while i <= 3:
#     j = 0
#     while j < i:
#         print("*", end=" ")
#         j += 1
#     print()
#     i += 1
# i = 2
# while i > 0:
#     j = 0
#     while j < i:
#         print("*", end=" ")
#         j += 1
#     print()
#     i -= 1

#################################################

#[shape3]
# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(i,end=" ")
#         i=i-1
#     print()

###################################################

# [4]

            #{for} حلي
# string = input(("Enter to revers: \n"))
# for i in string:
#     print("Reversed string:",string[::-1])
#     break

# # [for]

# word = input("enter the name:\n")
# reversed_word = ""
# for i in range((len(word) - 1), -1, -1):
#     reversed_word += word[i]
# print(reversed_word)

# [while]

# word = input("enter the name:\n")
# reversed_word = ""
# i = len(word) - 1
# while i >=0:
#     reversed_word += word[i]
#     i -=1
# print(reversed_word)


#[5]
# first_Num = int(input("Enter first Number:\n"))
# second_Num = int(input("Enter second Number:\n"))
# odd_Count = 0
# even_Count = 0
# if first_Num<= second_Num:
#     for Number in range(first_Num,second_Num+1):
#         if Number % 2 == 0:
#             even_Count+=1
#         else:
#             odd_Count+=1
#     print("even Numbers are",even_Count)
#     print("odd Numbers are",odd_Count)
# else:
#     for Number in range(first_Num,second_Num-1,-1):
#         if Number % 2 ==0:
#             even_Count+=1
#         else:
#             odd_Count+=1
#     print("even Numbers are",even_Count)
#     print("odd Numbers are",odd_Count)

# fisrt_Num = int(input("enter your frist number:\n"))
# second_Num = int(input("enter your second number:\n"))
# odd_Count = 0
# even_Count = 0
# if fisrt_Num<= second_Num :
#     while fisrt_Num <= second_Num :
#         if fisrt_Num % 2 == 0:
#             even_Count += 1
#         else:
#             odd_Count += 1
#         fisrt_Num +=1
#     print("even Numbers are",even_Count)
#     print("odd Numbers are",odd_Count)
# else:
#     while fisrt_Num>= second_Num:
#         if fisrt_Num % 2 == 0:
#             even_Count+=1
#         else:
#             odd_Count+=1
#         fisrt_Num-=1
#     print("even Numbers are",even_Count)
#     print("odd Numbers are",odd_Count)