print("Welcome to Multiplication Table Generator in Python")
print("By NoobzSquad")

num = int(input("Enter Your Number: "))
rng = int(input("Enter Your Range: "))
rng += 1
print("Multiplication Table Of", num)
for x in range(1, rng):
    print(num, 'x', x, '=', num * x)
