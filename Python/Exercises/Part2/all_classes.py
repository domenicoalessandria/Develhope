## ex 1 & 2
class animal():
    
    print('Animal object was created')
    
    def __init__(self,n_leg):
        self.n_leg=n_leg
        
    def runs(self):
        print('Running started')
    
    def count_legs(self):
        print(n_leg)
        
    def return_legs(self):
        return n_leg

dog=animal(4)
dog.n_leg


## ex3
class Animal():
    
    print('Animal object was created')
    
    def __init__(self,n_leg):
        self.n_leg=n_leg
        
    def runs(self):
        print('Running started')
    
    def _count_legs(self):
        print(self.n_leg)
        
    def return_legs(self):
        return self.n_leg
    
    def num_legs_plus_one(self):
        return self.return_legs()+1

## ex4

class Dog(Animal):
    
    def __init__(self,n_leg,name):
        Animal.__init__(self,n_leg)
        self._name=name
    
    def bark(self):
        print('Woof Woof')

dog=Dog(4,'Barney')

print(dog._name)
dog.bark()
dog._count_legs()