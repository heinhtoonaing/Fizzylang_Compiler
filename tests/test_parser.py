import unittest
from lexer import lexer
from parser import Parser

class TestParser(unittest.TestCase):
    def test_basic(self):
        code = "PRINT 5 + 3"
        tokens = lexer(code)
        parser = Parser(tokens)
        expected = [('PRINT', ('+', 5, 3))]
        self.assertEqual(parser.parse(), expected)

    def test_assignment(self):
        code = "x = 10 * 2"
        tokens = lexer(code)
        parser = Parser(tokens)
        expected = [('ASSIGN', 'x', ('*', 10, 2))]
        self.assertEqual(parser.parse(), expected)

    def test_combined(self):
        code = """
        PRINT 5 + 3
        x = 10 * 2
        PRINT x - 4
        """
        tokens = lexer(code)
        parser = Parser(tokens)
        expected = [
            ('PRINT', ('+', 5, 3)),
            ('ASSIGN', 'x', ('*', 10, 2)),
            ('PRINT', ('-', 'x', 4))
        ]
        self.assertEqual(parser.parse(), expected)

if __name__ == '__main__':
    unittest.main()
