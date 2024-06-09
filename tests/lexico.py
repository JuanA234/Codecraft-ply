import ply.lex as lex

# Lista de tokens
tokens = [
    'IDENTIFICADOR', 'ENTERO', 'FLOTANTE', 'CADENA',
    'OPERADOR', 'FIN_SENTENCIA'
]

# Palabras reservadas
reserved = {
    'bloque': 'DECLARACION_ENTERO',
    'hiloRedstone': 'DECLARACION_STRING',
    'pasoHelado': 'DECLARACION_FLOAT',
    'booleanman': 'DECLARACION_BOOLEAN',
    'si': 'CONDICIONAL_SI',
    'sino': 'CONDICIONAL_SINO',
    'contrario': 'CONDICIONAL_CONTRARIO',
    'minarPara': 'CICLO_FOR',
    'mientrasNoDiamante': 'CICLO_WHILE',
    'picoRoto': 'RESERVADA_PICOROTO',
    'seguirPicando': 'RESERVADA_SEGIRPICANDO',
    'interruptor': 'OPERADOR_LOGICO_INT',
    'puerta': 'OPERADOR_LOGICO_PUERTA',
    'cierre': 'OPERADOR_LOGICO_CIERRE'
}

tokens += list(reserved.values())

# Expresiones regulares para tokens simples
t_OPERADOR = r'[+\-*/=]'
t_FIN_SENTENCIA = r';'

# Ignorar espacios y tabs
t_ignore = ' \t'

def t_CADENA(t):
    r'\"([^\\\n]|(\\.))*?\" | \'([^\\\n]|(\\.))*?\''
    return t

def t_FLOTANTE(t):
    r'\d*\.\d+'
    t.value = float(t.value)
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFICADOR(t):
    r'[A-Za-z_][\w_]*'
    t.type = reserved.get(t.value, 'IDENTIFICADOR')  # Verificar palabras reservadas
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Crear el lexer
lexer = lex.lex()

''''''
# Probar el lexer (opcional)
if __name__ == "__main__":
    source_code = '''
    bloque variable1;
    hiloRedstone cadena = "Esto es una prueba";
    si (variable1 == 10) {
        pasoHelado valor = 10.5;
        minarPara (i = 0; i < 10; i++) {
            booleanman flag = verdadero;
        }
    }
    '''
    '''
    lexer.input(source_code)
    for token in lexer:
        print(token)
        '''