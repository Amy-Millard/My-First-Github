import math

num = int(input("Please enter a value"))


try:
  print(math.sqrt(num))
except:
  print("Bad value")
  print("Using absolute value")
  print(int(abs(num)))
