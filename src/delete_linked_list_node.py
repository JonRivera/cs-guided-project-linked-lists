"""
Given only a reference to a specific node in a linked list, delete that node from a singly-linked list.

Example:

The code below should first construct a linked list (x -> y -> z) and then delete `y` from the linked list by calling the function `delete_node`. It is your job to write the `delete_node` function.

```python
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z

delete_node(y)
```

*Note: We can do this in O(1) time and space! But be aware that our solution will have some side effects...*
"""


class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next = None


def delete_node(node_to_delete):
    # Your code here
    # check if `node_to_delete` is the last node in the ll 
    if node_to_delete.next is None:
        # traverse to the node right before the tail so that we can 
        # change its next reference 
        # this isn't possible because we don't have access to the head
        # if ur the last node-can't access the node that comes before the present without having to reference the entire linked list, so
        # if ur just give  node itself, u can only delete if you have pointer to a another node
        raise Exception("This function can't delete the tail")
    else:
        # change our `node_to_delete`'s value to be its next's value 
        node_to_delete.value = node_to_delete.next.value  # basically copies the node that comes after)
        # change our `node_to_delete`'s next to refer to its next's next
        # `1````v(changes the pointer to next next b/c the above code copies the next node)
        node_to_delete.next = node_to_delete.next.next


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


x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z

delete_node(y)

print_ll(x)
