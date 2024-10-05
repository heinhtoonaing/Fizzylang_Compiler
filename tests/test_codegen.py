import unittest
from lexer import lexer
from parser import Parser
from semantic import SemanticAnalyzer
from codegen import CodeGenerator
from io import StringIO
import sys

class TestCodeGenerator(unittest.TestCase):
    def test_basic(self):
        code = "PRINT 5 + 3"
        tokens = lexer(code)
        parser = Parser(tokens)
        ast = parser.parse()
        analyzer = SemanticAnalyzer(ast)
        analyzer.analyze()

        # Capture print output
        captured_output = StringIO()
        sys.stdout = captured_output

        codegen = CodeGenerator(ast)
        codegen.generate()

        # Reset redirect.
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue().strip(), "8")

    def test_assignment(self):
        code = """
        x = 10 * 2
        PRINT x
        """
        tokens = lexer(code)
        parser = Parser(tokens)
        ast = parser.parse()
        analyzer = SemanticAnalyzer(ast)
        analyzer.analyze()

        # Capture print output
        captured_output = StringIO()
        sys.stdout = captured_output

        codegen = CodeGenerator(ast)
        codegen.generate()

        # Reset redirect.
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue().strip(), "20")

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

        # Capture print output
        captured_output = StringIO()
        sys.stdout = captured_output

        codegen = CodeGenerator(ast)
        codegen.generate()

        # Reset redirect.
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue().strip(), "8\n16")

if __name__ == '__main__':
    unittest.main()
