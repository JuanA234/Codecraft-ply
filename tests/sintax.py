import ply.yacc as yacc
from tests.lexico import tokens

# Reglas gramaticales
def p_program(p):
    '''program : statement_list'''
    print("Program")

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    pass

def p_statement(p):
    '''statement : declaracion
                 | asignacion
                 | condicional
                 | ciclo_for
                 | ciclo_while'''
    pass

def p_declaracion(p):
    '''declaracion : DECLARACION_ENTERO IDENTIFICADOR FIN_SENTENCIA
                   | DECLARACION_STRING IDENTIFICADOR FIN_SENTENCIA
                   | DECLARACION_FLOAT IDENTIFICADOR FIN_SENTENCIA
                   | DECLARACION_BOOLEAN IDENTIFICADOR FIN_SENTENCIA'''
    print(f"Declaración: {p[1]} {p[2]}")

def p_asignacion(p):
    '''asignacion : IDENTIFICADOR OPERADOR expresion FIN_SENTENCIA'''
    print(f"Asignación: {p[1]} {p[2]} {p[3]}")

def p_condicional(p):
    '''condicional : CONDICIONAL_SI '(' expresion ')' bloque
                   | CONDICIONAL_SI '(' expresion ')' bloque CONDICIONAL_SINO bloque
                   | CONDICIONAL_SI '(' expresion ')' bloque CONDICIONAL_CONTRARIO bloque'''
    print("Condicional")

def p_ciclo_for(p):
    '''ciclo_for : CICLO_FOR '(' asignacion expresion FIN_SENTENCIA asignacion ')' bloque'''
    print("Ciclo for")

def p_ciclo_while(p):
    '''ciclo_while : CICLO_WHILE '(' expresion ')' bloque'''
    print("Ciclo while")

def p_expresion(p):
    '''expresion : ENTERO
                 | FLOTANTE
                 | CADENA
                 | IDENTIFICADOR'''
    p[0] = p[1]

def p_bloque(p):
    '''bloque : '{' statement_list '}' '''
    pass

def p_error(p):
    print(f"Error de sintaxis en '{p.value}'")

# Crear el parser
parser = yacc.yacc()

# Probar el parser (opcional)
if __name__ == "__main__":
    source_code = '''
    bloque variable1;
    hiloRedstone cadena = "Esto es una prueba";
    pasoHelado valor = 10.5;
    booleanman flag = verdadero;

    si (variable1 == 10) {
        variable1 = 20;
        minarPara (i = 0; i < 10; i++) {
            flag = falso;
        }
    } sino {
        variable1 = 30;
    }
    '''
    parser.parse(source_code)