class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z

y.prev = x
z.prev = y


def print_ll_reverse(tail):
    current = tail

    while current is not None:
        # print(current.value)
        current = current.prev


# traverse a linked list and print value of each node
def print_ll(head):
    # init a new variable to refer to the node we have 
    # access to 
    current = head

    # use while loop to keep traversing until our 
    # `current` variable falls off the tail of the ll 
    while current is not None:
        print(current.value)
        # update our `current` variable to refer to the 
        # next node in the ll 
        current = current.next


print_ll_reverse(z)
