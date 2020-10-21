"""Constructing Node and Linked list
https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/?ref=lbp


"""


# Node class
class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class
class LinkedList:

    # Function to initialize the Linked List object
    def __init__(self):
        self.head = None

    # This function is in LinkedList class
    # Function to insert a new node at the beginning
    def push(self, new_data):
        # 1 & 2: Allocate the Node &
        #	 Put in the data
        new_node = Node(new_data)

        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node


""" 
Reverse Linked List Problem
 https://leetcode.com/problems/reverse-linked-list/submissions/

Reverse a singly linked list.
Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev_node = None  # will ultimately be our last node;thinking backwards
        curr_node = head
        while curr_node:
            next_node = curr_node.next  # Remember next node
            curr_node.next = prev_node  # REVERSE! None, first time round.--> (whatever current node ur in, the curr_node
            # .next will correspond to what came before it in the linked list, in this case it head==none)
            prev_node = curr_node  # Used in the next iteration-> prep for the next reversal.
            curr_node = next_node  # Move to next node.
        head = prev_node
        return head


""" PROBLEM REVERSING LINKLIST Given Parameter M and N"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# understand were aiming to reverse the linked list givem the paramaters m and n
# create a pointer to the reverse list, and have a pointer that keeps track of the current head
# have a counter that keeps track of the current position if counter ==m or <=n
# run the while loop until counter > n
# add the last link back into the reverse list


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        # Empty list
        if not head:
            return None

        # Move the two pointers until they reach the proper starting point
        # in the list.
        cur, prev = head, None  # head is use as a dummy variable which be replaced by the mth element
        while m > 1:  # from starting position up to m; We keep progressing the two pointers in this way until
            # the cur pointer reaches the mth node
            prev = cur  # cur represents the head that we started with and thats it
            cur = cur.next  # cur becomes the next next node, this revers the order up mth
            m, n = m - 1, n - 1  # when m becomes 1 n-1 represents how many nodes were going to traverse internally to
            # reverse the internal order
            print(m, n)

        # The two pointers that will fix the final connections.
        tail, con = cur, prev

        # Iteratively reverse the nodes until n becomes 0.
        while n:
            # print(n)
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1
            print(n)

        # Adjust the final connections as explained in the algorithm
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head


"""PROBLEM Print Out Linked List Nodes"""

# Linked List Implementation I
# With the Node in hand, we can start building the actual linked list.
# Depending on the end-use of the linked list, a variety of methods can be defined.
#
# For our use, we want to be able to:
# get the head node of the list (it’s like peeking at the first item in line)
# add a new node to the beginning of the list
# print out the list values in order
# remove a node that has a particular value
# Let’s get started!
# Note: Because the workspace is set up with spaces instead of tabs, you will need to use spaces to prevent
# Python from throwing an error. You can learn more about this here.
#
# Instructions
# 1.
# Within script.py in the pane to the right, create an empty LinkedList class.
#
# Define an .__init__() method for the LinkedList. We want to be able to instantiate a LinkedList with a head node,
# so .__init__() should take value as an argument. Make sure value defaults to None if no value is provided.
#
# Inside the .__init__() method, set self.head_node equal to a new Node with value as its value.
#
# Checkpoint 2 Passed
#
# Stuck? Get a hint
# 2.
# Define a .get_head_node() method that helps us peek at the first node in the list.
#
# Inside the method, return the head node of the linked list.

# We'll be using our Node class
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


# Our LinkedList class
class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)  # initializing attributes

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)  # instanting a Node to a variable
        new_node.next_node = self.head_node
        self.head_node = new_node  # replacing a field/attribute

    # Add your insert_beginning and stringify_list methods below:
    def stringify_list(self):
        string_list = ""
        current_node = self.head_node
        while current_node != None:
            string_list += str(current_node.value) + "\n"
            current_node = current_node.next_node
        return string_list


# Test your code by uncommenting the statements below - did your list print to the terminal?
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())


"""PROBLEM REMOVE ARBITRARY Node corresponding to some data value"""

# Nice! Now we have a bunch of helpful LinkedList methods under our belt.
#
# The final use case we mentioned was the ability to remove an arbitrary node with a
# particular value. This is slightly more complex, since a couple of special cases need to be handled.
#
# Consider the following list:
#
# a -> b -> c
# If node b is removed from the list, the new list should be:
#
# a -> c

# We'll be using our Node class
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


# Our LinkedList class
class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

    # Define your remove_node method below:
    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None  # just a pointer
                else:
                    current_node = next_node