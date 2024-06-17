class CepNaoEhNumero(Exception):
    def __init__(self):
        super().__init__("CEP não é um número")