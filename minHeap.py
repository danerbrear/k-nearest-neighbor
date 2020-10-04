# Code copied from https://www.geeksforgeeks.org/min-heap-in-python/
# Modified to integrate with this codebase

import sys 
  
class MinHeap: 
  
    def __init__(self, maxsize): 
        self.maxsize = maxsize 
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1) 
        self.Heap[0] = -1 * sys.maxsize 
        self.FRONT = 1
  
    # Function to return the position of 
    # parent for the node currently 
    # at pos 
    def parent(self, pos): 
        return pos//2
  
    # Function to return the position of 
    # the left child for the node currently 
    # at pos 
    def leftChild(self, pos): 
        return 2 * pos 
  
    # Function to return the position of 
    # the right child for the node currently 
    # at pos 
    def rightChild(self, pos): 
        return (2 * pos) + 1
  
    # Function that returns true if the passed 
    # node is a leaf node 
    def isLeaf(self, pos): 
        if pos >= (self.size//2) and pos <= self.size: 
            return True
        return False
  
    # Function to swap two nodes of the heap 
    def swap(self, fpos, spos): 
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos] 
  
    # Function to heapify the node at pos 
    def minHeapify(self, pos): 
  
        # If the node is a non-leaf node and greater 
        # than any of its child 
        if not self.isLeaf(pos): 
            if (self.Heap[pos][1] > self.Heap[self.leftChild(pos)][1] or 
               self.Heap[pos][1] > self.Heap[self.rightChild(pos)][1]): 
  
                # Swap with the left child and heapify 
                # the left child 
                if self.Heap[self.leftChild(pos)][1] < self.Heap[self.rightChild(pos)][1]: 
                    self.swap(pos, self.leftChild(pos)) 
                    self.minHeapify(self.leftChild(pos)) 
  
                # Swap with the right child and heapify 
                # the right child 
                else: 
                    self.swap(pos, self.rightChild(pos)) 
                    self.minHeapify(self.rightChild(pos)) 
  
    # Function to insert a node into the heap 
    def insert(self, element): 
        if self.size >= self.maxsize : 
            return
        self.size += 1
        self.Heap[self.size] = element 
  
        current = self.size 
  
        if (self.parent(current) == 0):
            return
        while self.Heap[current][1] < self.Heap[self.parent(current)][1]: 
            self.swap(current, self.parent(current))
            current = self.parent(current) 
            if self.parent(current) == 0:
                break
  
    # Function to print the contents of the heap 
    def Print(self): 
        for i in range(1, (self.size//2)+1): 
            parent = "NULL"
            try:
                parent = str(round(self.Heap[i][1], 3))
            except:
                pass
            leftChild = "NULL"
            try:
                leftChild = str(round(self.Heap[2 * i][1], 3))
            except:
                pass
            rChild = "NULL"
            try:
                rChild = str(round(self.Heap[2 * i + 1][1], 3))
            except:
                pass
            print(" PARENT : " + parent + " LEFT CHILD : " + leftChild +" RIGHT CHILD : " + rChild) 
  
    # Function to build the min heap using 
    # the minHeapify function 
    def minHeap(self): 
  
        for pos in range(self.size//2, 0, -1): 
            self.minHeapify(pos) 
  
    # Function to remove and return the minimum 
    # element from the heap 
    def remove(self): 
  
        popped = self.Heap[self.FRONT] 
        self.Heap[self.FRONT] = self.Heap[self.size] 
        self.size-= 1
        self.minHeapify(self.FRONT) 
        return popped 