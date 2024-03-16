import math

class Calculadora:
    def __init__(self):
        pass
    
    def soma(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def mult(self, a, b):
        return a * b
    
    def divi(self, a, b):
        if b == 0:
            return "Erro: divisão por zero."
        return a / b
    
    def porcent(self, valor, percentual):
        return (valor * percentual) / 100
    
    def raiz_quadrada(self, a):
        return math.sqrt(a)
    
    def potenciacao(self, base, expoente):
        return base ** expoente


calc = Calculadora()

print("Soma:", calc.soma(500, 478))              
print("Subtração:", calc.sub(1, -100))     
print("Multiplicação:", calc.mult(75, 4))  
print("Divisão:", calc.divi(5, 3))        
print("Divisão por zero:", calc.divi(1, 0)) 
print("Porcentagem:", calc.porcent(1000, 70))  
print("Raiz Quadrada:", calc.raiz_quadrada(121))   
print("Potenciação:", calc.potenciacao(8, 3))     
