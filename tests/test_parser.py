import pytest
from compiler.tokenizer import tokenize
from compiler.parser import parse


def p(source):
    return parse(tokenize(source))


def test_number():
    assert p("42") == [42]

def test_negative_number():
    assert p("-7") == [-7]

def test_symbol():
    assert p("x") == ["x"]

def test_lone_minus_is_a_symbol():
    assert p("-") == ["-"]

def test_simple_list():
    assert p("(+ 1 2)") == [["+", 1, 2]]

def test_nested():
    assert p("(+ 1 (* 2 3))") == [["+", 1, ["*", 2, 3]]]

def test_define_function():
    assert p("(define (square n) (* n n))") == [
        ["define", ["square", "n"], ["*", "n", "n"]]
    ]

def test_multiple_top_level_expressions():
    assert p("(define x 5) (print x)") == [["define", "x", 5], ["print", "x"]]

def test_empty_list():
    assert p("()") == [[]]

def test_empty_program():
    assert p("") == []

def test_missing_close_paren():
    with pytest.raises(SyntaxError):
        p("(+ 1 2")

def test_extra_close_paren():
    with pytest.raises(SyntaxError):
        p("(+ 1 2))") 
