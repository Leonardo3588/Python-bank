import random
import time


def bank():
 while True:  
   print("Welcome to the bank!")
   amount =  input("Please input the amount of money you want to deposit ") 
   amount = int(amount) #Turns the str into an integer
   if amount < 0:
      print("Invalid amount of money, retry")
      break
   if amount > 0:
      print("Checking if money is real...")
      time.sleep(2)
      outcome = random.choice([True, True, False]) #Checks if money is true  
   outcome = str(outcome)

   if outcome == "False":
         print("Sorry, the money is fake. Please try again.")
         input("Press any key to retry")
        
   elif outcome == "True":
      print("Money deposited.")
      input("Press any key  to exit ")
      break
      

   
  
bank()