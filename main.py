from lexico import lexer
from sintax import parser, variables

source_code = '''
bloque numero1 = 7;
bloque numero2 = 5;
bloque suma = numero1 + numero2;
hiloRedstone sumastring = "La suma de los numeros es: " + suma;

booleanman comprobacion = False; 

si (suma > 10): 
    comprobacion = True;

mientrasNoDiamante(comprobacion != True):  
    suma = suma + 1;
    si (suma > 10):
        comprobacion = True;
'''

source_code2 = '''
pasoHelado decimal1 = 1.13; 
pasoHelado decimal2 = 7.14;
pasoHelado sumaDecimal = decimal1 + decimal2;
bloque numerin = 0;

decimal1 = 2.3;

si (sumaDecimal > 5):
    numerin = 1;
sino (sumaDecimal == 5):
    numerin = 2;
contrario:
    numerin = 3;

bloque sumaFor = 0;
minarPara i in range(5):
    sumaFor = sumaFor + i;
'''

# Ejecutar el lexer

'''lexer.input(source_code)
print("Tokens:")
for token in lexer:
    print(token)'''




data = "3 + 4 * (2 - 1)"

# Ejecutar el parser
print(parser.parse(source_code2))
print(variables)
