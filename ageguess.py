try:
    age= int(input("please enter the input \n"));
    if(age>0 and age<=5):
        print("he is a kid" )
    elif(age>5 and age <=30):
        print("he is young man");
    elif(age>31 and age<=60):
        print("middle aged man");
    elif(age>61):
        print("he is too old person");
    else:
        print("Invalid age entered, please enter correct age");
except:
    print("wrong type entered, try with integer value")
