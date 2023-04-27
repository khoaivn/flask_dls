# for x in range(3):
#     print(x)
# for x in range(2,6):
#     print(x)
# for x in range(2, 30, 5):
#     print(x)
# fruits = ['apple', 'banana', 'cherry']
# print(type(fruits))
# for x in fruits:
#     print(x)
# for x in 'banana':
#     print(x)
# for x in range(1, 101):
#     if (x % 2 == 1):
#         print(x)

# n = input("nhap n:")
# print(n)
# for x in range(2, 100):
#     if((x % 2 == 0) & (x % 3 == 0)):
#         print(x)

# S = 0
# n = int(input("nhap n:"))
# for x in range(1, n + 1):
#     S += x
# print(S)

# a = int(input("Nhap a:"))
# so_uoc = 0
# for x in range(1, a + 1):
#     if (a % x == 0):
#         so_uoc += 1
# print("So uoc cua a la:", so_uoc)

# i = 1
# while i < 6:
#     print(i)
#     i += 1

a = int(input("Nhap a:"))
while a <= 0:
    a = int(input("Nhap lai a:"))
print("Ban nhap dung quy tac")    