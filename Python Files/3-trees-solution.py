"""
Trees - Problem 1

Scenario is at the bottom.
"""

class BST:
    """
    Implement the Binary Search Tree (BST) data structure.  The Node 
    class below is an inner class.  An inner class means that its real 
    name is related to the outer class.  To create a Node object, we will 
    need to specify BST.Node
    """

    class Node:
        """
        Each node of the BST will have data and links to the 
        left and right sub-tree. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None


##############################################
################## CHANGES ###################
##############################################

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
            # We need to pass in the score as well for cleaner comparison
            self._insert(data, data.score, self.root)

    # Allow for score to be passed in.
    def _insert(self, data, score, node):
        """
        This function will look for a place to insert a node
        with 'data' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        """
        # We are comparing scores now
        if score == node.data.score:
            pass
        # We are comparing scores now
        elif score < node.data.score:
            
            if node.left is None:
                node.left = BST.Node(data)
            else:
                # Make sure you pass in the score again
                self._insert(data, score, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                node.right = BST.Node(data)
            else:
                # Make sure you pass in the score again
                self._insert(data, score, node.right)

##############################################
################## CHANGES ###################
##############################################



    def __contains__(self, data):
        """ 
        Checks if data is in the BST.  This function
        supports the ability to use the 'in' keyword:

        if 5 in my_bst:
            ("5 is in the bst")

        """
        return self._contains(data, self.root)  # Start at the root

    def _contains(self, data, node):
        """
        This funciton will search for a node that contains
        'data'.  The current sub-tree being search is 
        represented by 'node'.  This function is intended
        to be called the first time by the __contains__ function.
        """

        if data == node.data:
            return True
        
        elif data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                return False
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                return self._contains(data, node.left)
        elif data > node.data:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                return False
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                return self._contains(data, node.right)
        

    def __iter__(self):
        """
        Perform a forward traversal (in order traversal) starting from 
	    the root of the BST.  This is called a generator function.
        This function is called when a loop	is performed:

        for value in my_bst:
            print(value)

        """
        yield from self._traverse_forward(self.root)  # Start at the root
        
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
        
    def __reversed__(self):
        """
        Perform a formward traversal (in order traversal) starting from 
        the root of the BST.  This function is called when a the 
        reversed function is called and is frequently used with a for
        loop.

        for value in reversed(my_bst):
            print(value)

        """        
        yield from self._traverse_backward(self.root)  # Start at the root

    def _traverse_backward(self, node):
        """
        Does a backwards traversal (reverse in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the right
        side (thus getting the larger numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the left side (thus getting the smaller numbers last).

        This function is intended to be called the first time by 
        the __reversed__ function.        
        """
        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)

    def get_height(self):
        """
        Determine the height of the BST.  Note that an empty tree
        will have a height of 0 and a tree with one item (root) will
        have a height of 1.
        
        If the tree is empty, then return 0.  Otherwise, call 
        _get_height on the root which will recursively determine the 
        height of the tree.
        """
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)  # Start at the root

    def _get_height(self, node):
        """
        Determine the height of the BST.  The height of a sub-tree 
        (represented by 'node') is 1 plus the height of either the 
        left sub-tree or the right sub-tree (whichever one is bigger).

        This function intended to be called the first time by 
        get_height.
        """
        if node is None:
            return 0
        else :
            left = self._get_height(node.left)
            right = self._get_height(node.right)

            if (left > right):
                return left + 1
            else:
                return right + 1


# NOTE: This is not part of the BST class!

class TestResult:
    def __init__(self, name, score):
        """
        Initialize test result with given name and score.
        """
        self.name = name
        self.score = score

# Test Case
print("\n=========== PROBLEM 1 TEST ===========")
# Scenario: We had some people take a very important test
#           for us and we want to be able to quickly and
#           efficiently see the results with the person
#           having the highest score be displayed first.
# 
#           The TestResult class can be seen above. We can
#           see that each TestResult object will contain
#           two properties.
# 
#           Objective 1:
#           Modify the existing BST to sort the
#           results based on their score.
# 
#           Objective 2:
#           Insert your own code below to display the
#           results how we'd like them.

# Exepcted Result: Peter: 490
#                  David: 73
#                  Barb: 60
#                  Chris: 44
#                  Justin: 12


test1 = TestResult("Barb", 60)
test2 = TestResult("Chris", 44)
test3 = TestResult("David", 73)
test4 = TestResult("Justin", 12)
test5 = TestResult("Peter", 490)

results_tree = BST()
results_tree.insert(test1)
results_tree.insert(test2)
results_tree.insert(test3)
results_tree.insert(test4)
results_tree.insert(test5)


# insert code here
# Because of how the tree is implemented we can continue using the
# __iter__ functionality. In order for us to display the highest
# score first we need to add the reversed() call on our results_tree.
# This is not the only way to do this.
for result in reversed(results_tree):
    print(f"{result.name}: {result.score}")