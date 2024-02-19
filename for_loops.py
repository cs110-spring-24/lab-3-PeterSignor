print ("options: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
run = input ("enter the problem you want to run: ")
run = int(run)
if run == 1:
    for count in range(1,1001):
     print(count)

# Write a program that prints out the odd numbers between 1 and 1000. (+5 points)
if run == 2:
    for count in range(1,1001,2):
       print(count)     

# Write a program that prints out the numbers between 0 and 1000 that are divisible by 3. (+10 points)
if run == 3:
   for count in range(1,1001):
      if count % 3 == 0:
         print(count)

# Write a program that prints out the numbers between 1 and 1000 that are divisible by 3 or 5. (+10 point)
if run == 4:
    for count in range(1,1001):
        if count % 3 == 0:
            print (count)
        elif count % 5 ==0:
           print (count) 

# Write a program that asks the user to enter a number and prints out all the numbers between 1 and 
# that number that are divisible by 11 or 13. The number entered should be greater than 200. (+10 points) 
# Extra credit if the programs asks again if the number is less than 200. (+5 points)
if run == 5:
   user = int(input("Enter a number greater than 200:  "))
   if user < 200 :
      print(user, "is less than 200")
   else:   
      user = int(user) + 1
      for count in range(1,user):
         if count % 11 == 0:
            print(count)
         elif count % 13 == 0:
            print(count)  

# Write a program that prints out each letter of a string line by line (+5 points)
if run == 6:
   string1 = input("Enter a word: ")
   for L in range(0, len(string1),):
      print (string1[L])
# Write a program that asks the user to enter a string 
# and outputs every second letter. The string must be more than 10 letters long. (+10 points)

if run == 7:
   string2 = input("Enter a word over 10 letters long: ")
   for M in range(0,len(string2),2):
      print (string2[M])

# Write a program that rolls 1000 dice and prints out the number of times each number
# was rolled. (+15 points)
if run == 8:
   import random 
   one = 0 
   two = 0
   three = 0 
   four = 0
   five = 0 
   sixes = 0 
   for rolls in range(1000):
      dice = random.randint(1,6)
      if dice == 1:
         one += 1 
      elif dice == 2:
        two += 1 
      elif dice == 3:
        three += 1    
      elif dice == 4:
        four += 1 
      elif dice == 5:
        five += 1         
      else:
        sixes += 1 
   print(f"You rolled {one} 1's, {two} 2's, {three} 3's, {four} 4's, {five} 5's, {sixes} 6's")

# Write a program that checks if a given number is a prime number. A prime number is a number 
# that is only divisible by 1 and itself. The user enters a number and the programs prints out
# whether the number is a prime number or not. (+15 points)

if run == 9:
   user = (int(input("enter a number: ")))
   for i in range(2, user):
         if (user % i == 0):  
            print(user, "is not a prime number")
            exit()
   else:
      print(user, "is a prime number")
             


# Write a program that prints out the prime numbers less than 1000. (+20 points) 
if run == 10:            
   print("Skipped problem couldn't figure it out")

