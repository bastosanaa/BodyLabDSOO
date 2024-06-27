class CampoVazio(Exception):
    def __init__(self, campo):
        super().__init__(f"O campo {campo} está vazio. Por favor, preencha todos os campos.")
