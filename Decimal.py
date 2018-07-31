print('Demo for Decimal calculations')
from decimal import *
x= .1+.1+.1-.3
print ('sum of .1+.1+.1-.3 is', x,'but expected is {}'.format(0.0))
a=Decimal(.1)
b=Decimal(.3)
x= a+a+a-b
print ('sum of Decimal(.1)+Decimal(.1)+Decimal(.1)-Decimal(.3) is', x,'but expected is {}'.format(0.0))
a=Decimal('.1')
b=Decimal('.3')
x= a+a+a-b
print ('sum of a+a+a-b is', x,' and expected is {}'.format(0.0))