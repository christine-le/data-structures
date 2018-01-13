# Linked Lists exercises (from Cracking The Coding Interview)

# 2.1  Remove Dups:  Write code to remove duplicates from an unsorted linked list
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, node):
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = node

    def display(self):
        curr = self.head
        print curr.data

        while curr.next != None:
            curr = curr.next
            print curr.data

    def remove(self, node):
    	curr = self.head
        prev = None

        # Removes head
        if self.head.data == node.data:
        	self.head = curr.next
        else:
	    	while curr != None:
	            if curr.data != node.data:
	                prev = curr
	                curr = curr.next
	            else:
	                prev.next = curr.next
	                break

    # Time complexity of O(n)
    def remove_dups(self):
    	curr = self.head
        prev = None
        unique = []

    	while curr != None:
            if curr.data in unique:
                prev.next = curr.next
            else:
                unique.append(curr.data)
                prev = curr
            
            curr = curr.next

    # Time complexity of Quadric, O(n**2)
    # Space complexity of O(1)
    # def remove_dups_no_array_old(self):
    # 	curr = self.head
    # 	prevSecond = None

    # 	while curr != None:
    #         second = curr.next

    #         while second != None:
    #         	print "curr: " + str(curr.data) + " | " + " second: " + str(second.data)
    #         	if curr.data == second.data:
    #                 print "match"
    #                 prevSecond.next = second.next
    #         	else:
    #         		prevSecond = second

    #         	second = second.next
            
    #         curr = curr.next

    def remove_dups_no_array(self):
    	curr = self.head
    	while curr != None:
            second = curr
            while second.next != None:
            	if curr.data == second.next.data:
            		second.next = second.next.next
            	else:
            		second = second.next

            curr = curr.next

	                
node1  = Node(1)
node4  = Node(3)
node2  = Node(2)
node3  = Node(3)
node4b = Node(4)
node3b = Node(5)
node5 = Node(5)

my_list = LinkedList()
my_list.head = node1
my_list.insert(node4)
my_list.insert(node2)
my_list.insert(node3)
my_list.insert(node4b)
my_list.insert(node3b)
my_list.insert(node5)

# my_list.remove(node1)

print "Before:"
my_list.display()
# my_list.remove_dups()
my_list.remove_dups_no_array()
print "After:"
my_list.display()
