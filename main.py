import random
r =random.randint(-100,100)

found = false 
while found == false:
  m = int(input("Guess a number  "))
  
  if m == r:
    found = true 
    print("You won!!!")
    elif m>r:
  print(str(m), "is more thann it")
elif m<r:
    print(str(m), "is less than it")
    else:
      print("THis is not a number, try again.")