# semantic.py
class SemanticAnalyzer:
    def __init__(self, ast):
        self.ast = ast
        self.variables = {}

    def analyze(self):
        for statement in self.ast:
            if statement[0] == "PRINT":
                self.check_expression(statement[1])
            elif statement[0] == "ASSIGN":
                var = statement[1]
                expr = statement[2]
                self.variables[var] = self.check_expression(expr)
            elif statement[0] == "WHILE":
                condition = statement[1]
                self.check_expression(condition)
                for body_statement in statement[2]:
                    self.analyze(body_statement)

    def check_expression(self, expr):
        if isinstance(expr, int):
            return expr
        elif isinstance(expr, tuple):
            op, left, right = expr
            left_value = self.check_expression(left)
            right_value = self.check_expression(right)
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
        else:
            raise ValueError(f"Invalid expression: {expr}")

if __name__ == "__main__":
    from lexer import lexer
    from parser import Parser
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
    print(analyzer.variables)
