# conversão de tipos, ou tambem chamado de coerção, ou type convertion, ou typecasting ou coercion 
# é o ato de converter um tipo em outro tipo
#  tipos imutáveis e primitivos: str, int, float, bool 
print("1")
print("1", type("1"))
print(int("1"), type(int("1")))  # ao usar a função int, a mesma altera a classe ou o tipo de string para integer
print(int("3") + 2)  # usada a função int (integer) para alterar do tipo string ("") para int (integer - numero inteiro)
print(float("3") + 2)  # Neste caso foi usada a função float, para alterar para o tipo float, dando um resultado com casa decimal
print(type(float("3") + 2))  # Neste caso foi usada a função/classe type antes da função float, para apenas mostrar a classe
# As funções são sempre usadas primeiro de dentro do parenteses para fora: (3º(2º(1º)))
print(bool("casa"), type(bool("qualquer"))) # String de Boleano prenchida, mesmo com um espaço, representa True (Verdadeiro)
print(str(11) + "b") # Conversão de numero em String, para poder "somar"/acrescentar à palavra na string seguinte

