"""
Linked Lists - Problem 1

Scenario: 
One of the best places to find a linked list is in the implementation of a queue. One of the best places to find queues
in your music playing app. In this problem we are going to simulate the apps functionality. 

Because we are using the built in linked list data structure we will be focussing more on how to use each of the available
linked list methods described in the tutorial. If you are ever stuck please feel free to reference that or the solution.
"""
from collections import deque as linked_list

"""
Here is a list of the top 25 singles of 2021 as a reference:

1 - "Levitating" - Dua Lipa
2 - "Save Your Tears" - The Weeknd & Ariana Grande
3 - "Blinding Lights" - Then Weeknd
4 - "Mood" - 24kGolden
5 - "Good 4 U" - Olivia Rodrigo
6 - "Kiss Me More" - Doja Cat
7 - "Leave The Door Open" - Silk Sonic
8 - "Drivers License" - Olivia Rodrigo
9 - "Montero (Call Me By Your Name)" - Lil Nas X
10- "Peaches" - Justin Bieber
11- "Butter" - BTS
12- "Stay" - The Kid Laroi
13- "Deja Vu" - Olivia Rodrigo
14- "Positions" - Ariana Grande
15- "Bad Habits" - Ed Sheeran
16- "Heat Waves" - Glass Animals
17- "Without You" - The Kid Laroi
18- "Forever After All" - Luke Combs
19- "Go Crazy" - Chris Brown
20- "Astronaut in the Ocean" - Masked Wolf
21- "34+35" - Ariana Grande
22- "What You Know Bout Love" - Pop Smoke
23- "My Ex's Best Friend" - Machine Gun Kelly
24- "Industry Baby" - Lil Nas X
25- "Therefore I Am" - Billie Eilish

"""


music_queue = linked_list()

# Test Cases

# Test 1
# Scenario: There are already a few songs in the queue. They are all good, but you wanted to listen to
#           "Drivers License" by Olivia Rodrigo next without getting rid of the songs in the current
#           queue. What would the code for that funcitonality look like.

# Exepcted Result: Drivers License, Deja Vu, Bad Habits, What You Know Bout Love
print("Test 1")
print("=====================")
music_queue.append("Deja Vu")
music_queue.append("Bad Habits")
music_queue.append("What You Know Bout Love")

# #####################
# type code here.
# #####################



# Iterates through the linked list in order from head to tail.
while len(music_queue) != 0:
    value = music_queue.popleft()
    print(value)

print("=====================")
print()
music_queue.clear()


# Test 2

# Scenario: You looked at you song queue another time you listen to music and you notice that you'd rather listen
#           to "Therefore I Am" to the second in the list instead of "Peaches". How would you implement that given
#           the current list.  

# Exepcted Result: Without You, Therefore I Am, Peaches, Butter, Mood
print("Test 2")
print("=====================")
music_queue.append("Without You")
music_queue.append("Peaches")
music_queue.append("Save Your Tears")
music_queue.append("Therefore I Am")
music_queue.append("Mood")

# #####################
# type code here.
# #####################



# Iterates through the linked list in order from head to tail.
while len(music_queue) != 0:
    value = music_queue.popleft()
    print(value)

print("=====================")
print()
music_queue.clear()


# Test 3
# Scenario: You've been adding a lot of songs to your music queue recently and now you're just curious how many songs
#           you've got in there. How would we be able to output that number

# Exepcted Result: 6
print("Test 3")
print("=====================")
music_queue.append("Astronaut in the Ocean")
music_queue.append("Peaches")
music_queue.append("Forever After All")
music_queue.append("Leave The Door Open")
music_queue.append("Industry Baby")
music_queue.append("Heat Waves")

# #####################
# type code here.
# #####################



print("=====================")
print()