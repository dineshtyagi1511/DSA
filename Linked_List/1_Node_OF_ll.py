class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

first = Node(1)
second = Node(2)
third = Node(3)

print(f"id of first:{id(first)}")
print(f"id of second:{id(second)}")
print(f"id of third :{id(third)}")


first.next = second
second.next = third 

head= first

print(head.data)
print(first.data)
print("#########")
print(head.next.data)
print(second.data)
print("#########")
print(head.next.next.data)
print(third.data)