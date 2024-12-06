import ply.lex as lex

tokens = (
    # Keywords
    'FN', 'AS', 'RETURN', 'IF', 'ELSE', 'WHILE', 'DO',
    'FOR', 'TO', 'BEGIN', 'END', 'INT', 'VECTOR', 'STR',
    'BOOL', 'NULL','SCAN','PRINT','LIST','LENGTH','EXIT',

    # Operators
    'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE',
    'GREATER_THAN', 'LESS_THAN', 'EQUALS',
    'GREATER_EQUAL', 'LESS_EQUAL', 'NOT_EQUALS',
    'OR', 'AND', 'NOT',
    'QUESTION', 'COLON', 'DBL_COLON',
    'ARROW',
    'EQ',  # single equals for assignment

    # Brackets and delimiters
    'LPAREN', 'RPAREN',          # ( )
    'LCURLYEBR', 'RCURLYEBR',    # { }
    'LSQUAREBR', 'RSQUAREBR',    # [ ]
    'DBL_LSQUAREBR', 'DBL_RSQUAREBR',  # [[ ]]
    'COMMA',
    'SEMI_COLON',

    # Others
    'ID',        # identifiers
    'NUMBER',    # numeric literals
    'STRING',    # string literals
    'BOOLEAN',   # true/false literals
)

# Simple single-character operators and delimiters
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURLYEBR = r'{'
t_RCURLYEBR = r'}'
t_LSQUAREBR = r'\['
t_RSQUAREBR = r'\]'
t_COMMA = r','
t_SEMI_COLON = r';'
t_COLON = r':'
t_EQ = r'='
t_NOT = r'!'
t_QUESTION = r'\?'

# Multi-character operators (longer ones first!)
t_GREATER_EQUAL = r'>='
t_LESS_EQUAL = r'<='
t_NOT_EQUALS = r'!='
t_EQUALS = r'=='
t_GREATER_THAN = r'>'
t_LESS_THAN = r'<'
t_DBL_COLON = r'::'
t_ARROW = r'=>'
t_OR = r'\|\|'
t_AND = r'&&'
t_DBL_LSQUAREBR = r'\[\['
t_DBL_RSQUAREBR = r'\]\]'

# Keywords - using functions to ensure they're not part of identifiers
def t_FN(t): r'fn'; return t
def t_AS(t): r'as'; return t
def t_RETURN(t): r'return'; return t
def t_IF(t): r'if'; return t
def t_ELSE(t): r'else'; return t
def t_WHILE(t): r'while'; return t
def t_DO(t): r'do'; return t
def t_FOR(t): r'for'; return t
def t_TO(t): r'to'; return t
def t_BEGIN(t): r'begin'; return t
def t_END(t): r'end'; return t
def t_INT(t): r'int'; return t
def t_VECTOR(t): r'vector'; return t
def t_STR(t): r'str'; return t
def t_BOOL(t): r'bool'; return t
def t_NULL(t): r'null'; return t
def t_BOOLEAN(t):
    r'true|false'
    t.value = (t.value == 'true')
    return t
def t_SCAN(t): r'scan'; return t
def t_PRINT(t): r'print'; return t
def t_LIST(t): r'list'; return t
def t_LENGTH(t): r'length'; return t
def t_EXIT(t): r'exit'; return t

# Complex tokens
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"|\'([^\\\n]|(\\.))*?\''
    t.value = t.value[1:-1]  # Remove quotes
    return t

# Track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignore whitespace and tabs
t_ignore = ' \t'

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

# Handle comments
def t_COMMENT(t):
    r'<%.*?%>'
    pass  # No return value. Token is discarded

# Build the lexer
lexer = lex.lex()