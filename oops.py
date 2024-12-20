def pow(base, n):
    if n == 0:
        return 1
    else:
        return base * pow(base, n-1)
print(pow(5, 4))
