class EmailInvalido(Exception):
    def __init__(self):
        super().__init__("Email inválido")