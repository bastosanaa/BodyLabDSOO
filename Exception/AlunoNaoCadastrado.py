class AlunoNaoCadastrado(Exception):
    def __init__(self):
        super().__init__("Aluno não cadastrado")
