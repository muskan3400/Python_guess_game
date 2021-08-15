
import random
import string

print("WELCOME TO THE GUESS GAME!")
print("\n")
name=input("What is your name:")
print("\n")

print("Choose difficulty level")
print("B:Beginner level")
print("I:Intermediate level")
print("A:Advanced  level")

B=["early","table","abroad","letter","python","advice","actor","github","branch","charge","string","integer","source","array","binary","stack","queue","search","merge","quick","bucket"]
I=["crocodile","education","strawberry","government","pineapple","development","algorithm","assignment","tensorflow","appreciate","friendship","motivation","california","basketball","childhood","punishment","helicopter","leadership","revolution"]
A=["encouragement","reincarnation","sportsmanship","infrastructure","programming","independence","relationship","organization","architecture","concentration","deforestation","collaboration","international","embarassment","communication","discrimination","responsibility","photosynthesis"]

while True:
   cd=input()  #difficulty level
   if cd=="b" or cd=="B":
     word=random.choice(B)
     guesses=4
     break
   elif cd=="i" or cd=="I":
     word=random.choice(I)
     guesses=7
     break
   elif cd=="a" or cd=="A":
     word=random.choice(A)
     guesses=10
     break
   else:
     print("Please select a valid level") 
     continue
   
print("\n")
print("Good luck",name,"!")
print("\n")

print("Guess the hidden letters of the word")
print("The vowels are already revealed for you!!!")
print("Your word is.........")
print("\n")

k=["a","i","e","o","u"]

for i in word:
  if i in k :
   print (i,end=" ")
  else :
   print("_",end=" ")  

alphabet_list=list(string.ascii_lowercase)  #list of all small letters
while (guesses>0):
    fail=0
    print("\n")
    print("No. of guesses left:",guesses)
    g=(input("Guess a character : ")).lower()
    m=list()

    if len(g)==1 and g in alphabet_list:

       if g in k:
           print("\n")
           print ("That character is already revealed!")
           continue
       
       if g in word:
         print("YAY!") 
         print("Character found")
         k.append(g) #appending to the list of vowels

         for char in word:
            if char in k:
              print(char,end=" ")

            else:
              print("_",end=" ") 
              fail=fail+1

         guesses=guesses-1    
         if (fail==0):   #this occurs when all the letters will be revealed
           print("\n")  
           print("YOU WON!!")
           print("The letter is",word)
           print("HURRAH!! ")
           break
         
       else:
         print("Oops! letter not found")
         guesses=guesses-1   

    else:
      print("\n")  
      print("Enter a single character!!") 
      continue

if (guesses==0):
  print("\n")  
  print("You lost! ")
  print("There are no guesses left")
  print("So, the answer was")
  print(word)