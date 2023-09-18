#Data Types

#Strings - data type of characters put together >> in order to pull a character from a string use []
#Pulling character from string is called subscripting >> CAN ONLY BE DONE WITH STRINGS
print("Hello"[0])
# "123" is treated as a string of characters not as numbers
print("123" + "345")

#Number data type - Integers >> replace commas with underscore >> 100,000 > 100_000
print(123 + 345)
print(100_000 + 1)

#Number data type - Float > decimal numbers
3.123

#Number data type - Boolean - Only has "True" and "False"
True
False

#You can only concatenate a string to another string > not to an interger -- below won't work
num_char = len(input("What is your name?"))
# print("Your name has " + num_char + " characters.")
#This will give you an error >> type error

#type function will tell if it is character, interger or something else.
(type(num_char))  #This will tell you it is an 'int'

#typecasting is changing a peice of data from one type to another
num_char = len(input("What is your name?"))
new_num_char = str(num_char)
("Your name has " + new_num_char + " characters.")

#This will print 170.5 > we converted string 100.5 to float and added it to an int.
(70 + float("100.5"))

#Mathematical operations >> Follows PEMDAS ()
3 + 5
6 - 2
3 * 2  #multiply
6 / 3  #divide
2**2  #2^2 - exponents

#This will print 7
(3 * 3 + 3 / 3 - 3)

#This will print 3
(3 * (3 + 3) / 3 - 3)

#Use round function to round the number 
#Use round (8/3, 2) to round it down to 2 decimal places
(round(8/3,2))

#Use // as substitute to int 
(8 // 3)

#Use += or -= or *= or /= to add or divide existing variable to result in new variable
#Instead of doing score = 0 >> score = score + 1 
score = 0 
score += 1
print(score)

#f-strings >> use 'f' in front of the double quotes and use variables in curly brackets 
score = 0 
height = 1.8
isWinning = True 
print(f"Your score is {score} and your height is {height} and your winning is {isWinning}")
