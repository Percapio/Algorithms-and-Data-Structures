# Algorithms and Data Structures

A single repository for Algorithms and Data Strutures written in Python.

*_this repo is an emulation [yangshun/lago](https://github.com/yangshun/lago)_

#### Algorithms
* Search Algorithms:
  + [Binary Search](/lib/algorithms/binary_search.py)
* Search N-th Term Algorithm:
  + [Quickselect](/lib/algorithms/quick_select.py) **<--need to redo**
* Sort Algorithms:
  + [Merge Sort](/lib/algorithms/merge_sort.py)
  + [Quicksort](/lib/algorithms/quick_sort.py)
  + Heap Sort
  + Timsort
  + Topological Sort
* Node Algorithms:
  + Breadth First Search
  + Depth First Search
  + Djikstra's Algorithm
* Extras:
  + Bellman-Ford Algorithm
  + Floyd Warshall Algorithm

#### Data Structures
* List
* Stack
* Queue
* Double-ended Queue
* Trie
* Binary Tree
* Binary Search Tree
* AVL Tree
* Suffix Tree
* Segment Tree
* Graphs
* N-D arrays
* Bloom Filter

#### Time Complexity
A helpful reminder on Time Complexity using a graph.

![alt text](/assets/time_complexity_mini.svg "pretty graph")

What this pretty graph is essentially saying, from best to worst:

|Run Time|Ranking|
|--|--|
|O( 1 )|TUBULAR!| 
|O( logn )|AWESOME!|
|O( n )|meh|
|O( nlogn )|Not good...|
|O( n^2 )|Terrible.|

#### Running
This repo requires Python 2.x installed.
Clone the repo, and run:
```
python lib/index.py
```

Test functions are under ```index/testers```.