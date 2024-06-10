import ply.yacc as yacc
from lexico import tokens

variables = {}



# Definir la precedencia de los operadores
precedence = (
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTIPLICACION', 'DIVISION'),
    ('left', 'MENOR_QUE', 'MAYOR_QUE', 'MENOR_O_IGUAL', 'MAYOR_O_IGUAL'),
    ('left', 'IGUALDAD', 'DIFERENTE'),
    ('left', 'AND', 'OR'),
    ('right', 'NOT'),
)

# Reglas de la gramática
def p_program(p):
    '''program : statement_list'''
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]


def p_statement(p):
    '''statement : declaration
                 | assignment
                 | conditional
                 | conditional_else
                 | loop_while
                 | loop_for
                 | imprimir
                 | expression FIN_SENTENCIA'''
    p[0] = p[1]



def p_imprimir(p):
    'imprimir : IMPRIMIR PAREN_IZQUIERDO expression PAREN_DERECHO FIN_SENTENCIA'
    print(p[3])



def p_declaration(p):
    '''declaration : DECLARACION_ENTERO IDENTIFICADOR IGUAL expression FIN_SENTENCIA
                   | DECLARACION_STRING IDENTIFICADOR IGUAL expression FIN_SENTENCIA
                   | DECLARACION_FLOAT IDENTIFICADOR IGUAL expression FIN_SENTENCIA
                   | DECLARACION_BOOLEAN IDENTIFICADOR IGUAL expression FIN_SENTENCIA'''
    variables[p[2]] = p[4]
    p[0] = None



def p_assignment(p):
    '''assignment : IDENTIFICADOR IGUAL expression FIN_SENTENCIA'''
    if p[1] in variables:
        variables[p[1]] = p[3]
    else:
        print(f"Error: Variable {p[1]} no declarada")
    p[0] = None



def p_conditional(p):
    '''conditional : CONDICIONAL_SI PAREN_IZQUIERDO expression PAREN_DERECHO DOS_PUNTOS statement_list conditional_else
                   | CONDICIONAL_SI PAREN_IZQUIERDO expression PAREN_DERECHO DOS_PUNTOS statement_list'''
    if p[3]:
        for stmt in p[6]:
            eval_statement(stmt)
    elif len(p) == 8 and p[7] is not None:
        for stmt in p[7]:
            eval_statement(stmt)

def p_conditional_else(p):
    '''conditional_else : CONDICIONAL_SINO PAREN_IZQUIERDO expression PAREN_DERECHO DOS_PUNTOS statement_list conditional_else
                        | CONDICIONAL_SINO PAREN_IZQUIERDO expression PAREN_DERECHO DOS_PUNTOS statement_list
                        | CONDICIONAL_CONTRARIO DOS_PUNTOS statement_list'''
    if len(p) == 8:
        if p[3]:
            p[0] = p[6]
        else:
            p[0] = p[7]
    elif len(p) == 6:
        if p[3]:
            p[0] = p[5]
        else:
            p[0] = None
    elif len(p) == 4:
        p[0] = p[3]

def p_loop_while(p):
    '''loop_while : CICLO_WHILE PAREN_IZQUIERDO expression PAREN_DERECHO DOS_PUNTOS statement_list'''
    while p[3]:
        for stmt in p[6]:
            eval_statement(stmt)
        p[3] = p[3]  # Re-evaluar la condición después de cada iteración
    p[0] = None

def p_loop_for(p):
    '''loop_for :  CICLO_FOR PAREN_IZQUIERDO for_init FIN_SENTENCIA expression FIN_SENTENCIA for_update PAREN_DERECHO DOS_PUNTOS statement_list'''
    for _ in range(variables[p[3]]):
        if p[5]:
            p[9]

def p_for_init(p):
    '''for_init : declaration
                | assignment'''
    p[0] = p[1]

def p_for_update(p):
    '''for_update : assignment'''
    p[0] = p[1]


def p_expression_binop(p):
    '''expression : expression SUMA expression
                  | expression RESTA expression
                  | expression MULTIPLICACION expression
                  | expression DIVISION expression
                  | expression MENOR_QUE expression
                  | expression MAYOR_QUE expression
                  | expression MENOR_O_IGUAL expression
                  | expression MAYOR_O_IGUAL expression
                  | expression IGUALDAD expression
                  | expression DIFERENTE expression
                  | expression AND expression
                  | expression OR expression'''
    if p[2] == '+':
        if isinstance(p[1], str) or isinstance(p[3], str):
            p[0] = str(p[1]) + str(p[3])
        else:
            p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]
    elif p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]
    elif p[2] == '&&':
        p[0] = p[1] and p[3]
    elif p[2] == '||':
        p[0] = p[1] or p[3]

def p_expression_not(p):
    'expression : NOT expression'
    p[0] = not p[2]

def p_expression_group(p):
    'expression : PAREN_IZQUIERDO expression PAREN_DERECHO'
    p[0] = p[2]

def p_expression_number(p):
    '''expression : ENTERO
                  | FLOTANTE'''
    p[0] = p[1]

def p_expression_string(p):
    'expression : CADENA'
    p[0] = p[1]

def p_expression_identifier(p):
    'expression : IDENTIFICADOR'
    p[0] = variables.get(p[1], 0)  # Obtener el valor de la variable o 0 si no está definida

def p_error(p):
    print("Error de sintaxis en la entrada:", p)

def eval_statement(stmt):
    if stmt is not None:
        if isinstance(stmt, list):
            for s in stmt:
                eval_statement(s)
        else:
            exec(stmt, globals(), variables)

# Construir el parser
parser = yacc.yacc()

# Analizar una cadena de entrada
data = '''
pasoHelado numero1 = 7;
pasoHelado numero2 = 5;
pasoHelado suma = numero1 + numero2;
hiloRedstone sumastring = "La suma de los numeros es: " + suma;

booleanman comprobacion = False;

si (suma > 10):
    comprobacion = True;

mientrasNoDiamante(comprobacion != True):
    suma = suma + 1;
    si (suma > 10):
        comprobacion = True;
'''

#result = parser.parse(data)
#print(result)
#print(variables)  # Imprimir el entorno de variables para verificar los resultados