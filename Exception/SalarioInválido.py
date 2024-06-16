class SalarioInvalido(Exception):
    def __init__(self):
        super().__init__("Salário inválido")