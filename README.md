# TesLang Compiler

A compiler implementation for TesLang programming language, developed as part of a compiler construction course.

## Project Status

🚧 **Work in Progress** 🚧

Currently implementing:
- [x] Phase 1: Lexical Analysis (Tokenizer)
- [ ] Phase 2: Syntax Analysis (Parser)
- [ ] Phase 3: Semantic Analysis
- [ ] Phase 4: Code Generation

## Current Features (Lexical Analyzer)

- Token recognition for TesLang language
- Support for:
  - Keywords (fn, if, else, while, etc.)
  - Operators (+, -, *, /, etc.)
  - Delimiters ({}, [], (), etc.)
  - Comments (<% %>)
  - Built-in functions (scan, print, list, length, exit)
- Line and column number tracking
- Error reporting

## Prerequisites

- Python 3.x
- PLY (Python Lex-Yacc)

## Installation

```bash
pip install ply
```
## Usage

Currently supports lexical analysis:
```bash
python main.py
```
## License
This project is licensed under the MIT License - see the LICENSE.txt file for details

## Acknowledgments
Developed as part of the Compiler Design course