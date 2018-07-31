print('Prime numbers List')
def main(n):
    isPrime(n)
    listPrime()

def isPrime(n):
    if n<=1:
        return False
    for x in range(2,n):
        if n%x==0:
            return False
        else:
            return True

def listPrime():
    for n in range(100):
         if isPrime(n):
            print (n,end=' ',flush=True)

if __name__ == '__main__': main(7)
     