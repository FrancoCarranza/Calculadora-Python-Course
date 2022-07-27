import os
import tkinter as tk
from math import sqrt as raiz
os.system('cls')
class Calculdora:
    def __init__(self):
        #Creo la ventana
        self.ventana=tk.Tk()
        self.ventana.title('Calculadora')
        self.ventana.configure(background='steelblue')
        #Textos donde van aparecer las respuestas
        self.text=''
        self.text2=''
        self.operacion=''
        self.operacion2=''
        self.operacion3=''
        self.text3=self.text,self.operacion, self.text2 #, self.operacion2, self.text3, self.operacion3, self.text4
        
        self.label_1=tk.Label(self.ventana, text='')
        self.label_1.grid(column=0, row=0)
        self.label_1.configure(background='steelblue')
        self.label_2=tk.Label(self.ventana, text='')
        self.label_2.grid(column=1, row=1)
        self.label_2.configure(background='steelblue')
        self.label_3=tk.Label(self.ventana, text='')
        self.label_3.grid(column=2, row=2)
        self.label_3.configure(background='steelblue')
        self.label_4=tk.Label(self.ventana, text=self.text)
        self.label_4.grid(column=3, row=2)
        self.label_4.configure(background='steelblue')
        #Todos los 24 botones de la calculadora
        self.boton_1=tk.Button(self.ventana, text=' \n %\n', width=6, command=self.porcentaje)
        self.boton_1.grid(column=0, row=3)
        self.boton_1.configure(background='dodgerblue')
        self.boton_2=tk.Button(self.ventana, text='\nCE\n',  width=6, command=self.CE)
        self.boton_2.grid(column=1, row=3)
        self.boton_2.configure(background='dodgerblue')
        self.boton_3=tk.Button(self.ventana, text='\n C \n',  width=6, command=self.C)
        self.boton_3.grid(column=2, row=3)
        self.boton_3.configure(background='dodgerblue')
        self.boton_4=tk.Button(self.ventana, text='\n<<\n',  width=6, command=self.borrar)
        self.boton_4.grid(column=3, row=3)
        self.boton_4.configure(background='dodgerblue')
        self.boton_5=tk.Button(self.ventana, text='\n1/x\n',  width=6, command=self.fraccion)
        self.boton_5.grid(column=0, row=4)
        self.boton_5.configure(background='dodgerblue')
        self.boton_6=tk.Button(self.ventana, text='\n X²\n',  width=6, command=self.cuadrado)
        self.boton_6.grid(column=1, row=4)
        self.boton_6.configure(background='dodgerblue')
        self.boton_7=tk.Button(self.ventana, text='\n√x\n',  width=6, command=self.raiz)
        self.boton_7.grid(column=2, row=4)
        self.boton_7.configure(background='dodgerblue')
        self.boton_8=tk.Button(self.ventana, text='\n  ÷ \n',  width=6, command=self.dividir)
        self.boton_8.grid(column=3, row=4)
        self.boton_8.configure(background='dodgerblue')
        self.boton_9=tk.Button(self.ventana, text='\n  7 \n',  width=6, command=self.siete)
        self.boton_9.grid(column=0, row=5)
        self.boton_9.configure(background='gray')
        self.boton_10=tk.Button(self.ventana, text='\n  8 \n',  width=6, command=self.ocho)
        self.boton_10.grid(column=1, row=5)
        self.boton_10.configure(background='gray')
        self.boton_11=tk.Button(self.ventana, text='\n  9 \n',  width=6, command=self.nueve)
        self.boton_11.grid(column=2, row=5)
        self.boton_11.configure(background='gray')
        self.boton_12=tk.Button(self.ventana, text='\n  X \n',  width=6, command=self.multiplicar)
        self.boton_12.grid(column=3, row=5)
        self.boton_12.configure(background='dodgerblue')
        self.boton_13=tk.Button(self.ventana, text='\n  4 \n',  width=6, command=self.cuatro)
        self.boton_13.grid(column=0, row=6)
        self.boton_13.configure(background='gray')
        self.boton_14=tk.Button(self.ventana, text='\n  5 \n',  width=6, command=self.cinco)
        self.boton_14.grid(column=1, row=6)
        self.boton_14.configure(background='gray')
        self.boton_15=tk.Button(self.ventana, text='\n  6 \n',  width=6, command=self.seis)
        self.boton_15.grid(column=2, row=6)
        self.boton_15.configure(background='gray')
        self.boton_16=tk.Button(self.ventana, text='\n   - \n',  width=6, command=self.restar)
        self.boton_16.grid(column=3, row=6)
        self.boton_16.configure(background='dodgerblue')
        self.boton_17=tk.Button(self.ventana, text='\n  1 \n',  width=6, command=self.uno)
        self.boton_17.grid(column=0, row=7)
        self.boton_17.configure(background='gray')
        self.boton_18=tk.Button(self.ventana, text='\n  2 \n',  width=6, command=self.dos)
        self.boton_18.grid(column=1, row=7)
        self.boton_18.configure(background='gray')
        self.boton_19=tk.Button(self.ventana, text='\n  3 \n',  width=6, command=self.tres)
        self.boton_19.grid(column=2, row=7)
        self.boton_19.configure(background='gray')
        self.boton_20=tk.Button(self.ventana, text='\n  + \n',  width=6, command=self.sumar)
        self.boton_20.grid(column=3, row=7)
        self.boton_20.configure(background='dodgerblue')
        self.boton_21=tk.Button(self.ventana, text='\n+/-\n',  width=6, command=self.masmenos)
        self.boton_21.grid(column=0, row=8)
        self.boton_21.configure(background='gray')
        self.boton_22=tk.Button(self.ventana, text='\n  0 \n',  width=6, command=self.cero)
        self.boton_22.grid(column=1, row=8)
        self.boton_22.configure(background='gray')
        self.boton_23=tk.Button(self.ventana, text='\n  .  \n',  width=6, command=self.punto)
        self.boton_23.grid(column=2, row=8)
        self.boton_23.configure(background='gray')
        self.boton_24=tk.Button(self.ventana, text='\n  = \n',  width=6, command=self.igual)
        self.boton_24.grid(column=3, row=8)
        self.boton_24.configure(background='aqua')
        #Muestro la ventana
        self.ventana.mainloop()
    #Funciones de los botones    
    def cero(self):
        if self.operacion!= '':
            self.text2=self.text2+'0'
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
        else:
            self.text=self.text+'0'
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
    def uno(self):
        if self.operacion!= '':
            self.text2=self.text2+'1'
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
        else:
            self.text=self.text+'1'
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
    def dos(self):
        if self.operacion!= '':
            self.text2=self.text2+'2'
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
        else:
            self.text=self.text+'2'
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
    def tres(self):
        if self.operacion!= '':
            self.text2=self.text2+'3'
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
        else:
            self.text=self.text+'3'
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
    def cuatro(self):
        if self.operacion!= '':
            self.text2=self.text2+'4'
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
        else:
            self.text=self.text+'4'
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
    def cinco(self):
        if self.operacion!= '':
            self.text2=self.text2+'5'
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
        else:
            self.text=self.text+'5'
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
    def seis(self):
        if self.operacion!= '':
            self.text2=self.text2+'6'
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
        else:
            self.text=self.text+'6'
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
    def siete(self):
        if self.operacion!= '':
            self.text2=self.text2+'7'
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
        else:
            self.text=self.text+'7'
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
    def ocho(self):
        if self.operacion!= '':
            self.text2=self.text2+'8'
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
        else:
            self.text=self.text+'8'
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
    def nueve(self):
        if self.operacion!= '':
            self.text2=self.text2+'9'
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
        else:
            self.text=self.text+'9'
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
    def punto(self):
        if self.operacion!= '':
            self.text2=self.text2+'.'
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
        else:
            self.text=self.text+'.'
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
    def igual(self):
        if ' + ' in self.operacion:
            self.resultado=float(self.text)+float(self.text2)
            self.label_4.configure(text=self.resultado)
            self.text=self.resultado
            self.text2=''
            self.operacion=''
            self.text3=self.text,self.operacion, self.text2 
        elif ' - ' in self.operacion:
            self.resultado=float(self.text)-float(self.text2)
            self.label_4.configure(text=self.resultado)
            self.text=self.resultado
            self.text2=''
            self.operacion=''
            self.text3=self.text,self.operacion, self.text2 
        elif ' ÷ ' in self.operacion:
            self.resultado=float(self.text)/float(self.text2)
            self.label_4.configure(text=self.resultado)
            self.text=self.resultado
            self.text2=''
            self.operacion=''
            self.text3=self.text,self.operacion, self.text2 
        elif ' x ' in self.operacion:
            self.resultado=float(self.text)*float(self.text2)
            self.label_4.configure(text=self.resultado)
            self.text=self.resultado
            self.text2=''
            self.operacion=''
            self.text3=self.text,self.operacion, self.text2
        elif ' % ' in self.operacion:
            if self.text!= '' and self.text2 != '':
                self.resultado=float(self.text)*float(self.text2)/100
                self.label_4.configure(text=self.resultado)
                self.text=self.resultado
                self.text2=''
                self.operacion=''
                self.text3=self.text,self.operacion, self.text2
            elif self.text!='' and self.text2=='':
                self.resultado=float(self.text)*100/100
                self.label_4.configure(text=self.resultado)
                self.text=self.resultado
                self.text2=''
                self.operacion=''
                self.text3=self.text,self.operacion, self.text2
        elif ' √ ' in self.operacion:
            self.resultado=raiz(int(self.text2))
            self.label_4.configure(text=self.resultado)
            self.text=self.resultado
            self.text2=''
            self.operacion=''
            self.text3=self.text,self.operacion, self.text2
        elif ' ^(2) 'in self.operacion:
            self.resultado=int(self.text)*int(self.text)
            self.label_4.configure(text=self.resultado)
            self.text=self.resultado
            self.text2=''
            self.operacion=''
            self.text3=self.text,self.operacion, self.text2
    def sumar(self):
        if self.operacion!= '':
            self.label_4.configure(text=self.text3)
        elif self.text=='' and self.text2=='':
            self.label_4.configure(text=self.text3)
        else:
            self.operacion=self.operacion+' + '
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
    def restar(self):
        if self.operacion== '' and self.text=='':
            self.text='-'
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
        elif self.text != '' and self.operacion!= '' and self.text2== '':
            self.text2='-'
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
        elif self.text=='' and self.text2=='':
            self.label_4.configure(text=self.text3)
        else:
            self.operacion=self.operacion+' - '
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
    def dividir(self):
        if self.operacion!= '':
            self.label_4.configure(text=self.text3)
        elif self.text=='' and self.text2=='':
            self.label_4.configure(text=self.text3)
        else:
            self.operacion=self.operacion+' ÷ '
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
    def multiplicar(self):
        if self.operacion!= '':
            self.label_4.configure(text=self.text3)
        elif self.text=='' and self.text2=='':
            self.label_4.configure(text=self.text3)
        else:
            self.operacion=self.operacion+' x '
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
    def C(self):
        self.text=''
        self.operacion=''
        self.text2=''
        self.text3=self.text,self.operacion, self.text2
        self.label_4.configure(text=self.text3)
    def borrar(self):
        if self.operacion!= '':
            borrado=self.text2[:-1]
            self.text2=borrado
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
        elif self.text2=='' and self.operacion=='':
            borrado=self.text[:-1]
            self.text=borrado
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
        else:
            self.operacion=''
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
    def porcentaje(self):
        if self.operacion!= '':
            self.label_4.configure(text=self.text3)
        else:
            self.operacion=self.operacion+' % '
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
    def raiz(self):
        if self.operacion!= '':
            self.label_4.configure(text=self.text3)
        else:
            self.operacion=self.operacion+' √ '
            self.text=''
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
    def CE(self):
        if self.text2=='':
            self.text=''
            self.operacion=''
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
        else:
            self.text2=''
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
    def fraccion(self):
        if self.operacion!= '':
            self.label_4.configure(text=self.text3)
        elif self.text=='' and self.text2=='':
            self.text= '1'
            self.operacion=' ÷ '
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
        else:
            self.text='1'
            self.operacion=self.operacion+' ÷ '
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
    def cuadrado(self):
        if self.operacion!= '':
            self.label_4.configure(text=self.text3)
        elif self.text=='' and self.text2=='':
            self.label_4.configure(text=self.text3)
        else:
            self.operacion=self.operacion+' ^(2) '
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
    def masmenos(self):
        if self.operacion != '':
            cambio=int(self.text2)*-1
            self.text2=cambio
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
        else:
            cambio=int(self.text)*-1
            self.text=cambio
            self.text3=self.text,self.operacion, self.text2
            self.label_4.configure(text=self.text3)
#Llamo a la clase Calculadora
calculdora1=Calculdora()