import math

class Calculadora:
    def __init__(self):
        pass

    def verificar(self, numero1, numero2):
        if (numero1 or numero2) == str:
            print("Falha na Matrix")
            

    def somar(self, numero1:int, numero2:int)->int:
        return numero1 + numero2
    
    def subitrair(self, numero1:int, numero2:int)->int:
        return numero1 - numero2
    
    def multiplicar(self, numero1:int, numero2:int)->int:
        return numero1 * numero2
    
    def dividir(self, numero1:int, numero2:int)->float:
        if numero2 == 0 or numero1 == 0:
            return "Erro: divisão por zero."
        return numero1 / numero2
    
    def porcentagem(self, valor:int, percentual:float)->float:
        return (valor * percentual) / 100
    
    def raiz_quadrada(self, n1:int)->float:
        return math.sqrt(n1)
    
    def potenciacao(self, base:int, expoente:int)->int:
        return base ** expoente

operacao = 1
calc = Calculadora()

while operacao != 0: 
    operacao = input("Digite a operação desejada (+, -, *, /, %, v, ^) ou digite 0 para terminar: ")

    if operacao == "0":
        print("Fim do programa")
        break
    elif operacao == '+':
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        print(calc.somar(numero1, numero2))
        
    elif operacao == '-':
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        print(calc.subitrair(numero1, numero2))
    elif operacao == '*':
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        print(calc.multiplicar(numero1, numero2))
    elif operacao == '/':
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        print(calc.dividir(numero1, numero2))
    elif operacao == '%':
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        print(calc.porcentagem(numero1, numero2))
    elif operacao == 'v':
        numero1 = float(input("Digite o primeiro número: "))
        print(calc.raiz_quadrada(numero1))
    elif operacao == '^':
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        print(calc.potenciacao(numero1, numero2))
    else:
        print("Operação inválida!")
