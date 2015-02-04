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
