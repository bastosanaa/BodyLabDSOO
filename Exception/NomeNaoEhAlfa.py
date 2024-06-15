class NomeNaoEhAlfa(Exception):
    def __init__(self):
        super().__init__("O nome deve conter apenas letras.")