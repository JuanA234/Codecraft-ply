import ply.yacc as yacc
from calclex import tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)


def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_parentheses(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]


def p_error(p):
    print("Error de sintaxis en la entrada:", p)

yacc.yacc()

data = "3 + 4 * (2 - 1)"
result = yacc.parse(data)
print(result)