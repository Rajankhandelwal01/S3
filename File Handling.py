f = open('../MyData.txt', 'r')

print(f.readline(),end="")
print(f.readline())

f1 = open('abc', 'w')

for data in f:
    f1.write(data)