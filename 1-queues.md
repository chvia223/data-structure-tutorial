
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

## Example Use Case

When I listen to music on a music streaming app like Spotify I like to know what I'm listening to currently, but also what's coming up next. When Spotify organizes my streaming playlist it puts all of the songs in a queue. This streamlines for the user (and the software) what's coming next!

## Problem Solving Time

Now we're going to put these principles in action in our own code. Linked below is a python file that starts us off, but needs some more work solving the problem. See if you can figure it out! :)

[Queues Problem]()



## Reasons to Use Queues

Now that we've gotten some practice using queues we should talk about why we should use them in our programming.

1. **Our order is guaranteed!** - We know that the order we put things in is the same order they will come out. Every time.

2. **Our data is more secure!** - As opposed to a traditional list or array, a queue's only mutability is a pop or a push.

3. **We have more control!** - If a user was going to make thousands of requests at a time your computer or server may crash. With a list we can put a limit on those requests and make sure they still happen in order.