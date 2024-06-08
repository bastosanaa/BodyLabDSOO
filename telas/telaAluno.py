from telas.telaAbstrata import TelaAbstrata

class TelaAluno(TelaAbstrata):

    def tela_opcoes(self):
        print("----------- Alunos ------------")
        print("1 - Mostrar alunos cadastrados")
        print("2 - Cadastrar novo aluno")
        print("3 - Alterar aluno já cadastrado")
        print("4 - Realizar matrícula")
        print("5 - Cancelar matrícula")
        print("6 - Mostrar dados da matrícula")
        print("7 - Alterar algum dado da matrícula")
