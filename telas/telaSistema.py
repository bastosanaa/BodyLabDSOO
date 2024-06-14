import PySimpleGUI as sg

class TelaSistema():
    
    def __init__(self):
        self.__window = None
        self.init_opcoes()
    
    def tela_opcoes(self):
        print("---- Sistema BodyLab 🎯💪 ----")
        print("Escolha sua opção:")
        print("1 - Professores")
        print("2 - Alunos")
        print("3 - Fichas")
        opcao = int(input("Escolha a opcao:"))
        print()
        return opcao
    
    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkPurple1')
        layout = [
            [sg.Text("Sistema BodyLab", font=('Fira Code', 25))],
            [sg.Radio('Professores', "RD1", key='1')],
            [sg.Radio('Alunos', "RD1", key='2')],
            [sg.Radio('Matriculas', "RD1", key='3')],
            [sg.Radio('Fichas', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistma BodyLab').Layout(layout)
    
    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()