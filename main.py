#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## -*- coding: utf-8 -*-

#ANDRADE CIELO JULIO CESAR
import csv
import itertools
import os
class contact:
    ID=itertools.count()
    def __init__(self,nombre,apellido,numeroCel,numeroCas,correo):
        self.ID=next(self.ID)
        self.nombre=nombre
        self.apellido=apellido
        self.numeroCel=numeroCel
        self.numeroCas=numeroCas
        self.correo=correo
class Agenda:
    def __init__(self):
        self.contactos=[]
    def ordenar(self,contactos):
        def Particionar(A,p,r):           #p primero y r ultimo elemento
            indice=(p-1)
            limite=A[r].nombre
            for j in range(p,r):
                if(A[j].nombre<=limite):
                    indice=indice+1
                    A[indice],A[j]=A[j],A[indice]
                    A[indice+1],A[r]=A[r],A[indice+1]
                    return (indice+1) 
        def QuickSort(A,p,r):
            if(len(A)<2):
                return A
            else:#Entro mientras que p es menor a r
                if p<r: 
                    qindice=Particionar(A,p,r)
                    QuickSort(A,p,qindice-1)
                    QuickSort(A,qindice+1,r)
                return A
            lista=QuickSort(self.contactos,0,len(self.contactos)-1)
            return lista
    def agregar(self,nombre,apellido,numeroCel,numeroCas,correo):
        contacto=contact(nombre,apellido,numeroCel,numeroCas,correo)
        self.contactos.append(contacto)
        
    def mostrar(self):
        self.ordenar(self.contactos)
        for contacto in self.contactos:
            self.imprimeContacto(contacto)
            
    def buscar(self,contactos,key):
        izq = 0                                         
        der = len(contactos) - 1                              
   
        while izq <= der:                               
            medio = int((izq+der)//2)                    
  
            if contactos[medio].nombre == key:                       
                self.imprimeContacto(contactos[medio])
                self.submenubusc(contactos[medio].ID)
                return 
            elif contactos[medio].nombre > key:                      
                der = medio - 1                         
            
            else:
                izq = medio + 1
        a=print("no se encontro ningun contacto con ese nombre")
        return a
        
    def eliminar(self,ID):
        for contacto in self.contactos:
            if contacto.ID==ID:
                print('Quieres borrarlo? (s/n)')
                opcion=str(input(""))
                if opcion=='s' or opcion=='S':
                    print('Borrando contacto!!!')
                    del self.contactos[ID]
                elif opcion=='n' or opcion=='N':
                    break
    def submenubusc(self,ID):
        print('')
        print('Quieres modificarlo o borrarlo? ')
        print('m modificar/ b borrar')
        print('')
        opcion=str(input(""))
        if opcion=='m' or opcion=='M':
            self.modificar(ID)
        elif opcion=='b' or opcion=='B':
            self.eliminar(ID)
        else:
            print('Continuamos sin realizar modificacion alguna\n')
            
            
            
    def modificar(self, ID):
        for contacto in self.contactos:
            if contacto.ID==ID:
                del self.contactos[ID]
                nombre=str(input("Escribe el nombre: "))
                apellido=str(input("Escribe el apellido: "))
                numeroCel=str(input("Escribe el numero de celular: "))
                numeroCas=str(input("Escribe el nuemro de casa:"))
                correo=str(input("Escribe el correo:"))
                contacto=contact(nombre.capitalize(),apellido.capitalize(),numeroCel,numeroCas,correo.capitalize())
                self.contactos.append(contacto)
                break
                
    def grabar(self):
        with open('agenda.csv','w') as file:
            escribir=csv.writer(file)
            escribir.writerow(('ID','nombre','apellido','numero de celular',"numero de casa","correo"))
            for contacto in self.contactos:
                escribir.writerow((contacto.ID,contacto.nombre,contacto.apellido,contacto.numeroCel,contacto.numeroCas,contacto.correo))
    
    
    def imprimeContacto(self,contacto):
        print('ID:{} '.format(contacto.ID))
        print('Nombre: {}'.format(contacto.nombre))
        print('Apellido: {}'.format(contacto.apellido))
        print('numero de celular: {}'.format(contacto.numeroCel))
        print('numero de casa: {}'.format(contacto.numeroCas))
        print('correo: {}'.format(contacto.correo))
    

              
def menu():
    agenda=Agenda()
    try:
        
        with open('agenda.csv', 'r') as file:
            lector=csv.DictReader(file)
            for fila in lector:
                agenda.agregar(fila['nombre'].capitalize(),fila['apellido'].capitalize(),fila['numero de celular'],fila['numero de casa'],fila['correo'].capitalize())
    except:
        print('SEA USTED BIENVENIDO POR PRIMERA VEZ A ELECTRONIC AGENT\n')
    
              
    Var_aux=True
    while Var_aux:
        os.system('clear')
        print("SEA USTED BIENVENIDO A ELECTRONIC AGENT\n")
        print("****************MENU****************\n\nSelecciona que opcion deseas realizar\n")
        print("1)Deseas añadir un contacto nuevo\n")
        print("2)Visualizar todos los contactos\n")
        print("3)Buscar a un contacto\n")
        print("4)Salir\n")
        opc=int(input('Opcion a escoger:  \n'))
        if opc==1:
            nombre=str(input('Escribe el nombre: '))
            apellido=str(input('Escribe el apellido: '))
            numeroCel=str(input('Escribe el numero de celular: '))
            numeroCas=str(input('Escribe el numero de casa: '))
            correo=str(input('Escribe el correo: ')) 
            agenda.agregar(nombre.capitalize(),apellido.capitalize(),numeroCel,numeroCas,correo.capitalize())
            agenda.grabar()
        elif opc==2:
            agenda.mostrar()
        elif opc==3:
            texto=str(input('Escribe el nombre que deseas buscar: '))
            agenda.buscar(agenda.contactos, texto.capitalize())
            agenda.grabar()
        elif opc==4:
            print("Gracias vuelve pronto, que tengas un excelente dia\n")
            agenda.grabar()
            Var_aux=False
        else:
            print("\nOPCION INVALIDA SELECCIONE OTRA OPCION\n")
            
            
            
            
if __name__=='__main__':
    menu() 

