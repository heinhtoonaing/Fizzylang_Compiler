# codegen.py
class CodeGenerator:
    def __init__(self, ast):
        self.ast = ast
        self.variables = {}

    def generate(self):
        for statement in self.ast:
            if statement[0] == "PRINT":
                value = self.evaluate_expression(statement[1])
                print(value)
            elif statement[0] == "ASSIGN":
                var = statement[1]
                value = self.evaluate_expression(statement[2])
                self.variables[var] = value
            elif statement[0] == "WHILE":
                condition = statement[1]
                body = statement[2]
                while self.evaluate_expression(condition):
                    for body_statement in body:
                        self.generate(body_statement)

    def evaluate_expression(self, expr):
        if isinstance(expr, int):
            return expr
        elif isinstance(expr, tuple):
            op, left, right = expr
            left_value = self.evaluate_expression(left)
            right_value = self.evaluate_expression(right)
            if left_value is None or right_value is None:
                raise ValueError("Undefined variable used in expression")
            if op == '+':
                return left_value + right_value
            elif op == '-':
                return left_value - right_value
            elif op == '*':
                return left_value * right_value
            elif op == '/':
                if right_value == 0:
                    raise ValueError("Division by zero error")
                return left_value / right_value
        elif isinstance(expr, str):
            if expr in self.variables:
                return self.variables[expr]
            else:
                raise ValueError(f"Undefined variable: {expr}")

if __name__ == "__main__":
    from lexer import lexer
    from parser import Parser
    from semantic import SemanticAnalyzer
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
    codegen = CodeGenerator(ast)
    codegen.generate()
