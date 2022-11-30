from tkinter import *
from tkinter import Tk, StringVar, ttk

co0 = "#2e2d2b"  # preto
co1 = "#feffff"  # branco
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#e06636"  # profit
co6 = "#038cfc"  # azul
co7 = "#3fbfb9"  # azul
co8 = "#263238"  # verde
co9 = "#e9edf5"  # background


class app():
    def __init__(self):
        self.janela = Tk()
        self.janela.title('Trabalho Programação Orientada a Objetos')
        self.janela.geometry('200x200')
        self.janela.configure(background=co9)
        self.janela.resizable(width=FALSE, height=FALSE)

        style = ttk.Style(self.janela)
        style.theme_use("clam")

        self.bt = Button(
            self.janela, text="Cadastrar Usuario", command=teste)
        self.bt.pack()
        self.bt = Button(self.janela, text="Ver Usuarios", command="")
        self.bt.pack()
        self.bt = Button(self.janela, text="Cadastrar Produtos", command="")
        self.bt.pack()
        self.bt = Button(self.janela, text="Ver Produtos", command="")
        self.bt.pack()
        self.bt = Button(self.janela, text="Vender", command="")
        self.bt.pack()
        self.bt = Button(self.janela, text="Apagar Usuarios", command="")
        self.bt.pack()
        self.bt = Button(self.janela, text="Apagar Produtos", command="")
        self.bt.pack()

        self.janela.mainloop()


class teste():
    def __init__(self):
        self.teste = Tk()


app()
