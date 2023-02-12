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