import re

conditionals = ["si", "sino", "contrario"]
logicOperators = ["interruptor", "puerta", "cierre"]
reservedWords = ["bloque", "hiloRedstone", "pasoHelado", "booleanman", "minarPara", "mientrasNoDiamante", "picoRoto", "seguirPicando"]
token_specification = [
    ('Cadena', r'\'[^\']*\'|\"[^\"]*\"'),  # Cadenas de texto
    ('Identificador', r'[A-Za-z_]\w*'),    # Identificadores
    ('Entero', r'\d+'),                    # Números enteros
    ('Flotante', r'\d*\.\d+'),             # Números flotantes
    ('Operador', r'[+\-*/=]'),             # Operadores
    ('FinSentencia', r';'),                # Fin de sentencia
    ('Espacio', r'[ \t]+'),                # Espacios
    ('NuevaLinea', r'\n'),                 # Nueva línea
]

token_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

class Lexer(object):
    def __init__(self, source_code):
        self.source_code = source_code

    def tokenize(self):
        tokens = []
        for mo in re.finditer(token_regex, self.source_code):
            kind = mo.lastgroup
            value = mo.group(kind)

            if kind == 'Cadena':
                tokens.append(['Cadena', value])
            elif kind == 'Identificador':
                if value in conditionals:
                    tokens.append(['Condicional', value])
                elif value in logicOperators:
                    tokens.append(['OperadorLogico', value])
                elif value in reservedWords:
                    if value == "bloque":
                        tokens.append(["DeclaracionEntero", value])
                    elif value == "hiloRedstone":
                        tokens.append(["DeclaracionString", value])
                    elif value == "pasoHelado":
                        tokens.append(["DeclaracionFloat", value])
                    elif value == "booleanman":
                        tokens.append(["DeclaracionBoolean", value])
                    elif value == "minarPara":
                        tokens.append(["CicloFor", value])
                    elif value == "mientrasNoDiamante":
                        tokens.append(["CicloWhile", value])
                    elif value == "picoRoto":
                        tokens.append(["palabraReservadaPicoRoto", value])
                    elif value == "seguirPicando":
                        tokens.append(["palabraReservadaPicoRotoSeguitPicando", value])
                else:
                    tokens.append(['Identificador', value])
            elif kind == 'Entero':
                tokens.append(['Entero', value])
            elif kind == 'Flotante':
                tokens.append(['Flotante', value])
            elif kind == 'Operador':
                tokens.append(['Operador', value])
            elif kind == 'FinSentencia':
                tokens.append(['FinSentencia', value])
            elif kind == 'Espacio':
                continue
            elif kind == 'NuevaLinea':
                continue

        return tokens

# Ejemplo de uso
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
