a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = 0
print((a),("x"),(b),("="),(a*b))
if (a*b) > 0:
    print("The result is positive.")
elif (a*b) < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")