import platform

def main():
    message()

def message():
    true()
    bigger()

def bigger():
   x,y=5,5
   if x>=y:
       print("x>=y and X is {} and Y is {}".format(x,y))
       x,y=5,4
   elif x<=y:
       print("x<=y and y is {1} and x is {0}".format(x,y))
   else:
       print("x=y and X is {0} and Y is {1}".format(x,y))
 

def true():
 if True:
    x='All'
    print("Hello World,{}".format(x))
    
if __name__ == '__main__':
    main()