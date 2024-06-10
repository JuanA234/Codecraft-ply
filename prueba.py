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

sumaDecimal = 3;

imprimir(sumaDecimal);

si (sumaDecimal > 5):
    numerin = 1;
sino (sumaDecimal == 5):
    numerin = 2;

imprimir(numerin);

'''

source_code3 = '''
bloque nota1 = 85;
bloque nota2 = 90;
bloque nota3 = 78;
bloque sumaNotas = nota1 + nota2 + nota3;
pasoHelado promedio = sumaNotas / 3;
hiloRedstone mensaje = "El promedio del estudiante es: " + promedio;
imprimir(mensaje);
'''

# Ejecutar el lexer

'''lexer.input(source_code)
print("Tokens:")
for token in lexer:
    print(token)'''

data = "3 + 4 * (2 - 1)"

# Ejecutar el parser
parser.parse(source_code2)
print(variables)