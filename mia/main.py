#Autor: Alan Jahir Martinez Sepulveda
#Codigo: 216569127

import ply.lex as lex
 
#Lista de los tokens requerida
tokens = (
        'NUMBER',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'LPAREN',
        'RPAREN',
)
 
#Expresiones regulares
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
 
reservadas = ['BEGIN','END','IF','THEN','WHILE','DO','CALL','CONST',
		'VAR','PROCEDURE','OUT','IN','ELSE'
		]

tokens = reservadas+['ID','NUMBER','PLUS','MINUS','TIMES','DIVIDE',
		'ODD','ASSIGN','NE','LT','LTE','GT','GTE',
		'LPARENT', 'RPARENT','COMMA','SEMMICOLOM',
		'DOT','UPDATE'
		]

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t
 
#Regla si hay una nueva linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
 
#String si tiene cadena vacia
t_ignore  = ' \t'
 
def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)
 
lexer = lex.lex()

data = '''3 + 4 * 10+ -20 *1'''
 
# Give the lexer some input
lexer.input(data)
 
# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break 
    print(tok)