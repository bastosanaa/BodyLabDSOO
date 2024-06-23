import PySimpleGUI as sg

class TelaSistema():
    
    def __init__(self):
        self.__window = None
        self.init_opcoes()
    
    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3   
        if values['4']:
            opcao = 4
        if values['0'] or button in(None, "Cancelar"):
            opcao = 0
        self.close()
        return opcao
    
    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkPurple1')
        layout = [
            [sg.Text("Sistema BodyLab", font=('Helvetica', 30, 'bold'))],
            [sg.Radio('Professores', "RD1", key='1')],
            [sg.Radio('Alunos', "RD1", key='2')],
            [sg.Radio('Matriculas', "RD1", key='3')],
            [sg.Radio('Fichas', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar', button_color=('white', 'green')), sg.Cancel('Cancelar', button_color=('white', 'red'))]
        ]
        self.__window = sg.Window('Sistma BodyLab').Layout(layout)
    
    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()
        