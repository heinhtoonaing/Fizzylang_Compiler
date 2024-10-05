import unittest
from lexer import lexer

class TestLexer(unittest.TestCase):
    def test_basic(self):
        code = "PRINT 5 + 3"
        expected = ['PRINT', '5', '+', '3']
        self.assertEqual(lexer(code), expected)

    def test_assignment(self):
        code = "x = 10 * 2"
        expected = ['x', '=', '10', '*', '2']
        self.assertEqual(lexer(code), expected)

    def test_combined(self):
        code = """
        PRINT 5 + 3
        x = 10 * 2
        PRINT x - 4
        """
        expected = ['PRINT', '5', '+', '3', 'x', '=', '10', '*', '2', 'PRINT', 'x', '-', '4']
        self.assertEqual(lexer(code), expected)

if __name__ == '__main__':
    unittest.main()
