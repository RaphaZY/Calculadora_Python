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
        if n2 == 0:
            return "Erro: divisão por zero."
        return n1 / n2
    
    def porcent(self, valor:int, percentual:int):
        return (valor * percentual) / 100
    
    def raiz_quadrada(self, n1:int):
        return math.sqrt(n1)
    
    def potenciacao(self, base:int, expoente:int):
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
