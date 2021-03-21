class myStack:
     def __init__(self):
          self.stack = []
          
     def isEmpty(self):
          return True if not self.stack else False
         
     def push(self, item):
          self.stack.append(item)
         
     def pop(self):
          if self.isEmpty():
               return -1
          return self.stack.pop()
        
     def peek(self):
          if self.isEmpty():
               return -1
          return self.stack[-1]

     def size(self):
          return len(self.stack)
         
     def show(self):
          return self.stack

s = myStack()
s.push('1')
s.push('2')
print(s.pop())
print(s.show())
print(s.pop())
print(s.pop())
print(s.pop())