from collections import deque

def parse(tokens):
    """Parse a list of tokens into a list of top-level expressions."""
    print(tokens)
    tokens = deque(tokens)
    program = []
    while tokens:
        program.append(parse_expr(tokens))
    return program

expressions = []
def parse_expr(tokens):
    """Parse ONE expression from the front of tokens and return it. 
    ""(+ 1(* 2 3))") == ["(", "+", "1", "(", "*", "2", "3", ")", ")"] -> [ [+, 1, [*,2,3] ] ] [[]]  """
    token = tokens.popleft()
    if token == "(":
        current_expr = []
        while token != ")":
            current_expr.append(parse_expr(tokens))  
        return current_expr  
    else:
        return atom(token)
    

def atom(token):
    """Convert a token to an int if it's a number, otherwise return it as a symbol (str)."""
    if isinstance(int(token),int):
        return int(token)
    else:
        return token
        


