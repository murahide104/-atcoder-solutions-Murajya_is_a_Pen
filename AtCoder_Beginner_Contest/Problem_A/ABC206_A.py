n = int(input())
print(n * 1.08)
if n * 1.08 < 206:
    print("Yay!")
elif int(n * 1.08) == 206:
    print("so-so")
else:
    print(":(")