import ply.lex as lex

tokens = (
    'CHR',
    'DIVIDE'
)

# los literales son chars que matchean de una
literals = "_^(){}"

def t_CHR(t):
    # el primer ^ toma complemento de los símbolos que siguen
    r'[^ _ \^ / \( \)\{\}]'
    return t

def t_DIVIDE(t):
    r'/'
    return t

t_ignore  = '\t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
