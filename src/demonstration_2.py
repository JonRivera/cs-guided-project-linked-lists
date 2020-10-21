"""
Given a reference to the head node of a singly-linked list, write a function
that reverses the linked list in place. The function should return the new head
of the reversed list.

In order to do this in O(1) space (in-place), you cannot make a new list, you
need to use the existing nodes.

In order to do this in O(n) time, you should only have to traverse the list
once.

*Note: If you get stuck, try drawing a picture of a small linked list and
running your function by hand. Does it actually work? Also, don't forget to
consider edge cases (like a list with only 1 or 0 elements).*
"""

""" ATTEMPT #1"""
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse(head_of_list):
    current_node = head_of_list
    previous_node = None
    next_node = None

    # Until we have 'fallen off' the end of the list
    while current_node:
        # Copy a pointer to the next element
        # before we overwrite current_node.next
        next_node = current_node.next

        # Reverse the 'next' pointer
        current_node.next = previous_node

        # Step forward in the list
        previous_node = current_node
        current_node = next_node

    return previous_node


# https://www.geeksforgeeks.org/reverse-a-linked-list/

# ---------------------
""" Attempt #2 """


class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next = None


# Understand
# Want to create a function that reverses a known linked list
# Plan
# Traverse the linked list and change the connections:
# Traverse by performing a while loop
# Create 3 pointers:
# The current node represents the input

# Structure
# The next node represent the node that comes after current node
# we need this pointer to remmber what comes after the current before we over write it
""" next_node = current_node.next """
# We reverse the change the connection of currentnode.next to the previous pointer that was originally set to none
# This helps start the process of reversing the linked list as the head node will have a currentnode.next  pointing
# to a None node
"""current_node.next = previous_node"""
# The previous node keeps track of what came before we moved to the next node in the loop
# Its important to have this pointer b/c we need a way of remembering the previous current node
# This will ultimately help us continue reversing the linked list
"""previous_node = current_node"""
# As a final step in the while loop, we overwrite the current node to what comes after the original current node
# this will allows to move foward in the traversal
"""current_node = next_node"""


def reverse(head_node):
    current_node = head_of_list
    previous_node = None
    next_node = None

    # Until we have 'fallen off' the end of the list
    while current_node:
