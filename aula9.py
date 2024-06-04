# Operadores aritméticos em Python
adicao = 20 + 5  # operador adição "+", que permite somar numeros inteiros e/ou float, ou entre 2 ou mais strings (não int e str)
print("Adição: ", adicao)

subtracao = 15 - 4.5  # operador subtracao "-", que permite subtrair numeros inteiros e/ou float
print("Subtração: ", subtracao)

multiplicacao = 9 * 2  # operador multiplicação "*", que permite multiplicar numeros inteiros e/ou float
print("Multiplicação: ", multiplicacao)

divisao = 30 / 2  # operador divisão "/", que permite dividir numeros inteiros e/ou float, mas mostra SEMPRE resultados float (com decimais)
print("Divisão: ", divisao)

divisao_inteira = 30 // 7  # operador divisão "//", que permite dividir numeros inteiros e/ou float, mas mostra SEMPRE resultados int (inteiros)
#  Não mostra os numeros decimais, mesmo que a divisão inclua um numero float
print("Divisão inteira: ", divisao_inteira)

exponenciacao = 2 ** 10  # Exponenciação ou potenciação "**", que é elevar um numero a outro
print("Exponenciação: ", exponenciacao)

modulo = 55 % 2  # modulo mostra o resto da divisão "%", ou seja, se o primeiro numero é divisivel pelo segundo numero (primeiro é multiplo do segundo)
print("Modulo: ", modulo)  #  Se retornar 0, é porque é. Se retornar um numero, é porque não é.
print("Modulo: ", modulo == 0)  # Também é possivel utilizar o boleano, para retornar se é verdadeiro ou falso
modulo = 16 % 8
print("Modulo: ", modulo, modulo == 0)  # Outro exemplo que é verdadeiro e foi colocado para mostrar também o valor
# Também pode ser utilizado para saber se um numero é par ou ímpar
print(16 % 2 == 0)  
print(17 % 2 == 0)  