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