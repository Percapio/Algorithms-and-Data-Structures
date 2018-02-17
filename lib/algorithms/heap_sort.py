# Heap Sort:
#   A sorting technique where we first find the maximum element and 
# place the maximum element at the end. We repeat the same process for 
# remaining element.  
#   A Binary Heap is a Complete Binary Tree where items are stored in a 
# special order such that value in a parent node is greater(or smaller) 
# than the values in its two children nodes. The former is called as max 
# heap and the latter is called min heap. The heap can be represented by 
# binary tree or array.

# Heap Sort Algorithm for sorting in increasing order:
# 1. Build a max heap from the input data.
# 2. At this point, the largest item is stored at the root of the heap. 
#   Replace it with the last item of the heap followed by reducing the 
#   size of heap by 1. Finally, heapify the root of tree.
# 3. Repeat above steps while size of heap is greater than 1.
