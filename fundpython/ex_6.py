class Calculadora:
    def __init__(self, valor):
        self.valor = valor
    
    def quadrado(self):
        return self.valor ** 2

if __name__ == "__main__":
    # Testando a classe
    numero = 5
    calc = Calculadora(numero)
    resultado = calc.quadrado()
    print(f"O quadrado de {numero} é {resultado}.")
