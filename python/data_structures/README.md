# Data Structures:

## Linked-List

### Title:
Linked-List Insert, Includes, __str__

#### Date: 10-01-2023

#### Problem
Write classes to create Node and Linked Lists instances.
Create methods to insert, search if value exists and to return string representation of the linked list.

#### Approach & Efficiency
  * LinkedList.insert(value):
    * Time Complexity: O(1)
    * Space Complexity: O(1)
  * LinkedList.includes(value):
    * Time Complexity: O(n)
    * Space Complexity: O(1)
  * LinkedList.to_string()
    * Time Complexity: O(n)
    * Space Complexity: O(n)


### Title:
Linked-List-Insertions

#### Date:
10/05/2023

#### Problem
Create methods to delete a node,  insert a node at end of linked-list, insert a node before a node that matches a given value, and after the same matching node.

#### Whiteboard
![traverse-linked-list](./images/whiteboard_code-challenge-06.png)

#### Approach & Efficiency
  * LinkedList.append():
    * Time Complexity: O(n)
    * Space Complexity: O(1)
  * LinkedList.insert_before():
    * Time Complexity: O(n)
    * Space Complexity: O(1)
  * LinkedList.insert_after():
    * Time Complexity: O(n)
    * Space Complexity: O(1)
  * LinkedList.delete():
    * Time Complexity: O(n)
    * Space Complexity: O(1)


### Title:
Linked-List-Kth

#### Date:
10/06/2023

#### Problem
Find and return the kth from end node of the linked list.

#### Whiteboard
![linked-list-kth](./images/whiteboard_linked-list-kth2.png)

#### Approach & Efficiency
  * LinkedList.kth_from_end():
    * Time Complexity: O(n)
    * Space Complexity: O(n)


## Stack

### Title:
Stack

#### Date:
10/17/2023

#### Problem
Make class to handle the creation of stack instances and their maintenance.

#### Approach & Efficiency
  * Stack.push(value):
    * Time Complexity: O(1)
    * Space Complexity: O(1)
  * Stack.pop():
    * Time Complexity: O(1)
    * Space Complexity: O(1)
  * Stack.peek():
    * Time Complexity: O(1)
    * Space Complexity: O(1)
  * Stack.is_empty():
    * Time Complexity: O(1)
    * Space Complexity: O(0)

## Queue

### Title:
Queue

#### Date:
10/17/2023

#### Problem
Make class to handle the creation of queue instances and their maintenance.

#### Approach & Efficiency
  * Queue.enqueue(value):
    * Time Complexity: O(1)
    * Space Complexity: O(1)
  * Stack.dequeue():
    * Time Complexity: O(n)
    * Space Complexity: O(1)
  * Stack.peek():
    * Time Complexity: O(1)
    * Space Complexity: O(1)
  * Stack.is_empty():
    * Time Complexity: O(1)
    * Space Complexity: O(0)


## Binary Tree

### Title:
Binary Tree

#### Date:
11/4/2023

#### Problem
Make a class that can create and manage a binary tree. Must have methods to traverse the tree in a 'pre','post',and 'in'-order traversal; returning a list of the trees contents.

Also create a new Node class that has the attributes of 'value','left','right','count',and 'height'. These last two properties will come in handy for Binary Search Tree methods.

### Whiteboard
![binary tree whiteboard](./images/whiteboard_binary-tree.png)

#### Approach & Efficiency
  * BinaryTree.pre_order(value):
    * Time Complexity: O(N)
    * Space Complexity: O(N)
  * BinaryTree.in_order(value):
    * Time Complexity: O(N)
    * Space Complexity: O(N)
  * BinaryTree.post_order(value):
    * Time Complexity: O(N)
    * Space Complexity: O(N)

## Binary Search Tree

### Title:
Binary Search Tree

#### Date:
11/4/2023

#### Problem
Make a class that can create and manage a binary search tree while inheriting from the binary tree class. Must have a method to check if value exists in tree and another method add to binary search tree while maintaining balance and allow for duplication.

### Whiteboard

#### Whiteboard for 'contains' method
![binary search tree contains whiteboard](./images/whiteboard_binary-search-tree-contains.png)

#### Whiteboard for 'add' method
![binary search tree add whiteboard](./images/whiteboard_binary-search-tree-add.png)

#### Approach & Efficiency
  * BinarySearchTree.contains(value):
    * Time Complexity: O(N)
    * Space Complexity: O(1)
  * BinaryTree.add():
    * Time Complexity: O(N)
    * Space Complexity: O(1)

## Binary Tree method Find Maximum Value

### Title:
Find Maximum Value

#### Date:
11/5/2023

#### Problem
Write another class method to the Binary Tree class that will return the maximum value of any instance of the class. Assume that tree only contain numerical values.

### Whiteboard

#### Whiteboard for 'find_maximum_value' method
![binary tree find-maximum-value whiteboard](./images/whiteboard_binary-tree-max-value.png)

#### Approach & Efficiency
  * BinaryTree.find_max_value():
    * Time Complexity: O(N)
    * Space Complexity: O(1)







