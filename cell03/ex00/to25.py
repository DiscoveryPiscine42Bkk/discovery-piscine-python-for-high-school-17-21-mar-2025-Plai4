x = int(input("Enter a number less than 25:"))
while x < 25:
  x += 1
  if x == 20:
    continue
  print("Inside the loop, my variable is", x)