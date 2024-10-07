# parser.py
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def parse(self):
        statements = []
        while self.position < len(self.tokens):
            if self.tokens[self.position] == "PRINT":
                self.position += 1
                statements.append(("PRINT", self.expression()))
            elif self.tokens[self.position] == "WHILE":
                self.position += 1
                condition = self.expression()
                self.position += 1
                body = []
                while self.tokens[self.position] != "ENDWHILE":
                    body.append(self.statement())
                statements.append(("WHILE", condition, body))
            else:
                var = self.tokens[self.position]
                self.position += 1
                self.position += 1
                expr = self.expression()
                statements.append(("ASSIGN", var, expr))
        return statements
    def statement(self):
        if self.tokens[self.position] == "PRINT":
            return self.parse()
      
            
    

    def expression(self):
        left = self.term()
        while self.position < len(self.tokens) and self.tokens[self.position] in '+-':
            op = self.tokens[self.position]
            self.position += 1
            right = self.term()
            left = (op, left, right)
        return left

    def term(self):
        left = self.factor()
        while self.position < len(self.tokens) and self.tokens[self.position] in '*/':
            op = self.tokens[self.position]
            self.position += 1
            right = self.factor()
            left = (op, left, right)
        return left

    def factor(self):
        if self.position < len(self.tokens) and self.tokens[self.position].isdigit():
            value = int(self.tokens[self.position])
            self.position += 1
            return value
        elif self.position < len(self.tokens) and self.tokens[self.position].isidentifier():
            var = self.tokens[self.position]
            self.position += 1
            return var
        else:
            raise SyntaxError("Unexpected token: " + self.tokens[self.position])

if __name__ == "__main__":
    from lexer import lexer
    code = """
    PRINT 5 + 3
    x = 10 * 2
    PRINT x - 4
    """
    tokens = lexer(code)
    parser = Parser(tokens)
    print(parser.parse())
