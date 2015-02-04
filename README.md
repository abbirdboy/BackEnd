#Backend 


##Shifted List Search 


###Initial Code Implementation 
```python
def shiftlistmax(list):
    return max(list)
```
###Preliminary Test Code (Passing Test)

*initialtestcode.py*
```python
import unittest

#Sample 1
initial_list1 = [1, 3, 7, 8, 9, 10, 11]  # Here is our initial ordered list
shifted_list1 = [8, 9, 10, 11, 1, 3, 7]  # Here is the list after it has been sliced (at index 3) and shifted
# Your function should return `11`

# Sample 2
initial_list2 = [2, 4, 6, 8, 10]  # Here is our initial ordered list
shifted_list2 = [6, 8, 10, 2, 4]  # Here is the list after it has been sliced (at index 2) and shifted
# Your function should return `10`
# Sample 3
initial_list3 = [2, 4, 6, 8, 10]  # Here is our initial ordered list
shifted_list3 = [2, 4, 6, 8, 10]  # Here is the list after it has been sliced (at index 0) and shifted
# Your function should return `10`

def shiftlistmax(list):
    return max(list)

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(shiftlistmax(shifted_list1), 11, 'Sample 1') 
        self.assertEqual(shiftlistmax(shifted_list2), 10, 'Sample 2')
        self.assertEqual(shiftlistmax(shifted_list3), 10, 'Sample 3')
        
if __name__ == '__main__':
    unittest.main()

#Console Print Out:
#169-231-85-179:Desktop abhishekbhattacharya$  python3 initialtestcode.py
#.
#----------------------------------------------------------------------
#Ran 1 test in 0.000s

#OK
```

The preliminary test code ran without errors and performed the action desired.

###Considering Edge Cases

List can not be empty 

List can not contain non-integers

List must be iterable

###Test Code (Revised) for Edge Cases (Failing Test)

*revised_initialtestcode.py*
```python
import unittest

def shiftlistmax(list):
    return max(list)
        
        
# Sample 1
initial_list1 = [1, 3, 7, 8, 9, 10, 11]  # Here is our initial ordered list
shifted_list1 = [8, 9, 10, 11, 1, 3, 7]  # Here is the list after it has been sliced (at index 3) and shifted
# Your function should return `11`
#shiftedlist_max(shifted_list1) #=> '11'

# Sample 2
initial_list2 = [2, 4, 6, 8, 10]  # Here is our initial ordered list
shifted_list2 = [6, 8, 10, 2, 4]  # Here is the list after it has been sliced (at index 2) and shifted
# Your function should return `10`
#shiftedlist_max(shifted_list2) #=> '10'
# Sample 3
initial_list3 = [2, 4, 6, 8, 10]  # Here is our initial ordered list
shifted_list3 = [2, 4, 6, 8, 10]  # Here is the list after it has been sliced (at index 0) and shifted
# Your function should return `10`
#shiftedlist_max(shifted_list3) #=> '10'

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(shiftlistmax(shifted_list1), 11, 'Sample 1')
        self.assertEqual(shiftlistmax(shifted_list2), 10, 'Sample 2')
        self.assertEqual(shiftlistmax(shifted_list3), 10, 'Sample 3')
        self.assertEqual(shiftlistmax([ ]), False, 'Empty List')
        self.assertEqual(shiftlistmax(["1",bool,1]), False, 'Non-Integer Element in List')

        
if __name__ == '__main__':
    unittest.main()

#Console Print Out: 
#169-231-85-179:Desktop abhishekbhattacharya$ python3 revised_initialtestcode.py
#E
#======================================================================
#ERROR: test (__main__.MyTest)
#----------------------------------------------------------------------
#Traceback (most recent call last):
#  File "revised_initialtestcode.py", line 48, in test
#    self.assertEqual(shiftlistmax([ ]), False, 'Empty List')
#  File "revised_initialtestcode.py", line 3, in shiftlistmax
#    return max(list)
#ValueError: max() arg is an empty sequence
#
#----------------------------------------------------------------------
#Ran 1 test in 0.000s

#FAILED (errors=1)    

```

###Revised Code Implementation (Passing Test)

*revised_testcode.py*
```python
import collections 
import unittest

#*** Sample Shifted Lists Here ***#

def shiftlistmax(list):
    
    if (list and isinstance(list, collections.Iterable)):  
        if all(isinstance(n, int) for n in list):
           return max(list)  #max method only accepts iterable lists
        else:
           return False 
    else: 
        return False
        

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(shiftlistmax(shifted_list1), 11, 'Sample 1')
        self.assertEqual(shiftlistmax(shifted_list2), 10, 'Sample 2')
        self.assertEqual(shiftlistmax(shifted_list3), 10, 'Sample 3')
        self.assertEqual(shiftlistmax([ ]), False, 'Empty List')
        self.assertEqual(shiftlistmax(["1",bool,1]), False, 'Non-Integer Element in List')

        
if __name__ == '__main__':
    unittest.main()
    
# Console Print Out:     
#169-231-85-179:Desktop abhishekbhattacharya$ python3 revised_testcode.py
#.
#----------------------------------------------------------------------
#Ran 1 test in 0.000s

```

###Algorithm Growth Implications 

Since the max() method in Python iterates through the entire list, in a case where there are a large number of list elements, the time to process the max value would not only take a considerable amount of time but also be taxing on the system. 

Python (2.5) source code: (http://en.wikibooks.org/wiki/Algorithms/Find_maximum/Python_method_1)
```python
def findmax(a):
 
    if len(a) == 0:
        return 0
 
    curr_max = a[0]
 
    for i in a:
        if i > curr_max:
            curr_max = i
 
    return curr_max

```

Since we know that the initial lists are ordered and how the shifted lists were indexed, we can use that information to our advantage.

###A Better Solution?

In the case of a list with 1 million elements, we could use the index value and iterate that amount backwards through the list to the point where the max value was shifted. 

####Secondary Code Implementation 

```python
def shiftlistmax(list, index):
    return list[-(index + 1)]
```

####Secondary Test Code (Passing Test)

*secondarytestcode.py*
```python
import unittest

#*** Sample Shifted Lists Here ***#


def shiftlistmax(list, index):
    return list[-(index + 1)]
    
class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(shiftlistmax(shifted_list1, 3), 11, 'Sample 1')
        self.assertEqual(shiftlistmax(shifted_list2, 2), 10, 'Sample 2')
        self.assertEqual(shiftlistmax(shifted_list3, 0), 10, 'Sample 3')
        
if __name__ == '__main__':
    unittest.main()
    
# Console Print Out:     
#169-231-85-179:Desktop abhishekbhattacharya$ python3 secondarytestcode.py
#.
#----------------------------------------------------------------------
#Ran 1 test in 0.000s

```

####Secondary Test Code and Implementation (Revised) (Passing Test)
Rewritten secondary code and test code to comply with aforementioned edge cases. Also changed the return of `False` to `TypeError` for future specificity and debugging purposes. 

*finaltestcode.py*
```python
import collections
import unittest

# Sample 1
initial_list1 = [1, 3, 7, 8, 9, 10, 11]  # Here is our initial ordered list
shifted_list1 = [8, 9, 10, 11, 1, 3, 7]  # Here is the list after it has been sliced (at index 3) and shifted
# Your function should return `11`
#shiftedlist_max(shifted_list1) #=> '11'

# Sample 2
initial_list2 = [2, 4, 6, 8, 10]  # Here is our initial ordered list
shifted_list2 = [6, 8, 10, 2, 4]  # Here is the list after it has been sliced (at index 2) and shifted
# Your function should return `10`
#shiftedlist_max(shifted_list2) #=> '10'
# Sample 3
initial_list3 = [2, 4, 6, 8, 10]  # Here is our initial ordered list
shifted_list3 = [2, 4, 6, 8, 10]  # Here is the list after it has been sliced (at index 0) and shifted
# Your function should return `10`
#shiftedlist_max(shifted_list3) #=> '10'

def shiftlistmax(list, index):

    if (list and isinstance(list, collections.Iterable)):  

        if (all(isinstance(n, int) for n in list)) and index >= 0:
           return list[-(index + 1)]  
        else:
           raise TypeError("List elements must be integers and index value must be a positive integer") 
    else: 
        raise TypeError("List must be non-empty and iterable")
        

class MyTest(unittest.TestCase):
    def test(self):
       self.assertEqual(shiftlistmax(shifted_list1, 3), 11, 'Sample 1')
       self.assertEqual(shiftlistmax(shifted_list2, 2), 10, 'Sample 2')
       self.assertEqual(shiftlistmax(shifted_list3, 0), 10, 'Sample 3')
       self.assertRaises(TypeError, shiftlistmax)
       
if __name__ == '__main__':
    unittest.main()

#shiftlistmax(shifted_list1, 3) => 11
#shiftlistmax(shifted_list2, 2) => 10 
#shiftlistmax(shifted_list3, 0) => 10 
#shiftlistmax([ ], 0) => TypeError("List must be non-empty and iterable")
#shiftlistmax(["1"], 0) => TypeError("List elements must be integers and index value must be a positive integer") 
#shiftlistmax(shifted_list3, -1) => TypeError("List elements must be integers and index value must be a positive integer")

#169-231-85-179:Backend abhishekbhattacharya$ python3 finaltestcode.py
#.
#----------------------------------------------------------------------
#Ran 1 test in 0.000s
#
#OK

        
```


