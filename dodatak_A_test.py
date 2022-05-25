import math
import unittest

import dodatak_A

class DodatakATest(unittest.TestCase):

    def test_divide_with_zero(self):
        operations_manager = dodatak_A.OperationsManager(1, 0)
        self.assertTrue(math.isnan(operations_manager.perform_division()))

    def test_divide_with_not_a_float(self):
        operations_manager = dodatak_A.OperationsManager(1, "")
        self.assertTrue(math.isnan(operations_manager.perform_division()))

    def test_divide_with_not_a_number(self):
        operations_manager = dodatak_A.OperationsManager(1, None)
        self.assertTrue(math.isnan(operations_manager.perform_division()))


if __name__ == '__main__':
    unittest.main()

