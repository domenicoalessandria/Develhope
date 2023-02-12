## ex1
def goodbye():
    print('goodbye')

## ex2
def goodbye1(name: str):
    print(f'goodbye {name}')

## ex3
import os 
user=os.getlogin()
print(user)

## ex4
## non ho capito l'esercizio
def selected greetings(name_list):
    for i in name_list:
        print(f'hello {i}')

## ex5
import random
def random_list_summer():
    mysum=0
    for i in range(15):
        r=random.randint(-100,100)
        print(r)
        mysum+=r  
    return mysum

## ex Fibonacci sequence
def fibonacci_seq_gen(n):
    myseq=[0,1]
    for i in range(1,n):
        myseq.append(myseq[i-1]+myseq[i])
    
    return myseq

## ex 7
squared_list=list(map(lambda i: i**2,[*range(5)]))