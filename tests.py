import unittest
import task
import math


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test_circleArea(self):
        input1 = 1
        output1 = math.pi
        self.assertEqual(output1, task.circleArea(input1))
        input2 = 0
        output2 = 0
        self.assertEqual(output2, task.circleArea(input2))


if __name__ == '__main__':
    unittest.main()
