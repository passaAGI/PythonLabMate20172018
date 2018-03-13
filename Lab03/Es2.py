""" Vincenzo Passariello - Es2 - Lab03 """

def reverseOrder(a, b, c):
    nums = [a, b, c]
    for i in reversed(nums):
        print(i)

x = float(input("Primo numero: "))
y = float(input("Secondo numero: "))
z = float(input("Terzo numero: "))
reverseOrder(x, y, z)
