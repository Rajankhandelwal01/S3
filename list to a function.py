
def count(lst):

    even = 0
    odd = 0
    for i in lst:
        if i%2 ==0:
            even+=1
        else:
            odd+=1

    return even,odd

lst = [20,12,3,5,78,5,6,7,45,46]

even,odd =count(lst)

print(even)
print(odd)

print("Even: {} and odd: {}".format(even,odd))