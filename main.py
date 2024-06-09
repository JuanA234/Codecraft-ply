from tests.lexico import lexer
from tests.sintax import parser

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

# Ejecutar el lexer
lexer.input(source_code)
print("Tokens:")
for token in lexer:
    print(token)

# Ejecutar el parser
print("\nParsing:")
parser.parse(source_code)
