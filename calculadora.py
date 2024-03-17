import math

class Calculadora:
    def __init__(self):
        pass
    
    def soma(self, n1:int, n2:int):
        return n1 + n2
    
    def sub(self, n1:int, n2:int):
        return n1 - n2
    
    def mult(self, n1:int, n2:int):
        return n1 * n2
    
    def divi(self, n1:int, n2:int):
        if n2 == 0 or n1 == 0:
            return "Erro: divisão por zero."
        return n1 / n2
    
    def porcent(self, valor:int, percentual:int):
        return (valor * percentual) / 100
    
    def raiz_quadrada(self, n1:int):
        return math.sqrt(n1)
    
    def potenciacao(self, base:int, expoente:int):
        return base ** expoente

operacao = 1
calc = Calculadora()

while operacao != 0: 
    operacao = input("Digite a operação desejada (+, -, *, /, %, v, ^) ou digite 0 para terminar: ")

    if operacao == "0":
        print("Fim do programa")
        break
    elif operacao == '+':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = calc.soma(num1, num2)
        print(resultado)
    elif operacao == '-':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = calc.sub(num1, num2)
        print(resultado)
    elif operacao == '*':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = calc.mult(num1, num2)
        print(resultado)
    elif operacao == '/':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = calc.divi(num1, num2)
        print(resultado)
    elif operacao == '%':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = calc.porcent(num1, num2)
        print(resultado)
    elif operacao == 'v':
        num1 = float(input("Digite o primeiro número: "))
        resultado = calc.raiz_quadrada(num1)
        print(resultado)
    elif operacao == '^':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = calc.potenciacao(num1, num2)
        print(resultado)
    else:
        print("Operação inválida!")
