#!/usr/bin/env python
# coding: utf-8

# In[27]:


from tkinter import *
from tkinter import ttk

#cores

cor1 = '#F8F8FF' # azul
cor2 = '#90EE90' # verde
cor3 = '#D3D3D3' # cinza

janela = Tk()
janela.title("Calculadora Média Combustível")
janela.geometry("500x300")
janela.configure(bg=cor1)

#Dividindo a janela em duas partes

frame_cima = Frame(janela, width=500, height=50, bg=cor1, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=500, height=180, bg=cor1, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)


#Configurando frame_cima

app_nome = Label(frame_cima, text='Média Combustível', width=23, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 16 bold'), bg=cor1, fg=cor2)
app_nome.place(x=0, y=0)

app_linha = Label(frame_cima, text='', width=400, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 1 '), bg=cor3, fg=cor2)
app_linha.place(x=0, y=35)

# Função Calcular

def calcular():
    km = float(e_km.get())
    litros = float(e_litros.get())
    resultado = km/litros
    
    resultado_final = l_resultado_texto['text'] = "Sua média é " + resultado
    


#Configurando frame_baixo

l_km = Label(frame_baixo, text='Insira o KM', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold '), justify='center', bg=cor1, fg=cor2)
l_km.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)
e_km = Entry(frame_baixo, width=5, relief='solid', font=('Ivy 10 bold '), justify='center')
e_km.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)

l_litros = Label(frame_baixo, text='Abastecimento', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold '), justify='center', bg=cor1, fg=cor2)
l_litros.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)
e_litros = Entry(frame_baixo, width=5, relief='solid', font=('Ivy 10 bold '), justify='center')
e_litros.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)

l_resultado = Label(frame_baixo, text='---', width=10, height=1, padx=6, pady=12, relief='flat', anchor='center', font=('Ivy 24 bold '), justify='center', bg=cor3, fg=cor1)
l_resultado.place(x=175, y=10)

l_resultado_texto = Label(frame_baixo, text='', width=74, height=1, padx=0, pady=12, relief='flat', anchor='center', font=('Ivy 10 bold '), justify='center', bg=cor1, fg=cor2)
l_resultado_texto.place(x=0, y=90)

b_calcular = Button(frame_baixo,command=calcular, text="Calcular",width=50, height=1, overrelief=SOLID,  bg=cor2, fg="white", font=('Ivy 10 bold'), anchor="center", relief=RAISED )
b_calcular.grid(row=4, column=0,  sticky=NSEW, pady=60, padx=5, columnspan=30)


janela.mainloop()

