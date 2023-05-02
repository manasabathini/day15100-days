exit = "no"

while exit == "no":
  animal = input("What animal do you want?: ")

  if animal == "cow":
    print("Mooo!")
  elif animal == "Dog":
    print("Woof! Woof!")
  elif animal == "Rooster":
    print("cock a doodle doo")
  else: 
    print("I can't find the animal")

  exit = input("Exit?: ")