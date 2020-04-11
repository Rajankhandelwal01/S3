a = 5

b = 2

try:
    print("resource open")
    print(a/b)
    k = int(input("enter a number"))
    print(k)

except Exception as e:
    print(e)

finally:
    print("resource closed")