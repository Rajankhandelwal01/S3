num = int(input("input the value"))

for i in range(2,num):
    if num % i==0:
        print("not Prime")
        break

else:
    print("Prime")
