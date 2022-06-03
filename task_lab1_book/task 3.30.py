print("-----3.30-----")
print("a")
a = float(input())

if a % 2 == 0 or a % 3 == 0:
    print(True)
else:
    print(False)

print("б")
a = float(input())

if a % 10 != 0:
    print(False)
elif a % 3 !=0:
    print(True)
else:
    print(False)