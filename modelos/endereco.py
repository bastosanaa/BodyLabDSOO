class Endereco:

    def __init__(self, rua: str = "", complemento: str = "", bairro: str = "", cidade: str = "", cep: str = ""):
        self.rua = rua
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep

    def __str__(self):
        return 'Endereco: ' + self.rua + ', ' + self.complemento