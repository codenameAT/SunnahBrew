print("As salaam wa alaikum, welcome to Sunnah Brew! Home of the finest coffee.")

#Name for order
name = input("What is your name for your order?\n")

#No Crackheads allowed!!
if name == "Ben" or name == "":
  crackhead_status = input("are you a crackhead?\n")
  if crackhead_status == ("yes"):
    print("You're not welcome here crackhead! Get out before I call the police!!!")
    exit(name)
else:
 print("Hello " + name + ", thank you for coming in today.\n\n\n")

#Cafe menu
menu = "Black coffee, Espresso, Latte, Tea"

print(name + ", what can I get you today? Here is what we are serving.\n"
     + menu)

order = input()
if order == ("Tea"):
  print("Ah, need something to relax your mind, ey?")
elif order == ("Black coffee"):
  print("You must really need a pick me up, ey?")
elif order == ("Espresso"):
    print("I assume this is for your wife, ey?")
elif order == ("Latte"):
    print("Feeling a little fancy today, ey?")
price = 4

quantity = input("how many will you like?\n")
total = price * int (quantity)

print("Thanks you, your total is: $" + str(total))

print("Sounds good " + name + ", I will have your order ready in a moment.")

import time
n = 5
while n > 0:
  print(n)
  time.sleep(1)
  n -= 1
print("Here you go! Thank you for coming into Sunnah Brew. Have a great day.")