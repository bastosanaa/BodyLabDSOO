class NumeroInvalido(Exception):
    def __init__(self):
        super().__init__("Número de telefone inválido")