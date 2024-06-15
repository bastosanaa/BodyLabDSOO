class AlunoDuplicado(Exception):
    def __init__(self):
        super().__init__("Aluno já cadastrado")