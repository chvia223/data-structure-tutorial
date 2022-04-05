# Linked-Lists

## Intro
Linked Lists are a tricky Data Structure. On top, they are very similar to a normal array that you've probably already used at this point. It's under the hood that they become very different. When you store data in an array then address in memory for each element can be found right next to each other. This can be useful when you're using small data sets that can fit on one page of memory, but that is beyond the scope of this tutorial. A ```Linked List``` on the other hand is able to store each element of data at a random address in memory. It does this by creating pointers to each consecutive element so instead of looking at their neighbor, a linked list element looks at whatever address it was told the next element should be at.

## General Operations and Efficiency

Python has a built in linked list data structure called the ```deque```. We will be using that premade data structure in our practice problem. Here is a list of the functions that are available to us: 

| Operation            | Description                                 | Python Code                   | Performance |
| --------------       | ------------------------------------------- | -------------------------     | ----------- |
| insert_head(value)   | Adds "value" before the head.      | ```linked_list.appendleft(value)```    | O(1)        |
| insert_tail(value)   | Adds "value" after the tail.       | ```linked_list.append(value)```        | O(1)        |
| insert(index, value) | Adds "value" after node "index"    | ```linked_list.insert(index, value)``` | O(n)        |
| remove_head()        | Removes the first item (the head)  | ```value = linked_list.popleft()```    | O(1)        |
| remove_tail()        | Removes the last item (the tail)   | ```value = linked_list.pop()```        | O(1)        |
| remove(index)        | Removes node "index"               | ```del linked_list[index]```           | O(n)        |
| size()               | Return the size of the linked list | ```length = len(linked_list)```        | O(1)        |
| empty()              | Returns true if the length of the <br> linked list is zero | ```if len(linked_list) == 0:``` | O(1)        |

<br>

For most of your smaller sized projects you will be able to use a normal dynamic or static array and be fine, but if we are ever in a scenario where data needs to be collected and stored as fast as possible, but not necessarily retrieved at that same fast speed then a Linked List will be more beneficial for you to use. For example, if you were write embedded software for a high speed camera and wanted to make sure that each frame was store in order and as fast as possible you may consider a Linked List in your implementation, especially if you don't already know how long the camera operator is going to be shooting for.

<br>


## Example Use Case

We're going to look at how things are added to linked lists.

First, we'll need to call the appropriate method to add data to a new node to the tail.
``` python
from collections import deque as linked_list

our_list = linked_list()

our_list.append("Italy")
```
<br>
What's happening behind the scenes?

``` python
def insert_tail(self, value):
    """
    Insert a new node at the back (i.e. the tail) of the 
    linked list.
    """
    new_node = LinkedList.Node(value)

    if self.tail is None:
        self.head = new_node
        self.tail = new_node
    else:
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

```
This function acts in a similar way to the `append` method found in the built in Python linked list. First a new node is created that will hold the data we passed in. Then we check if the current linked list is empty. If it is then what we pass in becomes the head and the tail because it is the only value found. Otherwise, we set the old tail to our new node's previous pointer. Then we set the old tail's next pointer to the new node. Then we set the tail of the linked list to the new node. After all of that we have a new node added to our list.

<br>

## Problem Solving Time

Now we're going to try using the Linked List to solve some problems. Click on the link below and try your best. When you finish or if you get stuck make sure to take a look at the provided solution.

[Linked Lists Problem](https://github.com/chvia223/data-structure-tutorial/blob/main/Python%20Files/2-linked-lists-problem.py)

[Linked Lists Solution](https://github.com/chvia223/data-structure-tutorial/blob/main/Python%20Files/2-linked-lists-solution.py)

<br>


## Reasons to Use Linked Lists over Arrays

Now that we've gotten some practice using Linked Lists we should talk about what makes them useful in our programming.

1. **What if you don't know how long your list is going to be?** - If your data storage is sensitive and you don't know how much you're going to need to store at compile time a linked list may be more performant depending on the size of the data you are collecting. If a dynamic array gets too big then it will need to spend operations realocating a larger array in memory.

2. **Random access isn't important to your program's implementation.** - Where the linked list falls behind an array is accessing elements that aren't at the beginning or end of the list. If you don't need to access an elements that would be in between the beginning or end then it would be more performant to implement a linked list.

3. **What if you need to add a lot of data in the middle of your list?** - The linked list is able to add elements in the middle of the list faster than an array because it only needs to change the pointers of the element's new neighbors. An array, on the other hand, would need to change the index of each element found after the one you added.
