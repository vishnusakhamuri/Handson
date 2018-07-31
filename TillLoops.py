print("Hello Python users")
if (5>2):
    print("five is greater than two")
#This is a comment
"""this is a mulitline
docstring hehe"""
x=input()
print(x)
x=3
y=2.0
print(" x+y is :" ,x+y)
z="1"
a=1j
print(" z is :" ,z)

print(" x is :" ,x)
print(" y is :" ,y)
print(" z is :" ,z)
#Numeric types examples
print(type(x))
print(type(y))
print(type(z))
print(type(a))

x = 1
y = 35656222554887711
z = -3255522
print(" x is :" ,x)
print(" y is :" ,y)
print(" z is :" ,z)

print(type(x))
print(type(y))
print(type(z))

x = 1.10
y = 1.0
z = -35.59
print(" x is :" ,x)
print(" y is :" ,y)
print(" z is :" ,z)

print(type(x))
print(type(y))
print(type(z))


x = 35e3
y = 12E4
z = -87.7e100
print(" x is :" ,x)
print(" y is :" ,y)
print(" z is :" ,z)

print(type(x))
print(type(y))
print(type(z))

x = 3+5j
y = 5j
z = -5j
print(" x is :" ,x)
print(" y is :" ,y)
print(" z is :" ,z)

print(type(x))
print(type(y))
print(type(z))

print("Data conversions")

print("to int")
x=int(1.0)
y=int('1')
z=int("2")
print(" x is :" ,x)
print(" y is :" ,y)
print(" z is :" ,z+x)
print("to float")
x=float(1.0)
y=float('1')
z=float(1)
print(" x is :" ,x)
print(" y is :" ,y)
print(" z is :" ,z)

print("to str")
x=str(1.0)
y=str('1')
z=str(1)
print(" x is :" ,x)
print(" y is :" ,y)
print(" z is :" ,z)

print(" Arrays")
array='This is me'
print(array[0],array[0],array[0],array[0],array[0],array[0])
print(array[0],array[1],array[2],array[0:5]+array[6]+array[9])
print(array[0:10])

print(" Demo for strip()")
print(array.strip())
print(len(array))
print(array.lower())
print(array.upper())
print(array.replace('e','T'))
print(array)
print(array.split(' '))
print("Operators handson")
x=6
x-=3
print(x)
x=6
x+=3
print(x)
x=6
x = x / 3
print(x)
x=6
x = x % 3
print(x)
x=6
x = x // 3
print(x)
x=6
x = x ** 3
print(x)
x=6
x = x & 3
print(x)
x=6
x = x | 3
print(x)
x=6
x = x ^ 3
x=6
x = x >> 3
print(x)

x=6
x = x << 3
print(x)

x=6
y=4
if(x==y):
    print("X is equal to Y")
elif(not(x<=y or x>=y)):
    print("X is equal to Y")
elif(x<=y or x>=y):
     print("X is not equal to Y")
elif(x>0 and y>0):
    print("X and Y both are bigger than 0")
else :
    print("X is not equal to Y")

x='1'
y='1'
if (x is y):
    print ("both referring to same location")
x='str'
y='sub string is a portion inside the string'
if (x in y):
     print("true")
if (x not in y):
     print("false")

print (" **********Collections************* ")
print (" **********List************* ")
ThisIsList=['this','is ','my','first','list']
print(ThisIsList)
ThisIsList[2]=["Your"]
print(ThisIsList)
ThisIsList[2]="Your"
print(ThisIsList)
ThisIsList=list(['this','is ','my','first','list'])
print(ThisIsList)
ThisIsList=list(('this','is ','my','first','list'))
print(ThisIsList)
ThisIsList.append('Vishnu')
print(ThisIsList)
ThisIsList.append(['my','first','list'])
ThisIsList.remove(['my','first','list'])
print(ThisIsList)
print(len(ThisIsList))
copiedList=ThisIsList.copy()
print(copiedList)
copiedList.pop()
print(copiedList)
print(ThisIsList.count("my"))
copiedList.clear()
print(copiedList)
copiedList.extend(ThisIsList)
print(copiedList)
ThisIsList.extend(ThisIsList)
print(ThisIsList)
ThisIsList.extend(copiedList)
print(ThisIsList)
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)
print(fruits.index('Volvo'))
fruits.insert(1,'orange')
print(fruits)
fruits.pop(4)
print(fruits)
fruits.remove('Volvo')
print(fruits)
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)
print (" **********Tuple************* ")
ThisISTuple=('1','2','3',('4','5'))
print (ThisISTuple)
ThisISTuple = tuple(("apple", "banana", "cherry"))
print (ThisISTuple)
ThisISTuple=('1','2','3',('4','5'))
print (ThisISTuple)
print (" **********Set************* ")
ThisISSet={'1','2','3','4'}
print (ThisISSet)
ThisISSet = set({"apple", "banana", "cherry"})
print (ThisISSet)
ThisISSet={'1','2','3'}
print (ThisISSet)
thisset = set(("apple", "banana", "cherry"))
print(thisset)
thisset = set(("apple", "banana", "cherry"))
thisset.add("damson")
print(thisset)
thisset = set(("apple", "banana", "cherry"))
thisset.remove("banana")
print(thisset)
thisset = set(("apple", "banana", "cherry"))
print(len(thisset))
print (" **********Dictionary************* ")
thisISDict={
    "pinapple":"green",
    "mango":"yellow",
    "berry":"blue",
    "apple":"red"
    }
print (thisISDict)
thisISDict[1]="yellow"
print (thisISDict)
thisISDict["berry"]="yellow"
print (thisISDict)

thisISDict=dict(pinapple="green",
    mango="yellow",
    berry="blue",
    apple="red")

print (thisISDict)
thisISDict["damson"] = "purple"
print(thisISDict)
thisdict =	dict(apple="green", banana="yellow", cherry="red")
print(len(thisdict))
print (" **********Python Loops************* ")
print (" **********While************* ")
i=1
while i<10:
    print("i value is:",i)
    if(i==5):
        print("i value reached:",i,"so exiting")
        break
    else:
        print("i value reached:",i,"so continued")
        i+=1
        continue

print (" **********For ************* ")   
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print("x is:",x)
print (" **********For range************* ")
for x in range(6):
  print("x is:",x)
print (" **********For range with start and end************* ")
for x in range(2, 6):
  print("x is:",x)
print (" **********For range with start,end and with increment value************* ")
for x in range(2, 30, 3):
  print("x is:",x)

print (" **********Functions ************* ")
def tri_recursion(k):
    if(k>0):
        k=k+tri_recursion(k-1)
        print("call is inside the recursion",k)
    else:
        k=0
        print("call is outside the recursion", k)
    return k

print("\n\nRecursion Example Results")
tri_recursion(6)
        


  
exit()
