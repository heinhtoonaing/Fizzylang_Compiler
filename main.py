# main.py
if __name__ == "__main__":
    from lexer import lexer
    from parser import Parser
    from semantic import SemanticAnalyzer
    from codegen import CodeGenerator

    code = """
    PRINT 5 + 3
    x = 10 * 2
    PRINT x - 4
    """
    
    # Step 1: Tokenize the input code
    tokens = lexer(code)
    print("Tokens:", tokens)
    
    # Step 2: Parse the tokens into an AST
    parser = Parser(tokens)
    ast = parser.parse()
    print("AST:", ast)
    
    # Step 3: Semantic analysis (checking for undefined variables, etc.)
    analyzer = SemanticAnalyzer(ast)
    analyzer.analyze()
    print("Symbol Table (after semantic analysis):", analyzer.variables)
    
    # Step 4: Code generation
    codegen = CodeGenerator(ast)
    codegen.generate()
