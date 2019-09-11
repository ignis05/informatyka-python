# przykładowa implementacja stosu w pythonie
 
import os
 
 
def clear(): return os.system('cls')
 
 
clear()
 
 
class Stack:
    def __init__(self):
        self.items = []
 
    def isEmpty(self):
        return self.items == []
 
    def push(self, elem):
        self.items.append(elem)
 
    def pop(self):
        if self.isEmpty() == False:
            return self.items.pop()
 
    def peek(self):
        if self.isEmpty() == False:
            return self.items[-1]
 
    def getSize(self):
        return len(self.items)
 
 
# zastosowanie:
 
stack = Stack()
 
print('OUTPUT: \n')
while True:
    print('\n0 - exit')
    print('1 - push')
    print('2 - pop')
    print('3 - peek')
    print('4 - getSize')
    print('5 - isEmpty')
    x = int(input('\nCo checsz zrobic?\n'))
 
    if x == 1:
        el = input('Podaj wartość do umieszczenia w stacku:\n')
        stack.push(el)
        clear()
        print('OUTPUT: ')
        print(el)
    if x == 2:
        clear()
        print('OUTPUT: ')
        print(stack.pop())
    if x == 3:
        clear()
        print('OUTPUT: ')
        print(stack.peek())
    if x == 4:
        clear()
        print('OUTPUT: ')
        print(stack.getSize())
    if x == 5:
        clear()
        print('OUTPUT: ')
        print(stack.isEmpty())
    if x == 0:
        break