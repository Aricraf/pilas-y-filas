
############### listas.py ###############
import os
class Lista:
    def __init__(self,datos=[]):
       self.lista = datos
        
    def push(self):
        nombre= int(input("Ingrese Los Elementos Que Desea En La Lista: "))
        for x in range (nombre):
            dato = input('Inserte Un Nuevo Elemento: ')
            self.lista.append(dato)

    def show(self):
        if len(self.lista) != 0:
            print(f'Mostrando Lista: {self.lista}\n')
        else:
            print('Lista Vacia\n')

    def pop(self):
        if len(self.lista) != 0:
            self.lista.pop()
            print(f'Mostrando Lista Nueva: {self.lista}\n')
        else:
            print('Lista Vacia\n')

    def eliminarElemento(self):
        if len(self.lista) == 0:
            print('Lista Vacia\n')
        else:
            opc = int(input('Ingrese Una Posicion Que Desea Borrar: '))
            while opc > (len(self.lista)- 1):
                opc = int(input('Posicion inexistente, vuelva a ingresar posicion: '))
            else:
                print(f'Elemento borrado: {self.lista.pop(opc)}')
                print(f'Mostrando lista nueva: {self.lista}\n')
    
    def insertarElemento(self):
        if len(self.lista) == 0:
            print('Lista vacia\n')
        else:
            opc = input('Ingrese el nuevo elemento: ')
            opc1 = int(input('Ingrese la posicion en la que desea insertar el nuevo dato: '))
            while opc1 > (len(self.lista) - 1):
                opc1 = int(input('Posicion inexistente, vuelva a ingresar nuevamente posicion: '))
            else:
                self.lista.insert(opc1, opc)
                print(f'Elemento esta insertado en la posicion {opc1}: {opc}')
                print(f'Mostrando la lista nueva: {self.lista}\n')

    def buscar(self):
        if len(self.lista) != 0:
            pos = input('Ingrese el elemento para retornar una posicion: ')
            if pos in self.lista:
                print(f'Posicion: {self.lista.index(pos)}\n')
            else:
                print(f'Imprimiendo el elemento de la posicion -1: {self.lista[-1]}\n')
        else:
            print('Lista vacia\n')