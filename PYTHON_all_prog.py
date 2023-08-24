#TASK 0.
print("TASK 0") 
print("Output what is the day today in format  year-month-day  ") 
from datetime import datetime
current_datetime = datetime.now()
print(f"Today is {current_datetime.year} — {current_datetime.month} — {current_datetime.day} ") 


#TASK 1.
print("\n \ n \n TASK 1")
print("What version of Python do we use now?")
#!python --version
print("What are the Zen of Python?")
import this


#TASK 2.
print("\n \ n \n TASK 2")
print("Could you from one long word improvement get another word environment? Output the length of this new word.")
word = "improvement"
print(word)
new_word = word[6] + word[-2] + word[5] + word[0] + word[3] + word[4] + word[-2] + word[7] + word[8] + word[9] + word[-1]
print(new_word)
print(len(new_word))


#TASK 3.
print("\n \ n \n TASK 3")
print("Output a greeting for somebody")
A = input ("Input the surname: ")
B = input ("Input the name: ")
H=" "
C=A+H+B
print(f"I’m so glad to see you, Dear {C}!")


#TASK 4.
print("\n \ n \n TASK 4")
print("Output 10 times the sum of two  numbers А and B")
A=int(input("Input the first number: "))
B=int(input("Input the second number: "))
print((str(A+B)+" ")*10)


#TASK 5.
print("\n \ n \n TASK 5")
print("Let’s to see, how to work function PRINT: output the type of entered data; output the entered data three times in a row and then in a column; output the result of multiplying the favorite number by three ")
number=input("Input your favorite number: ")
print(type(number))
print("Output the entered data three times in a row ")
print((str(number)+" ")*3)
print("Output the entered data three times in a column ")
print((str(number)+"\n")*3)
а = input("What is the type of entered data? Write YES, if it’s the number")
if а == "YES":
 print("The result of multiplying your favorite number by three is ")
 print(int(number)*3)
else:
 print("It’s mistake! It’s impossible to multiply the entered data by three ! It’s not number!")


#TASK 6.
print("\n \ n \n TASK 6")
print("Swap two numbers")
a=input("Input the first number: ")
b=input("Input the second number: ")
a,b=b,a
print(a,b)


#TASK 7.
print("\n \ n \n TASK 7")
print("Ask your son, his homework was done or not.")
A = input("Have you already done your homework? YES?")
if A == "YES":
 print("Excellent! You can go for a walk!")
else:
 print("You must do it today! If it’s hard, answer me. I try to help you.")


#TASK 8.
print("\n \ n \n TASK 8")
print("You could buy an icecream only, if you want it and if you have money for it. Check these conditions. ")
A = input("Do you want an icecream? YES?")
if A == "YES":
 B = input("Do you have enough money for it? YES?")
 if B == "YES":
  print("Excellent! You could buy it!")
 else:
  print("You cannot buy an icecream: you haven’t got enough money for it. ")
else:
 print("You cannot buy an icecream, because you don’t want it!")


#TASK 9.
print("\n \ n \n TASK 9")
print("Output the sum of all numbers from 1 to 100")
sum=0
for i in range(1,101):
 sum = sum + i
print(sum)


#TASK 10.
print("\n \ n \n TASK 10")
print("Output the sum of three different numbers ")
A,B,C=input(),input(),input()
print(A,"+",B,"+",C,"=")
print(int(A)+int(B)+int(C))


#TASK 11.
print("\n \ n \n TASK 11")
print("Ask someone a question about broccoli, whether they like to eat it or not. And give advice depending on the received answer. ")
name=input("What is your name?  ")
broccoli=input("Do you like to eat broccoli? YES?")
if broccoli=="YES":
  print(f" {name} likes to eat broccoli. Excellent! ")
else:
  print(f" {name} doesn’t like to eat broccoli. But you need! It’s healthy vegetable!")


#TASK 12.
print("\n \ n \n TASK 12")
print("Count the sum of the two numbers 2 and 8 and check the answer.")
A = input("How many will it be? \n 2+8 =    ")
if A=="10":
  print("It’s correct answer! Excellent!")
else:
  print("Your answer is wrong! Try again.")


#TASK 13.
print("\n \ n \n TASK 13")
print("Ask one beautiful girl if she wants to go to the cinema with you or not. And depending on the answer, that you’ve received from her, say her a few words.")
A = input("Would you like to go out with me? YES? Answer me, please. ")
if A == "YES":
  B = input("Would you like to go to the cinema? YES? Answer me, please. ")
  if B == "YES":
    print("I will buy the cinema tickets and 5 bars of chocolate for you!!!")
  else:
      print("I will buy 15 roses for you!!!")
else:
 print("What a pity! But it’s not a problem - I'll invite someone else.")


#TASK 14.
print("\n \ n \n TASK 14")
print("A visitor comes to a popular nightclub. At the entrance, every guest is asked for a password and, depending on the answer received from the guest, they determine whether he is invited, as well as the status of the guest: regular or VIP.")
password = "LOVE"
elit_password = "NOVEMBER"
user_password = input("If you want to come in, you should enter the PASSWORD: ")
if user_password == password:
  print("\n It's ok. You could come in. We're happy to see you!!!")
elif user_password == elit_password:
  print("\n You are VIP. I'll call your own manager!!! ")
else:
  print("\n It's a wrong password! You couldn't come in. Try again!!! ")


#TASK 15.
print("\n \ n \n TASK 15")
print("A visitor comes to a popular nightclub. At the entrance, every guest is asked for a password of the month. Now it’s May. But the April’s password is still valid. Depending on the answer received from the guest, determine whether he can come in or not.")
password_may = "GREEN"
password_april = "RED"
user_password = input("If you want to come in, enter the password of the month:   ")
if user_password == password_may or user_password == password_april:
  print("You are welcome! We are happy to see you! ")
else:
  print("The password is wrong. Try again. ")


#TASK 16.
print("\n \ n \n TASK 16")
print("A visitor comes to a popular nightclub. At the entrance, each guest is asked to enter two passwords. Depending on the answers received from the guest, he can pass only in one case: both answers must be correct.")
password1 = "BED"
password2 = "TABLE"
user_password1 = input("Enter the first password:   ")
user_password2 = input("Enter the second password:   ")
if user_password1 == password1 and user_password2 == password2:
  print("You are welcome! We are happy! ")
else:
  print("You are wrong. You can’t pass here today. ")


#TASK 17.
print("\n \ n \n TASK 17")
print("Enter a word, whose first letter is M and the last letter is A. Check the entered word, whether it meets these both conditions or not ")
user_word = input("Enter the word     ")
if user_word[0] == "M" and user_word[-1] == "A":
  print("This is a word, that I want!")
else:
  print("Your word is wrong! Try again")


#TASK 18.
print("\n \ n \n TASK 18")
print("Enter a word, whose first letter is M or whose the last letter is A. Check the entered word, whether it meets one of these two conditions or not ")
user_word = input("Enter the word     ")
if user_word[0] == "M" or user_word[-1] == "A":
  print("This is a word, that I want!")
else:
  print("It is wrong word! Try again")


#TASK 19.
print("\n \ n \n TASK 19")
print("Enter a number that is divisible by three without remainder and in addition, the length of this number is also divisible by three without remainder. Check the entered number whether it meets these both conditions or not ")
A = input("Enter a number:   ")
if int(A) % 3 == 0 and len(A) % 3 == 0:
  print("This is a number, that I want!")
else:
  print("It is wrong number! Try again")


#TASK 20.
print("\n \ n \n TASK 20")
print("I came up with a number. Which one is it? Try to guess it. You have two attempts. ")
A = input("Enter your number:   ")
if A != "33":
  print("My number is not this! You have only one attempt now.")
  B = input("Enter your number again:   ")
  if not(B!= "33"):
    print("Excellent! You were able to guess my number!")
  else:
    print("You haven’t got any attempts now. Next one! Who will guess my number?")
else:
  print("Excellent! You were able to guess my number!")


#TASK 21.
print("\n \ n \n TASK 21")
print("You have a piece of Laura Numeroff's fairy tale. If you give a little mouse a cookie, he will definitely ask you for milk. If you give him milk, he will ask you to give him a straw. If you give him a straw, the little mouse will immediately ask you to give him a white napkin. Input, what this little mouse has already asked you, and output, what then he will ask you. ")
A = input("This is a little mouse. What does he want just now? Enter: MILK, STRAW or NAPKIN? \n ")
if A == "MILK":
  print("And then the little mouse will ask to give him: STRAW  ")
elif A == "STRAW":
  print("And then the little mouse will ask to give him: NAPKIN  ")
elif A == "NAPKIN":
  print("And then the little mouse will ask to give him: MILK  ")  
else: 
  print("And then the little mouse will ask to give him… I don’t know! Let’s ask him about!")


#TASK 22.
print("\n \ n \n TASK 22")
print(" There are seven days in each week. 1 — Monday. 2 — Tuesday. 3 — Wednesday. 4 — Thursday. 5 — Friday. 6 — Saturday. 7 — Sunday. Input a number from 1 to 7 and output, whether it is a working day or a weekend. ")
B = int(input("Input a number for the day of the week - from 1 to 7: "))
if B == "6" or B == "7":
  print("It’s a weekend!!!")
elif B > 0 and B < 8:
   print("It’s a working day.") 
else:
   print("You are wrong. There are 7 days in each week.") 


#TASK 23.
print("\n \ n \n TASK 23")
print("Enter any number and output the result, this number is greater than ten, less than ten or equal to ten. ")
C = int(input("Enter any number  "))
if C > 10:
  print("Your entered number is greater than ten. ")
elif C == 10:
  print("Your entered number is ten!!!")
else:
  print("Your entered number is less than ten. ")    


#TASK 24.
print("\n \ n \n TASK 24")
print("I came up with a number. Enter your number and output the result: your number is bigger than mine, smaller than mine. Try to guess what number I came up with. ")
M=53
while C != M: 
 C = int(input("Enter any number "))
 if C > M:
  print("The entered number must be reduced. ")
 elif C < M:
  print("The entered number must be increased. ") 
 elif C == M: 
  print("You have guessed the number I came up with!!!") 
 else:
  print("It’s mistake! Try again.") 


#TASK 25.
print("\n \ n \n TASK 25")
print("Output all the numbers from 6 to 36 in increments of 3 ")
for i in range(6,37,3):
 print(i)


#TASK 26.
print("\n \ n \n TASK 26")
print("I came up with a word. You will display your variants of my word until you guess which word I came up with.")
my_word = "STOP"
a = input("Input your variant of my word: ")
while a != my_word: a = input("Input your variant of my word: ")
print("Excellent! You have guessed my word!")


#TASK 27.
print("\n \ n \n TASK 27")
print(" You find yourself in a strange forest with a path branching in two directions. \n One path leads to a dark castle with a sinister reputation, \n and the other leads to mysterious ruins \n that are believed to have magical powers. \n Which path would you choose? \n The plot changes depending on your answer.")
D = input("Scary music... \n You find yourself in a strange forest with a path branching in two directions. \n Where will you go: to the right or to the left? Or maybe you’ll go straight home? \n Input: RIGHT, LEFT or HOME   ")

if D == "RIGHT":
 print(" This path leads to a dark castle with a sinister reputation.\n")

 M = input("You are near the dark castle. What are you going to do? \n Have you decided to enter the castle or go around? \n Or maybe you’ll go straight home? Scared? \n Input: IN, AROUND or HOME   ")
 if M == "IN":
  print(" And then you meet a snow-white white .... \n \n \n \n \n \n GHOST!!!")

  X = input("What are you going to do? \n Have you decided to escape immediately or to talk to a ghost? \n Or maybe you’ll go straight home? Scared? \n Input: ESCAPE, TALK or HOME   ")
  if X == "ESCAPE":
   print(" The ghost got angry. It chased you until you feel down... Ha-ha-ha — Now you will become like me - A ghost!!!")
  elif X == "TALK":
   print(" You've been polite to me. You didn't run away. \n \n \n \n \n ...And I will give you life. You will stay alive and even be able to return home. \n\n But never tell anyone about me! \n")
  elif X == "HOME":
   print(" The doors slammed shut. Why did you come here?! You will stay here forever!!! \n")
  else:
   print(" There is no such way here. You are lost in the deep cold damp dungeon of the castle... \n")

 elif M == "AROUND":
  print(" You find the door... It's not locked. Strange. The door opened itself up to you. \n\n You are coming in... \n And a lot of torches are flashing around. \n\n And a terrible voice sounds: \n - You are a 1001 traveler. And I'm giving you a big bag with gold coins.!!!!. \n")
 elif M == "HOME":
  print(" You can't budge. Why did you come here?! \n")
 else:
  print(" There is no such way here. \n You are falling into a bottomless abyss... \n")

elif D == "LEFT":
 print(" This path leads to mysterious ruins \n that are believed to have magical powers.. \n")

 Y = input("What are you going to do? \n Have you decided to climb a tall old tower or take a walk through an abandoned cemetery? \n Choose! \n Or maybe you’ll go straight home? Scared? \n Input: TOWER, CEMETERY or HOME   ")
 if Y == "TOWER":
  print(" Climbing to the top of the tower - you do not see the ruins - no! You see the city in all its splendor, as if you are in the past.")
 elif Y == "CEMETERY":
  print(" There are many ghosts around you! Don’t be afraid. They want to tell you more about your own future. \n")
 elif Y == "HOME":
  print(" You fell deep down into a fast mountain river. The waters carry you swiftly away... Why did you come here?! \n")
 else:
  print(" There is no such way here. \n You are lost in a deep, dense, scary forest…  \n")

elif D == "HOME":
 print(" Right! Why the adventure… \n I'd better go home. I'll lie on the couch and watch a scary movie. \n")

else:
 print(" There is no such way here. \n You are trapped in a swamp...")


#TASK 28.
print("\n \ n \n TASK 28")
print("Input, what products do you need to buy in the shop. And make the shopping list. If that’s enough, the stop-word will be STOP  ")
list = []
C=input("What products do you need to buy in the shop?")
while C!="STOP":
 list.append(C)
 C=input("What products do you need to buy in the shop?")
print(list)


#TASK 29.
print("\n \ n \n TASK 29")
print("Output the list of the even numbers which are more than null.")
list = []
C = input("Input the number more than null  ")
while int(C) > 0: 
 if int(C) % 2 == 0:
  list.append(C)
 else:
  print("It’s uneven number and I won’t add it in the list!") 
 C=input("Input the number more than null  ")
print("The end!!! \n You’ve printed the number which NOT more than null  \n You can see the list of uneven numbers now!!! ")
print(list)


#TASK 30.
print("\n \ n \n TASK 30")
print("You have a list \n  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]. \n Output all numbers of that list, which are less than five.  \n Make the output in a column, in a line separated by commas and separated by a space, and also in the form of a new list ")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for each in a:
 if int(each) < 5:
  print(each)

print("\n ")
b =[]
for each in a:
 if int(each) < 5:
  b.append(each)
print(" ".join(map(str,b)))
print("\n ")
print(str(b).strip('[]'))

print("\n ")
c =[]
for each in a:
 if int(each) < 5:
  c.append(each)
print(c)


#TASK 31.
print("\n \ n \n TASK 31")
print("Find and output the area and the perimeter of a right triangle by two given cathets.")
A = int(input("Output the length of the first cathet   "))
B = int(input(" Output the length of the second cathet   "))
C = (A*A + B*B) ** (0.5)
P = A + B + C
S = A * B * 0.5
print(f" The hypotenuse’s length of your triangle is:  {round(C,3)}")
print(f"The perimeter of your triangle is:  {round(P,3)}")
print(f"The area of your triangle is:  {round(S,3)}")


#TASK 32.
print("\n \ n \n TASK 32")
print("We have a list of numbers. Output the sum of all these numbers.")
number_list = [1,24,400,303,23,33,44,4]
print(number_list)

sum_1 = number_list[0] + number_list[1] + number_list[2] + number_list[3] + number_list[4] + number_list[5] + number_list[6] + number_list[-1]
print(f"The first way to solve: {sum_1}")

sum_2 = 0
for each in number_list:
  sum_2 = sum_2 + each
print(f"The second way to solve: {sum_2}")

def number(A,B,C,D,E,F,G,H):
  sum_3 = A+B+C+D+E+F+G+H
  print(f"The third way to solve: {sum_3}")
number(1,24,400,303,23,33,44,4)

sum_4 = 0
for i in range(0,8):
  sum_4 = number_list[i]+sum_4
print(f"The fourth way to solve: {sum_4}")

sum_5 = sum(number_list)
print(f"The fifth way to solve: {sum_5}")


#TASK 33.
print("\n \ n \n TASK 33")
print("We have a guest list, where are the different people. \n guest_list = [jedi, jedi,jedi, sith, jedi]. \n The jedi is a good person, but the sith is not. \n So if you find the word JEDI in guest list, you will output OK. \n But if you find in the guest list the word SITH, you will output BE CAREFUL. I HAVE FOUND THE ENEMY. \n How many jedi are in the guest list? ")
guest_list = ["jedi", "jedi","jedi", "sith", "jedi"]
A = 0
for i in range(0,5):
 if guest_list[i] == "sith":
  print(f"Number {i} - BE CAREFUL. I HAVE FOUND THE ENEMY.")
 else:
  A = A + 1
  print("OK")
print(f"There are {A} jedis in the guest list")


#TASK 34.
print("\n \ n \n TASK 34")
print("In our task, the Siths have only red swords, the Jedis have only blue, and ordinary people go without swords. \n At the entrance, while the word STOP is not written yet, data is submitted, each from a new line. Input: RED, BLUE or NOONE. Output data on, how many siths, jedis and ordinary people are here in total")
print("You are welcome. I’ll help you to count.")
print(" The siths have only red swords, the jedis have only blue, and ordinary people go without swords. \n At the entrance, while the word STOP is not written yet, data is submitted, each from a new line. Input: RED, BLUE or NOONE. \n")
A = 0
red = 0; blue = 0; noone = 0
while A != "STOP":
  A = input()
  if A == "RED": 
    red = red + 1
  elif A == "BLUE": 
    blue = blue + 1
  elif A == "NOONE":
    noone = noone + 1
  else:
    print("Mistake!!! You are wrong. Continue.")
print(f"Total: \n The siths - {red} with red swords \n The jedis - {blue} with blue swords \n The ordinary people - {noone} without any swords \n ")  


#TASK 35.
print("\n \ n \n TASK 35")
print("One hero's jump in the game is equal to 5 meters. Enter how many jumps the hero decided to make in the game, and output the total length by which the hero will jump from the start point. ")
E = int(input("How many jumps did the hero decide to make in the game?  "))
H = 0; J = 5
for i in range(1,E+1):
 H = J * i
 print(f"The hero’s {i} jump: the total length from the start point is {H} meters.")


#TASK 36.
print("\n \ n \n TASK 36")
print("Write a function that outputs greetings for the guests of the Klub.")
def print_name(name):
 print(f"Hello! Have a nice evening! Nice to see you, {name} !!!")
def print_parname(name1, name2):
 print(f"Hello! Have a nice evening! Nice to see you, {name1} and {name2} !!!")

print_name("Anna")
print_name("Peter")
print_name("Kristina")
print_name("Viktor")
print_name("Alex")
print_name("Eva")
print_parname("Oleg", "Viktoria")
print_parname("Aleksey", "Olga")
print_parname("Fillip", "Varvara")


#TASK 37.
print("\n \ n \n TASK 37")
print("Write a function Calculator with four basic operations.")
def calc(A, B, C):
  if C == "+":
   D = A + B
  elif C == "-":
   D = A - B
  elif C == "*":
   D = A * B 
  elif C == "/":
   D = A / B
  else:
   print("You are wrong. Try again.")
  print(f" Answer: {A} {C} {B} = {D} ") 

A = int(input("Input the first number "))
B = int(input("Input the second number "))
C = input("Input the operation sign: +, -, /, * ")
calc(A,B,C)


#TASK 38.
print("\n \ n \n TASK 38")
print("We need to know many sums of many numbers. Write the function.")
def sum_ab(A,B):
 C = A + B
 print(f"{A}+{B}={C}")

sum_ab(5,6)
sum_ab(4,86)
sum_ab(15,62)
sum_ab(43475,8634)


#TASK 39.
print("\n \ n \n TASK 39")
print("Write the division function with remainder.")
def div_1(A, B):
 C = A // B
 return(C)
def div_2(A, B):
 D = A % B
 return(D)

A = int(input("Input a divisible   "))
B = int(input("Input a divisor   "))
div_1(A, B)
div_2(A, B)
print(f"  The result of dividing a number {A} by a number {B} is {div_1(A, B)}. \n  And the remainder is {div_2(A, B)} \n  {A} / {B} = {div_1(A, B)}({div_2(A, B)})")


#TASK 40.
print("\n \ n \n TASK 40")
print("We have a kingdom that has three bridges. Only the king passes over the first bridge, a knight or a lady-in-waiting passes over the second bridge, and everyone else passes over the third bridge. Write a code that takes in who is passing through. And displays information on which bridge you need to send the cart")
bridge_input = input("Who is passing in the cart? Input KING, KNIGHT, LADY or somebody else you see")
if bridge_input == "KING":
 print("The cart should pass through the bridge № 1")
elif bridge_input == "KNIGHT" or bridge_input == "LADY":
 print("The cart should pass through the bridge № 2")
else:
 print("The cart should pass through the bridge № 3")


#TASK 41.
print("\n \ n \n TASK 41")
print("Write a function that takes a string and outputs it in reverse order. ")
def string_reverse(new_string):
 C = ""
 for each in new_string[-1::-1]:
  C = C + each
 print(f"Output this string in reverse order:   {C}")

new_string = input("Input the string:   ")
string_reverse(new_string)


#TASK 42.
print("\n \ n \n TASK 42")
print("Write a function that takes two arguments: a string and a character. The function should return the number of occurrences of a character in a string. ")
def N_fun(string,character):
 N=0
 for n in range(0,len(string)):
  if string[n] == character:
    N=N+1
 return(N) 

string=input("Input the string: ")
character=input("Input the character: ")
Y=N_fun(string,character)
print(f"The number of occurrences of a character in a string: {Y}")


#TASK 43.
print("\n \ n \n TASK 43")
print("Write a function that takes a list of strings and returns the longest string from the list and its length ")
def max_len(list_stroki):
 max_len = 0
 for each in list_stroki:
  if len(each) > max_len:
    max_word = each
    max_len = len(each)
 print(f"The longest string from the list - {max_word}")
 return(max_len)

list_stroki = ["apple","cherry","broccoli"] 
print(f" The length of the longest string from the list is {max_len(list_stroki)} letters")


#TASK 44.
print("\n \ n \n TASK 44")
print("Write a function that takes a list of numbers and checks if there are duplicate numbers in the list. ")
def check_list_number(list_number):
 l = len(list_number)
 n = 0
 for each in list_number:
   for j in range(n+1,l):
     if list_number[j] == each:
      return(True)
   n = n + 1
 return(False)

list_number_1 = [2,20,78,4,44,9,6,6] 
list_number_2 = [2,20,78,4,44,9,7,6]
print(f"The list is {list_number_1}")
print(f"Are there duplicate numbers in this list? \n {check_list_number(list_number_1)}")
print(f"The list is {list_number_2}")
print(f"Are there duplicate numbers in this list? \n {check_list_number(list_number_2)}")

#TASK 45.
print("\n \ n \n TASK 45")
print("Write a function that takes a list of numbers and prints to the screen the number of numbers that are greater than the arithmetic mean of all the numbers in the list.")
def fun_printing(list_number):
 C = 0
 for each in list_number:
  C = C + each
 B = C/len(list_number)
 print(f"The arithmetic mean of all the numbers in the list - {B}") 
 n = 0
 for each in list_number:
  if each > B:
   n = n + 1 
 return(n) 

list_number = [22,52,41,45,31,36]
print(f"The list - {list_number}")
print(f"The number of numbers that are greater than the arithmetic mean - {fun_printing(list_number)}")


#TASK 46.
print("\n \ n \n TASK 46")
print("Make new word from another.")
word = "definition"# symbols numbers 0,1,2,3... 10 or -9,-8...-2,-1
print(word[3:9:2]) # from symbol № 3 to symbol № 8 with step 2
print(word[3::-1]) # from symbol № 3 to the beginning but all symbols in the reverse order
print(word[3::3]) # from symbol № 3 to the end with step 3
print(word[::-1]) # all the word from end to beginning - in the reverse order
print(word[::-2]) # all the word from end to beginning but with step 2
print(word[7:]) # we don't see the first 7 symbols, only last
print(word[:5]) # we see only the first 5 symbols, not others
print(word[:2]+word[4:6]+word[8:]) # we take first 2 symbols, then symbols №4 and №5,and then last 2 symbols at the end (without 8 first symbols)


#TASK 47.
print("\n \ n \n TASK 47")
print("Create the Class about the cat. What’s the name? And what does the cat do during the day?")
class Cat():
  def meow(self):
    print("Meow  " * 10)
  def sleep(self):
    print("The cat sleeps on the self. ")  
  def walk(self):
    print("The cat walks in the garden.")  
  def rat(self):  
    print("The cat catches the big rat. ")
  def milk(self):
    print("The cat drinks milk") 
  def Cat_name(self,New_Name):
    self.name = New_Name  
  def print_Cat_name(self):
    print(f"The cat’s name is {self.name}")   

New_Cat = Cat()
New_Cat.Cat_name("Milka")
New_Cat.print_Cat_name()
New_Cat.meow()
New_Cat.sleep()
New_Cat.walk()
New_Cat.walk()
New_Cat.walk()
New_Cat.rat()
New_Cat.milk()
New_Cat.meow()
New_Cat.sleep()


#TASK 48.
print("\n \ n \n TASK 48")
print("Create the Class about the dog. What’s the name? And what does the dog do during the day?")
class Dog():
  def bark(self):
    print("Woof "*5)
  def run(self):
    print("The dog runs in the garden")
  def bite(self):  
    print("The dog wants to bite you.")
  def Dog_name(self,new_name):    
    self.name = new_name
  def print_Dog_name(self):  
    print(f"The dog’s name is {self.name}")

New_Dog = Dog()
New_Dog.Dog_name("Sharik")
New_Dog.print_Dog_name()
New_Dog.bark() 
New_Dog.run()
New_Dog.bite() 
New_Dog.bite()  
New_Dog.bark() 
New_Dog.run()
New_Dog.bark()


#TASK 49.
print("\n \ n \n TASK 49")
print("What could you tell me about your dog?")
class Dog():
  def __init__(self,name,breed,color):
    self.breed = breed
    self.name = name
    self.color = color
  def print_info(self):
    print(f"The dog’s name - {self.name}")  
    print(f"The dog’s breed - {self.breed}")  
    print(f"The dog’s color - {self.color}\n\n") 

Name1 = Dog("Artemon","poodle","blue")     
Name1.print_info()
Name2 = Dog("Alina","retriever","black")     
Name2.print_info()
Name3 = Dog("Marta","spaniel","orange")     
Name3.print_info()


#TASK 50.
print("\n \ n \n TASK 50")
print("Create the Class Student that has the attributes name, age and marks. The marks should be a list. Add the method, which calculates the student's average rate.")
class Student():
  def __init__(self,name,age,marks):
   Sum_marks = 0
   for each in (marks):
    Sum_marks += each
   Average_rate = Sum_marks/(len(marks))
   self.Average_rate = Average_rate 
   self.name = name
   self.age = age
   self.marks = marks

  def average_rating(self):
    print(f"Student Name: {self.name}\n")
    print(f"Student Age: {self.age}\n")
    print(f"Student's marks: {self.marks}\n")
    print(f"Student Average Rating: {self.Average_rate}\n\n\n")

alla_marks = [5,4,5,5,2,3,4,2,5,3,4,5]
greg_marks = [5,2,3,5,5,3,4,2,5,4,3,5]
kamilla_marks = [5,5,4,3,5,5,2,3,5,4,4,5]
Alla = Student("Alla Vatutina","21 years",alla_marks)
Greg = Student("Greg Shadow","22 years",greg_marks)
Kamilla = Student("Kamilla Snow","22 years",kamilla_marks)
Alla.average_rating()
Greg.average_rating()
Kamilla.average_rating()


#TASK 51.
print("\n \ n \n TASK 51")
print("Create the Class Worker, which has the attributes name, amount of salary and position. Add the premium size of salary, which takes the percentage of the premium bonus and calculates the amount of the premium bonus depending on the worker's amount of salary. Each worker has own the percentage of the premium bonus")
class Worker():
 def __init__(self,name,amount,position):
   self.name = name
   premium_percent = int(input(f"Input the percentage of the premium bonus  for {self.name}, %: "))
   premium = (int(amount))*(premium_percent)/100
   self.amount = amount
   self.position = position
   self.premium = premium
 def premium_amount(self):
   print(f"For worker: {self.name} On position: {self.position} With amount of salary: {self.amount} The amount of the premium bonus will be:  {self.premium} ")
EvdokimovaA = Worker("Evdokimova Anna","200000","accountant")
TrofimovM = Worker("Trofimov Mihail","400000","director")
TuchinK = Worker("Tuchin Kirill","300000","architect")
EvdokimovaA.premium_amount()
TrofimovM.premium_amount()
TuchinK.premium_amount()


#TASK 52.
print("\n \ n \n TASK 52")
print("Create the Class Worker, which has the attributes name, amount of salary and position. Add the premium size of salary, which takes the percentage of the premium bonus and calculates the amount of the premium bonus depending on the worker's amount of salary. All workers have one the percentage of the premium bonus")
class Worker():
 def __init__(self,name,amount,position):
   self.name = name
   premium = (int(amount))*(premium_percent)/100
   self.amount = amount
   self.position = position
   self.premium = premium
 def premium_amount(self):
   print(f"For worker: {self.name} On position: {self.position} With amount of salary: {self.amount} The amount of the premium bonus will be:  {self.premium} ")
premium_percent = int(input("Input the percentage of the premium bonus  for all workers, %: "))
EvdokimovaA = Worker("Evdokimova Anna","200000","accountant")
TrofimovM = Worker("Trofimov Mihail","400000","director")
TuchinK = Worker("Tuchin Kirill","300000","architect")
EvdokimovaA.premium_amount()
TrofimovM.premium_amount()
TuchinK.premium_amount()


#TASK 53.
print("\n \ n \n TASK 53")
print("Create a Class Triangle that has attributes sides. The sides should be a list. Add the method, which calculates the area of the triangle.")
class Triangle():
 def __init__(self,sides):
    a = sides[0];b = sides[1];c = sides[2]
    p = (a+b+c)/2
    area = (p*(p-a)*(p-b)*(p-c)) ** (0.5)  
    self.sides = sides; self.area = area
    self.sides[0] = a; self.sides[1] = b; self.sides[2] = c
 def print_area(self):
    print(f" For Triangle with sides {self.sides[0]} cm, {self.sides[1]} cm, {self.sides[2]} сm \n the area of the triangle is - {self.area} sq.сm \n\n")

fig_1_sides = [7,7,7]
fig_2_sides = [7,8,4]
fig_3_sides = [4,4,7]
fig_1 = Triangle(fig_1_sides)
fig_2 = Triangle(fig_2_sides)
fig_3 = Triangle(fig_3_sides)
fig_1.print_area()
fig_2.print_area()
fig_3.print_area()


#TASK 54.
print("\n \ n \n TASK 54")
print("Create a Class Figure that has attributes sides. The sides should be a list. Add the method, which calculates the perimeter of the figure. We have not only one figure.")
class Figure():
  def __init__(self,sides):
    perimeter = 0
    for each in (sides):
      perimeter += each
    self.sides = sides
    self.perimeter = perimeter
  def print_perimeter(self):
    print(f"The perimeter of the figure - {self.perimeter}") 

fig1_sides = [2,4,8,9,1,6]
ug_6 = Figure(fig1_sides)
ug_6.print_perimeter()
fig2_sides = [8,9,6]
ug_3 = Figure(fig2_sides)
ug_3.print_perimeter()  
fig3_sides = [4,8,9,6]
ug_4 = Figure(fig3_sides)
ug_4.print_perimeter()          


#TASK 55.
print("\n \ n \n TASK 55")
print("Create a Class Figure that has attributes sides. The sides should be a list. Add the method, which calculates the perimeter of the figure. We have only one figure and input the length of its sides. Stop-number — 0, if you haven’t got sides.")
class Figure():
  def __init__(self,sides):
    perimeter = 0
    for each in (sides):
      perimeter += int(each)
    self.sides = sides
    self.perimeter = perimeter
  def print_perimeter(self):
    print(f"The perimeter of the figure - {self.perimeter}") 

fig_sides = []
new_side = input("Input the length of the side of the figure in cm   ")
while int(new_side) > 0:
  fig_sides.append(new_side)
  new_side = input("Input the length of the side of the figure in cm   ")
else:
  print("You are wrong. Mistake!  The length of the side of the figure more than null!!!!")  
print(*fig_sides)  
ug = Figure(fig_sides)
ug.print_perimeter()


#TASK 56.
print("\n \ n \n TASK 56")
print("Create a Class Hero in a fantasy world. The class must include the name of the hero, health, power indicator. Write a method that will take the enemy's power and damage and subtract the damage from the hero's health only in case if the enemy's power is greater than the hero's power. We have only one Enemy’s hit on the Hero.")
class Hero():
  def __init__(self,Hero_name,Hero_health,Hero_power):
      self.Hero_name = Hero_name
      self.Hero_health = Hero_health
      self.Hero_power = Hero_power
  def print_remainder_hero_health(self):
    if (int(Enemy_1_power)) > (int(self.Hero_power)):
      a = int(self.Hero_health)
      b = int(Enemy_1_damage)
      self.Hero_health = a - b
      print(f" The health of the Hero {self.Hero_name} was harmed by the enemy {Enemy_1_name}!!!")
    else:
       print(f"For this Hero {self.Hero_name} this Enemy {Enemy_1_name} is too weak!!! ") 
    print(f"The remaining health of the Hero {self.Hero_name} with the power {self.Hero_power} after being hit by the Enemy {Enemy_1_name} - {self.Hero_health}")

Enemy_1_name = "Wolf"
Enemy_1_power = input(f"Input the power of the Enemy {Enemy_1_name} - a number greater than zero:   ")
Enemy_1_damage = input(f"Enter the damage inflicted after being hit by the Enemy {Enemy_1_name} the Hero's health - a number greater than zero   ")   
Hero_1 = Hero("Hare","300","200")
Hero_1.print_remainder_hero_health()


#TASK 57.
print("\n \ n \n TASK 57")
print("Create a Class Fight in a fantasy world. The class must include the name of the hero, health, power indicator and also the name of the enemy, health, power indicator. Write a method that will take the enemy's power and damage and subtract the damage from the hero's health only in case if the enemy's power is greater than the hero's power. You can choose, who hit: Enemy on Hero or Hero on Enemy. Also you can choose what is the hit: well-aimed hit or missed hit. Organize a great battle between a hero and an enemy until the health of one of them is null or becomes negative")
# Hero_harm - the damage that is caused by Hero’s well-aimed hit to the Enemy's health; other words, how much the Enemy's health will decrease after Hero’s hit
# Enemy_harm - the damage that is caused by Enemy’s well-aimed hit to the Hero's health; other words, how much the Hero's health will decrease after Enemy’s hit
class Fight():
  def __init__(self,Hero_name,Hero_health,Hero_harm,Enemy_name,Enemy_health,Enemy_harm):
      self.Hero_name = Hero_name
      self.Hero_health = Hero_health
      self.Hero_harm = Hero_harm
  
      self.Enemy_name = Enemy_name
      self.Enemy_health = Enemy_health
      self.Enemy_harm = Enemy_harm 
  def print_fight(self):
   while (int(self.Enemy_health)) > 0 and (int(self.Hero_health)) > 0:
    Question_1 = input(f"Who hits? Input {self.Hero_name} or {self.Enemy_name}.  ")
    Question_2 = input("Got it? Input YES or NO. ")
   # print(f"{self.Hero_name} - {self.Hero_health} --- {self.Enemy_name} - {self.Enemy_health}")   
    if Question_1 == self.Hero_name:
      if Question_2 == "YES":
        a = int(self.Enemy_health)
        b = int(self.Hero_harm)
        self.Enemy_health = a - b
        print(f"{self.Hero_name} - {self.Hero_health} : {self.Enemy_name} - {self.Enemy_health}") 
      elif Question_2 == "NO":
        print("The hit was - but it was missed hit!!!!")
        print(f"{self.Hero_name} - {self.Hero_health} : {self.Enemy_name} - {self.Enemy_health}") 
      else:
        print("Mistake!") 
    elif Question_1 == self.Enemy_name:
      if Question_2 == "YES":
        a = int(self.Hero_health)
        b = int(self.Enemy_harm)
        self.Hero_health = a - b 
        print(f"{self.Hero_name} - {self.Hero_health} : {self.Enemy_name} - {self.Enemy_health}") 
      elif Question_2 == "NO":
        print("The hit was - but it was missed hit!!!")
        print(f"{self.Hero_name} - {self.Hero_health} : {self.Enemy_name} - {self.Enemy_health}") 
      else:
        print("Mistake!") 
    else:
        print("Mistake!") 
   else:
      if (int(self.Enemy_health)) == (int(self.Hero_health)):
        print("There is no winner!") 
      elif (int(self.Enemy_health)) < 0 or (int(self.Enemy_health)) == 0:
        print(f"The Enemy {self.Enemy_name} is defeated. {self.Hero_name} is a winner.")
      elif (int(self.Hero_health)) < 0 or (int(self.Hero_health))== 0:
        print(f"The hero {self.Hero_name} is defeated. {self.Enemy_name} is a winner.") 
      else:
        print("Mistake") 
   #print(f"{self.Hero_name} - {self.Hero_health} --- {self.Enemy_name} - {self.Enemy_health}")     

Pair_1 = Fight("Hare","100","20","Wolf","150","50")
Pair_1.print_fight() 
        


#TASK 58.
print("\n \ n \n TASK 58")
print("How many times can we multiply a certain number by 2 but the result of that multiplication is not more than 100. ")
n = int(input("Input the number"))
C = 0
while n < 100:
 n = n * 2
 C = C + 1
print(f"We can do it - {C-1} times") 


#TASK 59.
print("\n \ n \n TASK 59")
print("Output the sum of all numbers in the list.")
numbers = [1,2,3,4,5]
total = 0
for num in numbers:
  total += num
print(f"The list - {numbers}.")
print(f"The sum of all numbers in the list - {total}.") 


#TASK 60.
print("\n \ n \n TASK 60")
print("Create a Class that returns the square of a numbers.")
class MyClass:
   def __init__(self):
     self.value = 0
   def update_value(self,new_value):
     self.value = new_value ** 2
   def get_value(self):
     return self.value  

obj = MyClass()
obj.update_value(10) 
print(obj.get_value()) 
obj.update_value(20) 
print(obj.get_value()) 
obj.update_value(30) 
print(obj.get_value())
