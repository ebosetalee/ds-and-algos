# __Data Structures and Algorithms__

__Data structure__ is a programmatic way of collecting, storing and organizing data. 
Anything that can store data can be called as a data structure, hence Integer, Float, Boolean, Char etc, all are data structures. They are known as __Primitive Data Structures__.

In this repository, the following are the __Abstract types of data structures__:
1. Linked List
2. Doubly Linked List
3. Queue
4. Stack
5. Hash Table
6. Tree

__Basic Operations:__

The data in the data structures are processed by certain operations that needs to be performed, such as:
 - Traversing; 
 - Searching;
 - Insertion; 
 - Deletion; 
 - Sorting.
 
## __LINKED LIST__
Linked List is a sequence of links which contains items. Each link contains a connection to another link. The important terms to understand the concept of Linked List are:
- _Link_ − Each link of a linked list can store a data called an element.
- _Next_ − Each link of a linked list contains a link to the next link called Next.

__Types of Linked List__
1. Simple Linked List − Item navigation is forward only.
2. Doubly Linked List − Items can be navigated forward and backward.

__Basic Operations:__
1. Insertion − Adds an element at the beginning of the list.
2. Deletion − Deletes an element at the beginning of the list.
3. Display − Displays the complete list.
4. Search − Searches for an element using the given key.
5. Delete − Deletes an element using the given key.
6. Reverse - Moves the head list to the last node.

### SIMPLE / LINEAR LINKED LIST
__Linear Linked list__ is the default linked list and a linear data structure in which data is not stored in contiguous memory locations but each data node is connected to the next data node via a pointer, hence forming a chain.

- __The element in such a linked list can be inserted in 2 ways:__
    - Insertion at beginning of the list.
    - Insertion at the end of the list.

![linearlinkedlist](https://upload.wikimedia.org/wikipedia/commons/6/6d/Singly-linked-list.svg)

- __Time Complexities:__

traverse | Search | Insert | Delete
-----    | -----  | -----  | ----- 
 O(n)    | O(n)   | O(1)   | O (n)
 
- __Space Complexities:__
O(n)
 
### __DOUBLY LINKED LIST__
__Doubly Linked List__ is a variation of Linked list whereby navigation is possible in both ways, either forward and backward easily as compared to Single Linked List. 
The important terms to understand the concept of doubly linked list which linked lists don't have are:
1. _Prev_ − Each link of a linked list contains a link to the previous link called Prev.
2. _LinkedList_ − A Linked List contains the connection link to the first link called First and to the last link called Last.

![doublylinkedlist](https://upload.wikimedia.org/wikipedia/commons/5/5e/Doubly-linked-list.svg)

- __Other Basic Operations:__
1. Insert Last − Adds an element at the end of the list.
2. Delete Last − Deletes an element from the end of the list.
3. Display forward − Displays the complete list in a forward manner.
4. Display backward − Displays the complete list in a backward manner.

- __Time Complexities:__

traverse | Search | Insert | Delete
-----    | -----  | -----  | ----- 
 O(n)    | O(n)   | O(1)   | O (n)
 
- __Space Complexities:__
O(n)

- __NODE:__
A Node in a linked list holds the data value and the pointer which points to the location of the next node in the _linked list_. 
In other words, it is a data value and a pointer (pointing to the next node) put together.


## __QUEUE__
Queue is an abstract data structure, somewhat similar to Stacks. Unlike stacks, a queue is open at both its ends. 
One end is always used to insert data (enqueue) and the other is used to remove data (dequeue). 
Queue follows __First-In-First-Out__ methodology, i.e., the data item stored first will be accessed first.

![queue](https://upload.wikimedia.org/wikipedia/commons/5/52/Data_Queue.svg)

__Basic Operations:__
1. `enqueue()` − add (store) an item to the queue.
2. `dequeue()` − remove (access) an item from the queue.
3. `peek()` − Gets the element at the front of the queue without removing it.
4. `isfull()` − Checks if the queue is full.
5. `isempty()` − Checks if the queue is empty.

- __Time Complexities:__

traverse | Search | Enqueue| Dequeue
-----    | -----  | -----  | ----- 
 O(n)    | O(n)   | O(1)   | O (1)
 
- __Space Complexities:__
O(n)


## __STACK__
__Stack__ is an abstract data type with a bounded(predefined) capacity. 
It is a simple data structure that allows adding and removing elements in a particular order.

![stack](https://www.notion.so/image/https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fb%2Fb4%2FLifo_stack.png?table=block&id=05f99432-9e8e-477c-a676-eaa902cf7190&width=2640&userId=cd51252f-d7d9-4c13-931d-9d4740803e48&cache=v2)

- __Basic Operations:__
1. Stack is an ordered list of similar data type.
2. Stack is a __LIFO(Last in First out)__ structure or we can say FILO(First in Last out).
3. `push()` function is used to insert new elements into the Stack and `pop()` function is used to remove an element from the stack. Both insertion and removal are allowed at only one end of Stack called __Top__.
4. Stack is said to be in Overflow state when it is completely full and is said to be in Underflow state if it is completely empty.

- __Time Complexities:__

traverse | Search | push   | pop
-----    | -----  | -----  | ----- 
 O(n)    | O(n)   | O(1)   | O (1)
 
- __Space Complexities:__
O(n)


## __HASH TABLE__
A hash table (hash map) is a data structure which implements an associative array abstract data type, a structure that can map keys to values. 
A hash table uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

Ideally, the hash function will assign each key to a unique bucket, but most hash table designs employ an imperfect hash function, 
which might cause hash collisions where the hash function generates the same index for more than one key. Such collisions must be accommodated in some way.

- __Hash Algorithm:__
1. input the string argument n
2. find the ascii value of each character in n
3. add the ascii values as value
4. return the remainder of value divided by 1000 

![hash](https://upload.wikimedia.org/wikipedia/commons/7/7d/Hash_table_3_1_1_0_1_0_0_SP.svg)

- __Hash function:__
```
Start
input "Raymond"
R = 82, a = 97, y = 121, m = 109, o = 111, n = 110, d = 100
82 + 97 + 121 + 109 + 111 + 110 + 100 = 730
return 730 % 1000 = 730
End
```

- __In code:__
```py
def awesome_hash_func(value=None):
    # do awesome stuff here
    return awesome_hash_value

hash_value = awesome_hash_func("raymond")
print(hash_value) # prints 730
```

__Basic Operations:__ 
1. `get` - Searches for the key using a given element or value.
2. `set`- Adds an element to the table using the key;
3. `delete` - Deletes an element or value and its key using the given element;
4. `has` - Searches if the key is in the table using the given key;
5. `hash` - Creates the hash key;
6. `get_keys` - Displays the elements or values in the table.

- __Time Complexities:__

traverse | Search | Insert | Delete
-----    | -----  | -----  | ----- 
 N/A     | O(1)   | O(1)   | O (1)
 
- __Space Complexities:__
 O(n)


__An Important point to note is Hash Collision.__

### __Hash Collision:__
This occurs when a hash function maps two different keys to the same table address, a collision is said to occur.
This is solved by giving the second element a different key to a different table address; involves re-hashing either by 
 - __linear probing:__
    A simple re-hashing scheme in which the next slot in the table is checked on a collision. OR
 - __quadratic probing:__
    A re-hashing scheme in which a higher (usually 2nd) order function of the hash index is used to calculate the address.

![hash_collision](https://upload.wikimedia.org/wikipedia/commons/d/d0/Hash_table_5_0_1_1_1_1_1_LL.svg)


## __TREE__
A tree is a widely used abstract data type (ADT) that simulates a hierarchical tree structure, with a root value and subtrees of children with a parent node, represented as a set of linked nodes.
It is used mostly for representing hierarchical information.

A tree data structure can be defined recursively (locally) as a collection of nodes (starting at a root node), where each node is a data structure consisting of a value, together with a list of references to nodes (the "children"), with the constraints that no reference is duplicated, and none points to the root.

__Terminologies:__
- Root Node - The topmost node in a tree and will not have a parent. 
- Nodes - A node is a structure which may contain a value or condition, or represent a separate data structure
- Leaf Nodes - Any node that does not have child nodes.
- Parents - A node that has a child is called the child's parent node. A node has at most one parent, but possibly many ancestor nodes, such as the parent's parent.
- Children 
- Ancestor - A node reachable by repeated proceeding from child to parent.
- Levels 

![tree](https://upload.wikimedia.org/wikipedia/commons/f/f7/Binary_tree.svg)

- __Time Complexities:__

traverse   | Search    | Insert    | Delete
-----      | -----     | -----     | ----- 
 O(log(n)) | O(log(n)) | O(log(n)) | O(log(n))
 
- __Space Complexities:__
O(n)

## __ACKNOWLEDGEMENT__
Once again I thank [@jirevwe](https://github.com/jirevwe) and [@yudori](https://github.com/yudori) for helping me, ensuring it's python-like and most importantly the encouragement.
Lastly, I thank the 8 people that saw this repo and gave it a star, I'm still blushing. Thank you....

For more details on data structures and more on what I did and didn't do check this repo [@ebosetalee - Understanding Python](https://github.com/ebosetalee/Understanding-Python/tree/master/data_structure)