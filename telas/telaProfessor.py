from telas.telaAbstrata import TelaAbstrata

class TelaProfessor(TelaAbstrata):
    def tela_opcoes(self):
        print("----------- Professores ------------")
        print("1 - Mostrar professores cadastrados")
        print("2 - Cadastrar novo professor")
        print("3 - Alterar professor já cadastrado")
        print("4 - Vizualizar professor já cadastrado")
        print("5 - Relatório de professores por turno")
        print("0 - Voltar ao menu inicial")
        opcao = int(input("Insira a opção escolhida: "))
        return opcao