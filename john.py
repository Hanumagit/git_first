'''print("hello python")
A=10
B=20
print(A+B)


VAR="Hanuma"
VAR1="John"
print(VAR+VAR1)'''
'''
for i in range(10):
    print("Atempt",i+1,(i+1)*".")

for i in range(10):
 print("Atempt",i+1,(i-1)*".")'''




'''
for i in range(1,10):
    print("Atempt",i,i*".")

count=0
for i in range(1,10):
    if i%2==0:
        count+=1
        print(i)
print(f"Count of even numbers:{count}")
'''

m=[10,20,30,40,50,60,70,80,90,100]
s=0
for i in m:
    s=s+i
print(s)

'''
l=[1,2,3]
dm=[]
for i in l:
    dm.append(i)
print(dm) '''
'''
n=[1,2,3,4]
s=[]
for i in range(0,len(n)+1):
    s.append(i*i)
print(s)

l=[1,2,3,4]
print([i+i for i in n])

'''

h =[70.5,40.2,48.5,60.5,75.0,52.0,85.0]
day=input("enter 'sun','mon','tues',,'wed','thur','fri','sat':")
if day=="sun":
    dayname="sunday"
    temp=h[0]
elif day=="mon":
    dayname="monday"
    temp=h[1]
elif day=="tues":
    dayname="Tuesday"
    temp=h[2]
elif day=="wed":
    dayname="Wedday"
    temp=h[3]
elif day=="thur":
    dayname="Thursday"
    temp=h[4]
elif day=="fri":
    dayname="Friday"
    temp=h[5]
elif day=="sat":
    dayname="saturday"
    temp=h[6]
else:
    print('it is invalid day and tempreature')
print(f"Temprature for:{dayname} was {temp} degress")



l=[1,2,3,4,5,6]
dict.fromkeys(l)
