class Moo:
    def __init__(self, num):
            self.num = num
    
    def get_num(self):
        print(self.num)

mer = [Moo(2), Moo(3), Moo(4)]
meow = mer[0]
print("what " + str(meow.get_num()))
del mer[0]
print("what " + str(meow.get_num()))
print(meow.get_num())