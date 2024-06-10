import ply.lex as lex

# Lista de tokens
tokens = [
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
    'IGUAL',
    'MENOR_QUE',
    'MAYOR_QUE',
    'MENOR_O_IGUAL',
    'MAYOR_O_IGUAL',
    'IGUALDAD',
    'DIFERENTE',
    'AND',
    'OR',
    'NOT',
    'PAREN_IZQUIERDO',
    'PAREN_DERECHO',
    'LLAVE_IZQUIERDA',
    'LLAVE_DERECHA',
    'DOS_PUNTOS',
    'IDENTIFICADOR',
    'ENTERO',
    'FLOTANTE',
    'CADENA',
    'FIN_SENTENCIA'
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
    'picoRoto': 'ESTRUCTURA_BREAK',
    'seguirPicando': 'ESTRUCTURA_CONTINUE',
    'imprimir' : 'IMPRIMIR',
    'in': 'IN',
    'range': 'RANGE'
}

tokens += list(reserved.values())

# Expresiones regulares para tokens simples
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_IGUAL = r'='
t_MENOR_QUE = r'<'
t_MAYOR_QUE = r'>'
t_MENOR_O_IGUAL = r'<='
t_MAYOR_O_IGUAL = r'>='
t_IGUALDAD = r'=='
t_DIFERENTE = r'!='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_PAREN_IZQUIERDO = r'\('
t_PAREN_DERECHO = r'\)'
t_LLAVE_IZQUIERDA = r'\{'
t_LLAVE_DERECHA = r'\}'
t_DOS_PUNTOS = r':'
t_FIN_SENTENCIA = r';'

# Ignorar espacios y tabs
t_ignore = ' \t'

def t_CADENA(t):
    r'\"([^\\\n]|(\\.))*?\"|\'([^\\\n]|(\\.))*?\''
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
