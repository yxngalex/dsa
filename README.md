# Data Structures and Algorithms in Python

Welcome to my repository dedicated to learning and implementing core **Data Structures and Algorithms (DSA)** using
Python.

This project is built as a study aid, interview preparation tool, and personal reference.

To check how the implementation works of each Data Structure, open a Custom(Structure).py to view the code.

---

## Big O Notation

Big O Notation is a way to describe the **performance** or **complexity** of an algorithm. It expresses how the runtime
or space requirements of an algorithm grow relative to the input size. Big O helps us understand which algorithm is more
efficient as inputs become large.

Common complexities include:

- **O(1)** – Constant time
- **O(log n)** – Logarithmic time
- **O(n)** – Linear time
- **O(n log n)** – Linearithmic time
- **O(n²)** – Quadratic time
- **O(2ⁿ)** – Exponential time

Below are visual resources to help illustrate this concept:

![Big O Graph](images/BigO_Graph.png)
![Big O Table](images/BigO-table.JPG)
![Big O Cheatsheet](images/BigO-cheat-sheet.png)

---

## Project Structure

- Each data structure or algorithm is organized in its own directory.
- Where applicable, example usage and test files are included.
- All illustrations are located in the `images/` folder.

---

## Arrays

Covers fundamental array operations:

- Insertion and deletion
- Searching and sorting
- Rotation and reversal

---

## Hash Tables

Includes implementations of:

- Hash Table with Separate Chaining
  Covers operations like:
- Insertion and deletion
- Key lookup
- Collision handling

---

## Linked Lists

Includes implementations of:

- Singly Linked List
- Doubly Linked List

Covers operations like insertion, deletion, search, and reversal.

---

## Stacks & Queues

Stack and queue implementations using:

- Python lists
- Linked lists
- Queues with Stacks

---

## Trees

Includes:

- Binary Trees
- Binary Search Trees (BST)

### More about trees:

#### Types of trees:

- **Balanced Trees**  
  A balanced tree maintains a roughly equal height between the left and right subtrees for each node. This ensures
  efficient operations such as insertion, deletion, and search, typically in O(log n) time.  
  Examples: AVL Trees, Red-Black Trees

- **Unbalanced Trees**  
  An unbalanced tree can have one side significantly deeper than the other. This degrades performance, potentially
  making operations as slow as O(n), especially when the tree resembles a linked list.

#### Tree Traversals

- **In-order**  
  Visits nodes in the following order: Left → Root → Right  
  (Useful for retrieving values in sorted order from a BST)

- **Pre-order**  
  Visits nodes in the following order: Root → Left → Right  
  (Useful for copying the tree or generating prefix expressions)

- **Post-order**  
  Visits nodes in the following order: Left → Right → Root  
  (Useful for deleting the tree or evaluating postfix expressions)

### Self-Balancing Trees

Self-balancing trees maintain their structure automatically after insertions or deletions to preserve optimal
performance.

- **AVL Trees**  
  AVL trees maintain a balance factor (height difference) of -1, 0, or 1 for each node. If a node becomes unbalanced,
  rotations are used to restore balance.

- **Red-Black Trees**  
  Red-Black trees use color properties and a set of rules to maintain balance. While slightly less rigid than AVL trees,
  they provide good performance for insertions and deletions in practice.

### Binary heaps

Binary Heaps are complete binary trees that satisfy the **heap property**:

- **Max-Heap**: Every parent node has a value **greater than or equal to** its children.
- **Min-Heap**: Every parent node has a value **less than or equal to** its children.

They are commonly implemented using arrays, taking advantage of the index relationships:

- For a node at index `i`:
    - Left child: `2i + 1`
    - Right child: `2i + 2`
    - Parent: `(i - 1) // 2`

### Operations

- **Insert**  
  Adds a new element to the heap and restores the heap property by "bubbling up" the value.

- **Extract Max / Min**  
  Removes the root element and restores the heap property by "bubbling down" the last element.

- **Heapify**  
  Converts an unordered array into a valid heap in O(n) time.

### Use Cases

- Priority Queues
- Heap Sort (O(n log n))
- Efficient retrieval of min/max elements

### Priority Queues


A **Priority Queue** is an abstract data structure where each element has a "priority". Elements are served based on their priority rather than just their order in the queue.

#### Characteristics

- Elements with **higher priority** are dequeued before elements with lower priority.
- If two elements have the **same priority**, they are served in the order they were enqueued (FIFO).

#### Implementations

- **Binary Heaps** are the most efficient and commonly used way to implement priority queues.
  - Max-Heaps → for highest-priority first.
  - Min-Heaps → for lowest-priority first.

#### Operations

- **Insert / Enqueue**: Add an element with its priority.
- **Extract / Dequeue**: Remove the element with the highest (or lowest) priority.
- **Peek**: View the top-priority element without removing it.

#### Use Cases

- Task scheduling (e.g., CPU job queues)
- Dijkstra’s algorithm (for shortest paths)
- Event-driven simulations

### Trie

Trie (Prefix Tree)

A **Trie** is a tree-like data structure used to store a dynamic set of strings, where keys are usually strings. It is especially efficient for string-related operations like prefix matching or autocomplete.

### Characteristics

- Each node represents a single character of a string.
- The root node is empty and paths from root to leaf represent words.
- Nodes may store:
  - A character (implicitly via position)
  - A flag indicating the end of a word (`is_end_of_word`)
  - Optionally, a count or value (e.g., frequency)

### Operations

- **Insert(word)**: Adds a word to the trie, creating new nodes as needed.
- **Search(word)**: Checks if a full word exists in the trie.
- **StartsWith(prefix)**: Checks if any word in the trie starts with the given prefix.
- **Delete(word)**: Removes a word from the trie (optional and more complex).

### Advantages

- Fast lookup time: O(m), where *m* is the length of the word.
- Efficient for autocomplete systems.
- Stores common prefixes only once, reducing space in some cases.

### Use Cases

- Autocomplete and spell checking
- IP routing (longest prefix match)
- Dictionary word search
- Word games

---

## Graphs

Graph implementations using adjacency lists and matrices.

Algorithms:

- BFS and DFS
- Dijkstra’s Algorithm
- Kruskal and Prim (MST)

---

## Recursion

Examples:

- Tower of Hanoi
- Permutations and combinations
- N-Queens problem

---

## Sorting Algorithms

Includes:

- Bubble Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort

---

## Searching Algorithms

Includes:

- Linear Search
- Binary Search (iterative & recursive)
- Interpolation Search

---

## Dynamic Programming

Solved problems:

- Fibonacci (Memoization & Tabulation)
- 0/1 Knapsack
- Longest Common Subsequence (LCS)

---

## Complexity Analysis

Each function includes analysis of time and space complexity.

---

## How to Run

```bash
git clone https://github.com/yxngalx/dsa.git
cd dsa
python3 some_file.py
```
