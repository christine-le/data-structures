# Stacks and Queues exercises (from Cracking The Coding Interview)

#3.1 Three in One: Use single array to implement three stacks
class Stack(object):
    def __init__(self):
        self.size = 0
        self.stack = []
        self.tops = []

    def add_stack(self, new_stack):
    	if len(self.tops) == 0:
    		self.tops.append(0)
        else:
        	self.tops.append(self.size)
    	
    	self.size += len(new_stack)
        self.stack.extend(new_stack)

    def update_pointers(self, stack_num):
    	i = len(self.tops) - 1
        while i >= stack_num:
        	self.tops[i] -= 1
        	i -= 1

    def push(self, stack_num, value):
    	top = self.tops[stack_num-1]
    	self.stack.insert(top, value)
    	self.size += 1

    	self.update_pointers(stack_num)

    def pop(self, stack_num):
    	top = self.tops[stack_num-1]
        self.stack.pop(top)
        self.size -= 1
        self.update_pointers(stack_num)
        
    
my_stack = Stack()
my_stack.add_stack([1,3,5])
my_stack.add_stack([2,4,6,8])
my_stack.add_stack([1,2,4,8])

my_stack.push(2, 10)
my_stack.push(3, 50)
my_stack.pop(2)

# print my_stack.stack
# print my_stack.tops

#3.5 Sort Stack:
class SortStack(object):
    def __init__(self, stack = []):
        self.stack = stack
        self.stack2 = []
    
    def sort(self):
        while len(self.stack) > 0:
            tmp = self.stack.pop()

            while len(self.stack2) > 0 and tmp < self.stack2[len(self.stack2) - 1]:
	            self.stack.append(self.stack2.pop())

            self.stack2.append(tmp)

        while len(self.stack2) > 0:
        	self.stack.append(self.stack2.pop())


my_stack = SortStack([5,10,1,2])
print my_stack.stack
my_stack.sort()
print my_stack.stack