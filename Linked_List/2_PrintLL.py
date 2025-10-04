class Node:
    def __init__(self,value):
        self.data = value
        self.next = None 

first= Node(1)
second= Node(2)
third= Node(3)

first.next = second
second.next = third 

head = first 
def PrintLL(head):
    temp = head 
    while temp!=None:
        print(temp.data)
        temp =temp.next

PrintLL(head)