# Trees

## Intro
When we look at trees in real life we can see that, starting at the base, there are many different ways that it will branch off whether you're looking up or down. Each branch will take us down a different path that may contain different fruits or leaves. This is very similar to the `Tree` data structure that we will be studying. It is much like a linked list in that each piece of data is linked and points to a node. What makes them different is how all that data is being linked.
<br>
<br>

## General Operations and Efficiency
The trunk of our `Tree` is call the root and this is the starting value that all things will be compared to when sorting out their branches. Every node that comes after it is called a child and is stored at a different "level" in the tree. If we're at a child node and we want to look at a node up a level we call it the parent of that node. If there is a child node that connects to no other nodes then it is referred to as a leaf.

For the sake of simplicity in this tutorial we'll be focusing on only one implementation of trees. It is the `Binary Search Tree`. What separates this from a traditional tree is that there can only ever be two children to each node thus the binary naming. When a node is added to the tree it recusively compares it's value to nodes that are already in the tree starting at the root. If the value is found to be less than then the node travels to the left of the compared value otherwise it moves right. If the value is equal then there will need to be a programmed exception for it depending on the implementation of the tree.

Common Binary Search Tree Methods are:

| Operation            | Description                                 | Python Code                   | Performance |
| --------------       | ------------------------------------------- | -------------------------     | ----------- |
| insert(value)        | Insert a value into the tree.      | ```BST.insert(value)```    | O(log n)        |
| remove(value)        | Removes a value from the tree.       | ```BST.remove(value)```        | O(log n)        |
| contains(value)      | Determine if a value is in the tree. | ```if BST.contains(value):``` | O(log n)        |
| traverse_forward()   | Visit all objects from smallest to largest.  | ```for data in BST:```    | O(n)        |
| traverse_reverse()   | Visit all objects from largest to smallest.   | ```for data in reversed(BST)```         | O(n)        |
| height(node)         | Determine the height of a node. If the <br> height of the tree is needed, the root <br> node is provided.  | ```height = BST.height(node)```           | O(n)        |
| size()               | Return the size of the BST. | ```length = BST.size()```        | O(1)        |
| empty()              | Returns true if the root node is empty. <br> This can also be done by checking the <br> size for 0. | ```if BST.empty():``` | O(1)        |

<br>

## Example Use Case

We're just going to practice displaying the data from a tree.

First, we'll need to populate our tree.

``` python
BST.insert(3)
BST.insert(10)
BST.insert(7)
BST.insert(8)
BST.insert(5)
```
What's happening behind the scenes isn't too complex. We start by checking if something has been set to the root yet. If it hasn't then we want to make sure that the first thing we add goes there.
``` python
def insert(self, data):
        """
        Insert 'data' into the BST.  If the BST
        is empty, then set the root equal to the new 
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)
```
Then if the root is populated we want to called the _insert method. For this implementation, if the data is duplocated then we don't want it to be added at all. If it's not a duplicate then we'll move on to check which side of the node the data will become a child in. If it finds that there isn't an existing node in that spot then the data gets set there. Otherwise the _insert method gets called again recursively and makes the check on the next level down the tree.
``` python
    def _insert(self, data, node):
        """
        This function will look for a place to insert a node
        with 'data' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        """
        if data == node.data:
            pass
        elif data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)
```
<br>
Now, to iterate through our Binary Search Tree we can do so the same way as other, standard data structures in Python.

``` python
for data in BST:
    print(data)
```
This is possible because we did an override on the default `__iter__` method to call the `_traverse_forward` method we defined inside the class.
``` python
def _traverse_forward(self, node):
        """
        Does a forward traversal (in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the left
        side (thus getting the smaller numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the right side (thus getting the larger numbers last).

        The use of the 'yield' will allow this function to support loops
        like:

        for value in my_bst:
            print(value)

        The keyword 'yield' will return the value for the 'for' loop to
	    use.  When the 'for' loop wants to get the next value, the code in
	    this function will start back up where the last 'yield' returned a 
	    value.  The keyword 'yield from' is used when our generator function
        needs to call another function for which a `yield` will be called.  
        In other words, the `yield` is delegated by the generator function
        to another function.

        This function is intended to be called the first time by 
        the __iter__ function.
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
```
What is happening is we are moving all the way to left of our tree first to make sure we get the lowest data value and then we yield it to iterator to use. As we iterate we move on to the right moving up and down the levels of the tree. This ensures that the data is displayed in the order that it has been sorted.

<br>

## Problem Solving Time

Now we're going to use a `Binary Search Tree` to solve a problem. Because of it's difficulty there will only be one problem to solve. Take your time with it and if you get stuck or finish please check the solution's answer.

[Trees Problem](https://github.com/chvia223/data-structure-tutorial/blob/main/Python%20Files/2-linked-lists-problem.py)

[Trees Solution](https://github.com/chvia223/data-structure-tutorial/blob/main/Python%20Files/2-linked-lists-solution.py)

<br>

## Reasons to Use a Binary Search Tree Instead of a Linked List
1. **Automatic Sorting** - This can be a big one. When things get added to a binary search tree they will be sorted typically from smallest to largest, but can be designed to sort in whatever way you need. This will happen as it's added so when you need to interate through the data it is all ready for you.

2. **Better Performance** - This comes with a big caveat. You need to make sure there is a mechanism in your BST that will balance your tree as things are getting added. Since a comparison is only evaluated for each level you go down, balancing will reduce the amount of level and therefore make things more efficient. If there was no balancing than the worse case scenario would be equal in efficency to a linked list.



<br>