import unittest
from operator import itemgetter

from rk1 import Computer, Microprocessor, MicroprocessorComputer


class TestMicroprocessorComputerSystem(unittest.TestCase):

    def setUp(self):
        # Create sample data
        self.computers = [
            Computer(1, 'Desktop PC'),
            Computer(2, 'Laptop'),
            Computer(3, 'Server'),
        ]

        self.microprocessors = [
            Microprocessor(1, 'Intel', 25000, 1),
            Microprocessor(2, 'AMD', 35000, 1),
            Microprocessor(3, 'ARM', 25000, 2),
            Microprocessor(4, 'Apple', 45000, 3),
        ]

        self.microprocessors_computers = [
            MicroprocessorComputer(1, 1),
            MicroprocessorComputer(1, 2),
            MicroprocessorComputer(2, 3),
            MicroprocessorComputer(3, 4),
            MicroprocessorComputer(3, 5),
            MicroprocessorComputer(3, 6),
        ]

    def test_task_e1(self):
        # Test Task E1
        result = [(m.brand, m.price, c.name)
                  for c in self.computers
                  for m in self.microprocessors
                  if m.computer_id == c.computer_id]

        self.assertIn(('Server', 45000, 'Server'), result)
        self.assertNotIn(('ARM', 25000, 'Desktop PC'), result)

    def test_task_e2(self):
        # Test Task E2
        res_12_unsorted = []
        for c in self.computers:
            computer_microprocessors = list(filter(lambda i: i[2] == c.name, self.task_e1_result))
            if len(computer_microprocessors) > 0:
                c_prices = [price for _, price, _ in computer_microprocessors]
                c_prices_sum = round(sum(c_prices) / len(computer_microprocessors), 2)
                res_12_unsorted.append((c.name, c_prices_sum))

        res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
        expected_result = [('Server', 45000.0), ('Desktop PC', 30000.0), ('Laptop', 0.0)]

        self.assertEqual(res_12, expected_result)

    def test_task_e3(self):
        # Test Task E3
        result = list(filter(lambda i: i[0].find('A') != -1, self.task_e3_result))
        expected_result = [('ARM', 25000, 'Server'), ('Apple', 45000, 'Server')]

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()