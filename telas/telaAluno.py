from telas.telaAbstrata import TelaAbstrata

class TelaAluno(TelaAbstrata):

    def tela_opcoes(self):
        print("----------- Alunos ------------")
        print("1 - Cadastrar Aluno")
        print("2 - Remover Aluno")
        print("3 - Listar Alunos")
        opcao = int(input("Insira a opção escolhida: "))
        return opcao
    
    def pega_dados_aluno(self):
        print("----------- Cadastrar Aluno ------------")
        nome = input("Insira o nome do aluno: ")
        numero_telefone = input("Insira o número de telefone do aluno: ")
        email = input("Insira o email do aluno: ")
        return {"nome": nome, "numero_telefone": numero_telefone, "email": email}

    def seleciona_aluno(self):
        nome = input("Insira o nome do aluno: ")
        return nome
    
    def mostra_aluno(self, aluno):
        print("-------- Dados do Aluno ----------")
        print(f"Nome: {aluno.nome}")
        print(f"Telefone: {aluno.numero_telefone}")
        print(f"Email: {aluno.email}")
    
    def mostra_mensagem(self, msg):
        print(msg)