"""PROBLEM 3"""


# Note: Your solution should have O(n) time complexity, where n is the number of elements in l, since
# this is what you will be asked to accomplish in an interview.
#
# You have a singly linked list l, which is sorted in strictly increasing order, and an integer
# value. Add value to the list l, preserving its original sorting.
#
# Note: in examples below and tests preview linked lists are presented as arrays just for simplicity
#     of visualization: in real data you will be given a head node l of the linked lis

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None

# Understand
# We have  a linked list that is strictly increasing order *
# insert value in while maininting this order

# Plan
# given the first element is the smallestet simply run a loop and compare wweather
# if value is > l[len(l)-1] then  l.append(len(l)-1,)
# if value is lower than current element insert number into the current index ; note: insert scoots everything
# to the right and takes O(n)
# if its greater than the current index and less than the next one then insert
# else continue

# if input is an array
def insertValueIntoSortedLinkedList(l, value):
    print(l)
    for index, num in enumerate(l):
        if index == (len(l) - 1) and value > l[len(l) - 1]:
            l.append(value)
        elif value < l[index]:
            l.insert(index, value)
        elif (index + 1) < len(l) and l[index + 1] > value and l[index] < value:
            l.insert(index + 1, value)
    return l


# input is a linked list
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def insertValueIntoSortedLinkedList(l, value):
    new_node = ListNode(value)

    if l is None or l.value >= value:
        # if new node is needed at the start of list
        new_node.next = l
        return new_node

    current = l

    while (current.next is not None) and current.next.value < value:
        current = current.next;
        # finding a node which has lesser value than new_node
        # but its successor should have greater (or equal) value
        # this will loop breaks once the input-value is > current .next value in LL

    # inserting new_node after current node
    new_node.next = current.next;  # the new_node.next becomes the next bigger the current above and is also bigger than the inptus
    # before the while loopp stoppped. and is also bigger has a corresponign value bigger than the input.
    current.next = new_node;  # current.next was point to bigg value but now is point to new node which less than that bigger value.

    return l


# Ex)
x = ListNode(1)
y = ListNode(2)
z = ListNode(3)

x.next = y
y.next = z

insertValueIntoSortedLinkedList(x, 4)

# Similar Problem:
# https://www.geeksforgeeks.org/given-a-linked-list-which-is-sorted-how-will-you-insert-in-sorted-way/
# def sortedInsert(self, new_node):
#     # Special case for the empty linked list
#     if self.head is None:
#         new_node.next = self.head
#         self.head = new_node
#
#     # Special case for head at end
#     elif self.head.data >= new_node.data:
#         new_node.next = self.head
#         self.head = new_node
#
#     else:
#
#         # Locate the node before the point of insertion
#         current = self.head
#         while (current.next is not None and
#                current.next.data < new_node.data):
#             current = current.next
#
#         new_node.next = current.next
#         current.next = new_node

# Test in python tutor: http://www.pythontutor.com/live.html#mode=edit

"""PROBLEM #4 - Merge 2 Linked Lists"""


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    # a dummy first node to hang the result on
    dummy = ListNode(0) # psuedo empty node

    # tail points to the last result node
    tail = dummy

    while l1 is not None and l2 is not None:
        # Compare the data of the two
        # lists whichever lists' data is
        # smaller, append it into tail and
        # advance the head to the next Node
        if l1.value <= l2.value: # were updating l2 and l2 as we get the tail
            tail.next = l1
            l1 = l1.next;

        else:
            tail.next = l2
            l2 = l2.next
        # eventually this tail will correspond to either to the last node in either l2 and l2
        # eventually l2 or l2 will become None as well
        tail = tail.next;

    # when the while loop terminates we want to connect the tail of either l2 or l2 to the head of l1 or l2
    if l1 is None:
        tail.next = l2
    if l2 is None:
        tail.next = l1
    # returns the new merged linked list excluding that inital value of 0 that we used to create the psudo node
    return dummy.next


# Resource:https://practice.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1



""""ATTEMPT#2"""
# Understand:
# Were given two linked lists (represented as lists)
# Two linked lists are given to use in non-decreasing order
# Want to merge and make sure that the new merged linked lists also maintains this nondecreasing order

# Plan:
#







# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None

def mergeTwoLinkedLists(l1, l2):














"""Problem #5 Potential Solution----REWORK"""


# https://leetcode.com/problems/reverse-nodes-in-k-group/solution/
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverseNodesInKGroups(l, k):
    """ :type head: ListNode
        :type k: int
        :rtype: ListNode
        Approach : convert all list elements to list,
    """
    values = list()
    # copy of input list to list
    while l:
        values.append(l.value)
        l = l.next

    split = len(values) % k
    print(split)

    if split > 0:
        end_values = values[-split:]  # from split to end will not undergo split
        values = values[:-split]  # till split (will undergo split operation)

    else:
        end_values = []  # all will undergo split

    print(end_values, values)

    # reversing k at a time in values
    for ndx in range(0, len(values), k):
        values[ndx:ndx + k] = values[ndx:ndx + k][::-1]  # reversing k

    values = values + end_values
    print(values)
    res = ListNode(values.pop())

    # building linked list in reverse
    while values:
        res = ListNode(values.pop())
        res.next = res  # append to the beginning of res in every iteration

    return res


# Potential Recursive Solution
# https://practice.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseNodesInKGroups(l, k):
    current = l
    next = None
    prev = None
    count = 0

    while (current is not None and count < k):
        # reversing k elements
        next = current.next  # storing value of next node
        current.next = prev  # reversing link
        prev = current  # updating prev
        current = next  # updating current
        count += 1

    if next is not None:  # checking if there are more nodes ahead
        l.next = reverseNodesInKGroups(next, k)  # reversing those recursively

    return prev
