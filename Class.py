print('Class Duck Demo')
class Duck:
    sound='Quack ! like a Duck'
    walking='Walk ! like a Duck'
    def quack(self):
        print(self.sound)
    def walk(self):
        print(self.walking)

def main():
    duckObject=Duck()
    duckObject.walk()
    duckObject.quack()

if __name__ == '__main__': main()
print('Class Duck Demo completed')
