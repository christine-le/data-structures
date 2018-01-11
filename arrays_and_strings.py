# Arrays and Strings (from Cracking The Coding Interview)
# TODO: Complete exercises 1.6, 1.7, 1.8, 1.9 and Additional Questions

### 1.1  Is unique:  Implement an algorithm to determine if a string has all unique characters.  What if you cannot use additional data structures.
# TODO:  Implement using a bit map

# With simple data structure:
# Time Complexity: O(n)
# Space Complexity: O(1)
def is_unique(my_string):
  my_array = []

  for l in my_string:
    if l not in my_array:
      my_array.append(l)
    else:
      return False

  return True

# print "is_unique:", is_unique("hello")

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

# print "check_permutation:", check_permutation("abba", "bbaa")
# print "check_permutation:", check_permutation("abbda", "bbaas")

# Time Complexity: O(n log n) due to sorting
def check_permutation2(string1, string2):
	# Return immediately if different lengths
  if len(string1) != len(string2): return False

  string1 = ''.join(sorted(string1))
  string2 = ''.join(sorted(string2))

  if string1 == string2:
    return True
  else:
    return False

# print "check_permutation2:", check_permutation2("abba", "bbaa")
# print "check_permutation2:", check_permutation2("abbda", "bbaas")

### 1.3 URLify:  Write a method to replace all spaces in a string with '%20'.
import re

def URLify(my_string, len):
  return re.sub("\s+", "%20", my_string.strip())

# print URLify("Hello world ", 11)
# print URLify(" Hello world ", 11)
# print URLify("  Hello world ", 11)

### 1.4 Palindrome Permutation
# TODO:  Implement using a bit map

# Time Complexity: O(n)
def palindrome_permutation(my_string):
  my_string = my_string.lower()
  my_array = []

  for i in my_string:
    if i == " ": continue

    if i not in my_array:
      my_array.append(i)
    else:
      my_array.remove(i)

  if len(my_array) == 0 or len(my_array) == 1:
    return True
  else:
    return False

# print palindrome_permutation("Tact Coa")

### 1.5 One Away
# assumptions: case sensitive
def one_away(string1, string2):
  len1 = len(string1)
  len2 = len(string2)
  
  if abs(len1 - len2) > 1: return False
  if string1 == string2: return True
  
  string1 = string1.lower()
  string2 = string2.lower()
  
  if len1 == len2:
    is_one_away = replace(string1, string2)
  elif len1 > len2:
    is_one_away = remove(string1, string2)
  else:
    is_one_away = remove(string2, string1)
    
  return is_one_away
  
def replace(string1, string2):
  cnt = 0
  for i in range(0, len(string1)):
    if string1[i] != string2[i]:
      cnt += 1
    if cnt > 1:
      return False
  
  return True
  
def remove(string1, string2):
  cnt = 0
  for i in range(0, len(string1)):
    if i >= len(string2) or string1[i] != string2[i]:
      string1 = string1[0:i] + string1[i+1:]
      
      if string1 == string2:
        return True
      else:
        return False
    

print one_away("pale", "ple")
print one_away("pales", "pale")
print one_away("pale", "bale")
print one_away("pale", "bake")