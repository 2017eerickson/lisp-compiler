from compiler.tokenizer import tokenize

def test_simple_expression():
    assert tokenize("(+ 1 2)") == ["(", "+", "1", "2", ")"]

def test_nested():
    assert tokenize("(+ 1 (* 2 3))") == ["(", "+", "1", "(", "*", "2", "3", ")", ")"]

def test_multi_character_symbols():
    assert tokenize("(define (square n) (* n n))") == [
        "(", "define", "(", "square", "n", ")", "(", "*", "n", "n", ")", ")"
    ]

def test_extra_whitespace_and_newlines():
    assert tokenize("  (+\n  1   2 )  ") == ["(", "+", "1", "2", ")"]

def test_no_spaces_around_parens():
    assert tokenize("(+ 1(* 2 3))") == ["(", "+", "1", "(", "*", "2", "3", ")", ")"]

def test_empty_input():
    assert tokenize("") == []
    
def test_comparison_operators():
    assert tokenize("(>= x 10)") == ["(", ">=", "x", "10", ")"]

def test_hyphenated_symbols():
    assert tokenize("(define my-var 5)") == ["(", "define", "my-var", "5", ")"]

def test_negative_numbers():
    assert tokenize("(+ -7 3)") == ["(", "+", "-7", "3", ")"]

def test_lone_minus_is_still_a_token():
    assert tokenize("(- 10 3)") == ["(", "-", "10", "3", ")"]