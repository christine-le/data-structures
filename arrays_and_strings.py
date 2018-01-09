# Arrays and Strings (from Cracking The Coding Interview)

### 1.1  Is unique:  Implement an algorithm to determine if a string has all unique characters.  What if you cannot use additional data structures.
# TODO:
# Implement w/o a data structure
# Implement using a bit map

# With simple data structure:
# Time Complexity = O(n)
# Space Complexity = O(1)
def is_unique(my_string):
    my_array = []

    for l in my_string:
        if l not in my_array:
        	my_array.append(l)
        else:
			return False
    return True

print "is_unique(hello):", is_unique("hello")

### 1.2 Check Permutation:  Given two strings, write a method to decide if one is a permutation of the other.

# Time Complexity: O(n)
def check_permutation(string1, string2):
	# Return immediately if different lengths
    if len(string1) != len(string2): return False
    
    for i in string1:
      pos = string2.find(i)
      if pos > -1:
        string2 = string2[:pos] + string2[pos+1:]
      else:
        return False
  
    if len(string2) > 0:
      return False
      
    return True

print "check_permutation:", check_permutation("abba", "bbaa")
print "check_permutation:", check_permutation("abbda", "bbaas")

# Time Complexity: O(n log n)
def check_permutation2(string1, string2):
	# Return immediately if different lengths
    if len(string1) != len(string2): return False

	string1 = ''.join(sorted(string1))
	string2 = ''.join(sorted(string2))
	
	if string1 == string2:
	  return True
	else:
	  return False
print "check_permutation2:", check_permutation2("abba", "bbaa")
print "check_permutation2:", check_permutation2("abbda", "bbaas")