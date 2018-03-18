class MinHeap:
  def __init__(self):
    self.heap = []
  
  def swap(self, parentIdx, idx):
    temp = self.heap[parentIdx]
    self.heap[parentIdx] = self.heap[idx]
    self.heap[idx] = temp
    
  def getParent(self, idx):
    return self.heap[self.getParentIdx(idx)]
        
  def getParentIdx(self, idx):
    return abs(idx - 1) / 2
    
  def insert(self,val):
    self.heap.append(val)
    idx = len(self.heap) - 1
    parent = self.getParent(idx)
    
    while parent > val:
      parentIdx = self.getParentIdx(idx)
      self.swap(parentIdx, idx)
      idx = parentIdx
      parent = self.getParent(idx)
  
  #def delete(self, val):
  
  #def extractMin(self):
  

heap = MinHeap()

heap.insert(3)
heap.insert(4)
heap.insert(1)
heap.insert(7)
heap.insert(8)
heap.insert(2)

print heap.heap