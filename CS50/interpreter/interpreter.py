exp = input("Expression: ")

x, y, z = exp.split(" ")
x = int(x)
z = int(z)

if y == "+":
    ans = x + z
elif y == "-":
    ans = x - z
elif y == "*":
    ans = x * z
elif y == "/":
    ans = x / z

print(float(ans))