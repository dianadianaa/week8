def xor(x, y):
    if x == 0 and y == 1 or x == 1 and y == 0:
        return 1
    else:
        return 0


a = input().split()
print(xor(int(a[0]), int(a[1])))