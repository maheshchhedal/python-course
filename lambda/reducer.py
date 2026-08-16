from functools import reduce

def reducerEx(x,y):
    return x+y

lis=[10,20.2,23.0,55]
print(reduce(reducerEx,lis))


#using map
tup=(10,55.2,66,80.5,99)
print(reduce(lambda x,y: x+y,tup))