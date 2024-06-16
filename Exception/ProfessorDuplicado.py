class ProfessorDuplicado(Exception):
    def __init__(self):
        super().__init__("Professor já cadastrado")