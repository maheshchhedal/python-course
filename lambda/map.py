def myFunction(n):
    return n*n
list1=[1,2,3,4,5]
print(list(map(myFunction,list1)))

nums=[1,2,3,4,5]
print(list(map(lambda x: x if x>2 else 0, nums)))