
from collections import deque


def parse(tokens):
    """Parse a list of tokens into a list of top-level expressions."""
    tokens = deque(tokens)
    program = []
    while tokens:
        program.append(parse_expr(tokens))
    return program


def parse_expr(tokens):
    """Parse ONE expression from the front of tokens and return it."""
    token = tokens.popleft()

    if token == "(":
        current_expr = []                                  # make the box only when we see "("
        while tokens and tokens[0] != ")":                 # PEEK, don't pop
            current_expr.append(parse_expr(tokens))        # helper hands back ONE finished thing
        if not tokens:
            raise SyntaxError("Unexpected end of input: missing ')'")
        tokens.popleft()                                   # throw away the matching ")"
        return current_expr                                # hand the box back

    elif token == ")":
        raise SyntaxError("Unexpected ')'")

    else:
        return atom(token)                                 # base case: no box


def atom(token):
    """Convert a token to an int if it's a number, otherwise return it as a symbol (str)."""
    try:
        return int(token)
    except ValueError:
        return token


if __name__ == "__main__":
    from compiler.tokenizer import tokenize
    print(parse(tokenize("(+ 1 (* 2 3))")))# from collections import deque
# from tokenizer import tokenize

# def parse(tokens):
#     """Parse a list of tokens into a list of top-level expressions."""
#     tokens = deque(tokens) # [ "(" , "(", "+", "1", "2" ")", ")"]
#     program = []
#     while tokens:
#         program.append(parse_expr(tokens))
#     return program

# expressions = []
# def parse_expr(tokens):
#     """Parse ONE expression from the front of tokens and return it. 
#     ""(+ 1(* 2 3))") == ["(", "+", "1", "(", "*", "2", "3", ")", ")"] -> [ [+, 1, [*,2,3] ] ] [[]]  
#      [ "(" , "(", "+", "1", "2" ")", ")"] -> [["+", 1 , 2]] 
#     """
#     if tokens and tokens[0] == "(" : 
#         # token = tokens.popleft() 
#         current_expr = [] 
#         token = tokens.popleft()
#         while tokens or token != ")" :
#             if token == "(":  
#                 current_expr.append(parse_expr(tokens))
#             current_expr.append(atom(token))
#             token = tokens.popleft() 
#         return current_expr 
#     else:
#         return atom(tokens.popleft())  
        
# def atom(token):
#     """Convert a token to an int if it's a number, otherwise return it as a symbol (str)."""
#     if token.lstrip("-").isdigit():
#         return int(token)
#     else:
#         return str(token)

# print(tokenize("(+ 1 (* 2 3))"))
# print(parse(tokenize("(+ 1 (* 2 3))"))) # -> ["+", 1, ["*", 2, 3]]
