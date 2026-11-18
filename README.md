# Lisp Compiler

A compiler for a small Lisp dialect, written from scratch in Python. It compiles Lisp source code to bytecode for a custom stack-based virtual machine. No parsing libraries are used.

```
source code → tokenizer → parser → code generator → bytecode → VM
```

## Goal

Compile and run programs like this:

```lisp
(define (factorial n)
  (if (< n 2)
      1
      (* n (factorial (- n 1)))))

(print (factorial 5))   ; → 120
```

## Status

🚧 In progress

- [x] Tokenizer
- [ ] Parser
- [ ] Stack-based VM
- [ ] Code generation (arithmetic)
- [ ] Variables, comparisons, and `if`
- [ ] Functions and recursion
- [ ] Command-line interface

## Language features (v1)

| Feature | Examples |
|---|---|
| Integers | `42`, `-7` |
| Arithmetic | `+ - * /` |
| Comparisons | `< > = <= >=` |
| Special forms | `define`, `if` |
| Output | `print` |

## Getting started

```bash
git clone https://github.com/YOUR-USERNAME/lisp-compiler.git
cd lisp-compiler
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m pytest
```

## Project structure

```
lisp-compiler/
├── compiler/
│   └── tokenizer.py
└── tests/
    └── test_tokenizer.py
```

## Author

Ericka C. Erickson
