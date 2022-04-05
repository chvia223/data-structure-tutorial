
# Queues

## Intro
Back in 2017, Apple celebrated the 10 year anniversary of their popular smartphone line by releasing the iPhone X. Because of all of the generated excitement, people queued up at Apple stores days in advance of the phone's release to be one of the first to purchase one. The first one in line was the first one to get an iPhone. Imagine if it wasn't like this. Imagine if the iPhones were given out in a stacking order instead. It would be madness.

In this scenario it is easy to recognize the value of a queue in it's operation and in this tutorial we'll explore how we can implement this data structure in our own code.

## General Operations and Efficiency

The Queue functions in a "First In, First Out" operation order. Like a line, the first thing in is the first thing to leave. We implement this in Python using a list and thus it's efficiency as a data structure is tied to that of a dynamic array.

| Operation      | Description                                 | Python Code               | Performance |
| -------------- | ------------------------------------------- | ------------------------- | ----------- |
| enqueue(value) | Adds "value" to the <br> back of the queue.  | ```queue.append(value)``` | O(1)        |
| dequeue()      | Two Options: <br> - Remove and return <br> the item form the <br> front of the queue. <br> - Pop off index 0 | ```value = queue[0]``` <br> ```del queue[0]``` <br> OR <br> ``` value = queue.pop(0) ``` | O(n)
| size()         | Return the size of the <br> queue.          | ```length = len(queue)``` | O(1)        |
| empty()        | Returns true if the <br> length of the queue <br> is zero. | ```if len(queue) == 0:``` | O(1)

<br>

When I listen to music on a music streaming app like Spotify I like to know what I'm listening to currently, but also what's coming up next. When Spotify organizes my streaming playlist it puts all of the songs in a queue. This streamlines for the user (and the software) what's coming next!

<br>

## Example Use Case

Let's go over how to add something and take something away from the queue.

First we need to use the `enqueue` method to add our data to the queue. Let's add a few things.

``` python
# We have to create our queue first!
our_queue = Queue()

our_queue.enqueue(1000)
our_queue.enqueue(12)
our_queue.enqueue(503)
```

Now let's see what's happening behind the scenes.
``` python
    def enqueue(self, value):
        """
        Add an item to the queue
        """
        self.queue.append(value)
```
It looks very similar to adding an item to the built in list data structure. They function very similar too.
<br>
<br>
Let's say our queue advanced and the next item in line now had to be removed and used. It is a very similar process.

``` python
value = our_queue.dequeue()
```
This will pull out the next item in the queue for us to use elsewhere in our program. Let's see how it works.

``` python
    def dequeue(self):
        """
        Remove the next item from the queue. 
        """
        value = self.queue[0]
        del self.queue[0]
        return value
```
We see that we are intializing a new value variable that will hold whatever is in the first spot of the queue. Then we make sure to delete that data from the queue so we don't double use the data. Once all of that is finished we need to return the value that was held there so it can be used outside of the queue.

<br>

## Problem Solving Time

Now we're going to put these principles in action in our own code. Linked below is a python file that starts us off, but needs some more work solving the problem. See if you can figure it out! :)

[Queues Problem](https://github.com/chvia223/data-structure-tutorial/blob/main/Python%20Files/1-queues-problem.py)

[Queues Solution](https://github.com/chvia223/data-structure-tutorial/blob/main/Python%20Files/1-queues-solution.py)

When you're finished or if you get stuck check the solution provided.

<br>


## Reasons to Use Queues

Now that we've gotten some practice using queues we should talk about why we should use them in our programming.

1. **Our order is guaranteed!** - We know that the order we put things in is the same order they will come out. Every time.

2. **Our data is more secure!** - As opposed to a traditional list or array, a queue's only mutability is a pop or a push.

3. **We have more control!** - If a user was going to make thousands of requests at a time your computer or server may crash. With a list we can put a limit on those requests and make sure they still happen in order.