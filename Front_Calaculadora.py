
from tkinter import *
from tkinter import ttk

bg_primary = '#003566'
bg_secondary = '#ffc300'
bg_display = '#001d3d'
text_primary = '#fff'

janela = Tk()
janela.title('Calculadora')
janela.geometry('235x310')
janela.config(bg=bg_primary)

frame_tela = Frame(janela, width=235, height=50, bg=bg_display)
frame_tela.grid(row=1, column=0)

frame_body = Frame(janela, width=235, height=258)
frame_body.grid(row=1, column=0)

janela.mainloop()