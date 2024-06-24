class CPFinvalido(Exception):
    def __init__(self):
        super().__init__("CPF inválido")