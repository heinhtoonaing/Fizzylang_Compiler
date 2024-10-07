# lexer.py
# lexer.py
import re

def lexer(code):
    tokens = re.findall(r'\bPRINT\b|\bWHILE\b|\b\d+\b|[-+*/=()<>]|[a-zA-Z_]\w*', code)
    return tokens


if __name__ == "__main__":
    code = """
    PRINT 5 + 3
    x = 10 * 2
    PRINT x - 4
    """
    print(lexer(code))
