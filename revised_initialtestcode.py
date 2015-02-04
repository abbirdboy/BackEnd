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