import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Mateo Joaquin
apellido:Rivero Correa
---
Ejercicio: Simulacro de examen.
---
Enunciado:
Es la gala de eliminación del Gran Utniano y la producción nos pide un programa para contar los votos de los televidentes y saber cuál será el participante que deberá abandonar la casa más famosa del mundo.

Los participantes en la placa son: Giovanni, Gianni y Esteban. Matias no fue nominado y Renato no está en la placa esta semana por haber ganado la inmunidad.

Cada televidente que vota deberá ingresar:

Nombre del votante

Edad del votante (debe ser mayor a 13)

Género del votante (Masculino, Femenino, Otro)

El nombre del participante a quien le dará el voto negativo (Debe estar en placa)

No se sabe cuántos votos entrarán durante la gala.

Se debe informar al usuario:

El promedio de edad de las votantes de género Femenino 

Del votante más viejo, su nombre.

Nombre del votante más joven qué votó a Gianni.

Nombre de cada participante y porcentaje de los votos qué recibió.

El nombre del participante que debe dejar la casa (El que tiene más votos)
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        edad_votante = 0
        acumulador_fem = 0 
        edad_fem = 0
        cantidad_personas = 0
        votante_gianni = 0
        edad_mas_viejo = 0
        contador_votos = 0
        

        


        nombre = prompt('X', 'Ingrese su nombre')
        edad_votante = prompt('X', 'Ingrese su edad')
        edad_votante = int(edad_votante)
        if edad_votante < 13:
            edad_votante = alert('Error', 'Necesitas ser mayor a 13 anos para votar')
            
        sexo = prompt('X', 'Ingrese su sexo')
        while sexo != 'femenino' and sexo != 'masculino' and sexo != 'otro':
            sexo = prompt('Error', 'Re-Ingrese su sexo')
        nombre_participante = prompt('X', 'A quien desea votar(negativo)')
        while nombre_participante != 'Giovanni' and nombre_participante != 'Gianni' and nombre_participante != 'Esteban':
            nombre_participante = prompt('X', 'Vuelva ingresar al participante, Recuerde usar mayusculas')
        
        match sexo:
            case 'femenino':
                acumulador_fem = acumulador_fem + 1
                edad_fem = edad_fem + edad_votante
                promedio = 1
                promedio = acumulador_fem / edad_fem
            
                

            
                sexo = alert('X', f'El promedio de edad de votantes femeninas es: {promedio}')
        
            
        

        match edad_mas_viejo:
            case edad_votante:
                edad_mas_viejo < edad_votante
                edad_mas_viejo = nombre
                edad_mas_viejo = alert('X', f'El votante mas viejo es: {edad_mas_viejo}')
            
        match votante_gianni:
            case edad_votante:
                votante_gianni > edad_votante
                votante_gianni = nombre
                votante_gianni = alert('X', f'El votante de Gianni mas joven es: {votante_gianni}')
            
        

        




        



        
        



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
