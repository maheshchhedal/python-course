
lis=[1,2,3,4,5,6]
double=[]

for i in lis:
    if i%2==0:
        db=i*i
        double.append(db)
print(double)

#using list comprehensive

db=[i*2 for i in lis]
print(db)

doubles=[i*i for i in lis if i%2==0]
print(doubles)

name=['ram','hari','shyam','arjun']

uppercase=[nm.upper() for nm in name ]
print(uppercase)

upp=[nm[0].upper() for nm in name ]
print(upp)