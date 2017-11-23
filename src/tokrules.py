import ply.lex as lex


#    Robado de la documentacion. la idea es definir qué pinta tienen los
#    simbolos terminales de la gramática. se definen como t_TOKEN para cada TOKEN
#    (o definirlos como literales de un solo caracter)
#
#
#
#
#    When a function is used, the regular expression rule is specified in the function #   documentation string.
#    The function always takes a single argument which is an instance of LexToken. This #   object has attributes of t.type which is the token type (as a string), t.value which #   is the lexeme (the actual text matched), t.lineno which is the current line number, #   and t.lexpos which is the position of the token relative to the beginning of the
#   input text.
#
#    data = '''
#    3 + 4 * 10
#    + -20 *2
#    '''
#
#    $ python example.py
#    LexToken(NUMBER,3,2,1)
#    LexToken(PLUS,'+',2,3)
#    LexToken(NUMBER,4,2,5)
#    LexToken(TIMES,'*',2,7)
#    LexToken(NUMBER,10,2,10)
#    LexToken(PLUS,'+',3,14)
#    LexToken(MINUS,'-',3,16)
#    LexToken(NUMBER,20,3,18)
#    LexToken(TIMES,'*',3,20)
#    LexToken(NUMBER,2,3,21)
#
#    #
#    List of token names.   This is always required
#    tokens = (
#       'NUMBER',
#       'PLUS',
#       'MINUS',
#       'TIMES',
#       'DIVIDE',
#       'LPAREN',
#       'RPAREN',
#    )
#
#    # Regular expression rules for simple tokens
#    t_PLUS    = r'\+'
#    t_MINUS   = r'-'
#    t_TIMES   = r'\*'
#    t_DIVIDE  = r'/'
#    t_LPAREN  = r'\('
#    t_RPAREN  = r'\)'
#
#    # A regular expression rule with some action code
#    def t_NUMBER(t):
#        r'\d+'
#        t.value = int(t.value)
#        return t
#
#    # Define a rule so we can track line numbers
#    def t_newline(t):
#        r'\n+'
#        t.lexer.lineno += len(t.value)
#
#    # If no value is returned by the action function, the token is simply discarded and
#    the next token read.
#
#
#    # A string containing ignored characters (spaces and tabs)
#    t_ignore  = ' \t'
#
#    # Error handling rule
#    def t_error(t):
#        print("Illegal character '%s'" % t.value[0])
#        t.lexer.skip(1)


tokens = (
    'CHR',
)

# los literales son chars que matchean de una
literals = "_^/(){}"

def t_CHR(t):
    # el primer ^ toma complemento de los símbolos que siguen
    r'[^ _ \^ / \( \)\{\}]'
    return t

t_ignore  = '\t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
