class TrieNode:
  def __init__(self):
    self.children = {}
    self.isWord = False
    
class Trie:
  def __init__(self):
    self.root = TrieNode()
    
  def insert(self, word):
    curr = self.root
    
    for letter in word:
      if letter not in curr.children:
        node = TrieNode()
        curr.children[letter] = node
      
      curr = curr.children[letter]
    
    curr.isWord = True
    
    
  def search(self, word):
    curr = self.root
    
    for letter in word:
      if letter in curr.children:
        curr = curr.children[letter]
      else:
        return False
        
    if curr.isWord == True:
      return True
    else:
      return False
    
  def startsWith(self, prefix):
    curr = self.root
    
    for letter in prefix:
      if letter in curr.children:
        curr = curr.children[letter]
      else:
        return False
        
    return True
  
obj = Trie()
obj.insert('car')
obj.insert('care')

print "obj.search('car')", obj.search('car')
print "obj.startsWith('ca')", obj.startsWith('ca')
