def filterEx(n):
    return n %2==0

tup=(1,2,3,4,5,6,7,8,9)

print(list(filter(filterEx,tup))) #also print in tuple


#using lambda function

list1=[1,2,3,4,5,6,7,8,9]

print(list(filter(lambda x:x if x*x >6 else '',list1)))


