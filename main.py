# for i in range(100, 110):
#   print(i)

# for i in range(1, 8):
#   print("Day", i)

# print("Thirteen Times Table")
# for i in range(1, 13):
#   print(i, "x 13 =", i * 13)

# for i in range(0, 1000001, 250000):
#     print(i)

# for i in range(10, -1, -1):
#   print(i)

# for i in range(10, 0, -1):
#     print(i)

# for i in range(20, 40, 1):
#   print(i)
print("Welcome to my number list generator.")
print()
print("You are going to give me a number you want to start with, an ending number, and by how many you want me to add each time.")
print()
m = int (input("enter starting number: "))
n = int (input("enter ending number: "))
p = int (input("enter increamental number:"))

for i in range (m, n, p):
  print(i)