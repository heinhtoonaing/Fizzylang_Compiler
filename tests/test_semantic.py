import unittest
from lexer import lexer
from parser import Parser
from semantic import SemanticAnalyzer

class TestSemanticAnalyzer(unittest.TestCase):
    def test_basic(self):
        code = "PRINT 5 + 3"
        tokens = lexer(code)
        parser = Parser(tokens)
        ast = parser.parse()
        analyzer = SemanticAnalyzer(ast)
        analyzer.analyze()
        self.assertEqual(analyzer.variables, {})

    def test_assignment(self):
        code = "x = 10 * 2"
        tokens = lexer(code)
        parser = Parser(tokens)
        ast = parser.parse()
        analyzer = SemanticAnalyzer(ast)
        analyzer.analyze()
        self.assertEqual(analyzer.variables, {'x': 20})

    def test_combined(self):
        code = """
        PRINT 5 + 3
        x = 10 * 2
        PRINT x - 4
        """
        tokens = lexer(code)
        parser = Parser(tokens)
        ast = parser.parse()
        analyzer = SemanticAnalyzer(ast)
        analyzer.analyze()
        self.assertEqual(analyzer.variables, {'x': 20})

if __name__ == '__main__':
    unittest.main()
