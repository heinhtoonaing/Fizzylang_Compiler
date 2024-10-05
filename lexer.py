# lexer.py
import re

def lexer(code):
    tokens = re.findall(r'\bPRINT\b|\b[A-Za-z_][A-Za-z0-9_]*\b|\b\d+\b|[-+*/=]', code)
    return tokens

if __name__ == "__main__":
    code = """
    PRINT 5 + 3
    x = 10 * 2
    PRINT x - 4
    """
    print(lexer(code))
