def fact(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i

    return f


x = int(input("Enter the value of which you want to get factorial"))

result = fact(x)

print(result)
