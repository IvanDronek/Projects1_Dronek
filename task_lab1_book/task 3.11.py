print("----3.11----")
print("А")
x = 1
y = -1
if x ** 2 + y ** 2 <= 4:
    print(True)
else:
    print(False)

print("Б")
x = 1
y = 2
if x >= 0 or y ** 2 != 4:
    print(True)
else:
    print(False)

print("В")
x = 1
y = 2
if x >= 0 and y ** 2 != 4:
    print(True)
else:
    print(False)

print("Г")
x = 2
y = 1
if x * y != 0 and y > x:
    print(True)
else:
    print(False)

print("Д")
x = 2
y = 1
if x * y != 0 or y < x:
    print(True)
else:
    print(False)

print("Е")
x = 2
y = 1
if not x * y < 0 and y > x:
    print(True)
else:
    print(False)

print("Ж")
x = 1
y = 2
if not x * y < 0 or y > x:
    print(True)
else:
    print(False)
