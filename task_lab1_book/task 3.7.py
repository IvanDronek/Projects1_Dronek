print("-----3.7-----")
a = True
b = False
c = False

print(a or not (a and b) or c)
print(not a or a and (b or c))
print((a and b and not c) and c)