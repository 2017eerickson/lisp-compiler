def tokenize(source):
    tokens = []
    i = 0
    while i < len(source):
        char = source[i]
        parens = {"(", ")"}
        if char in parens:
            tokens.append(char)
            i += 1
        elif char.isspace():
            i += 1
        else:
            start = i
            while i < len(source) and ( not source[i].isspace() and source[i] not in parens) :
                i += 1
            tokens.append(source[start:i])
        
    return tokens
                 