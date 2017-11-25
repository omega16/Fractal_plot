#!/usr/bin/env python3

import numpy as np
import sys
from matplotlib import pyplot as plt
from matplotlib import gridspec
from mpl_toolkits.mplot3d import Axes3D
import sympy as sy












"""


24-Nov-2017

Metodo general para ver fractales



Proyecto echo para la clase de Topologia II en ESFM-IPN 
Omega16 (nombre omitido por privacidad)
https://github.com/omega16/Fractal_plot


La forma de usar estas funciones se encuentra en driver.py (se recomienda agregar una funcion nueva a driver.py para crear un nuevo fractal)



"""




def limite(no_funciones,no_iteraciones):
    return no_funciones*((2**no_iteraciones)-1)
    
    
    
    
    
    
def funciones1(iteraciones,lista):
    """Dada una lista de funciones de sympy, calcula las posibles composiciones de longitud 'iteraciones' de  las funciones """
    aux =[lista] 
    aux2 = []
    for j in range(0,iteraciones):
        #print(j)
        if j == 0:

            for i in aux[0]:
                for w in aux[0]:
                    aux2.append(w.subs({'x':i}))
            aux.append(aux2)
        else :
            for i in aux[1]:
                for w in aux[0]:
                    aux2.append(w.subs({'x':i}))
        
            aux[1] = aux2
            
        aux2 =[]
    
        
    return aux[1]









def funciones2(iteraciones, lista, simbolos):
    """Dada una lista de funciones de sympy, calcula las posibles composiciones de longitud 'iteraciones' de  las funciones
        Las funciones en la lista deben ser de n-argumentos (n>1) pero deben ser campos escalares """
    aux =[lista] 
    aux2 = []
    for j in range(0,iteraciones):
        print("Numero de Iteración: ",j)
        if j == 0:

            for i in aux[0]:
                for w in aux[0]:
                    aux2.append(compone(w,i,simbolos))
            aux.append(aux2)
        else :
            for i in aux[1]:
                for w in aux[0]:
                    aux2.append(compone(w,i,simbolos))
        
            aux[1] = aux2
            
        aux2 =[]
    
        
    return aux[1]











def  funciones_simetrico(iteraciones,funcion,simbolos=[]):
    aux = funcion
    for i in range(0,iteraciones):

        funcion = compone(aux,funcion,simbolos)

    return funcion








def funciones(iteraciones,lista,simbolos=[]):
    if simbolos == [] :
        return funciones1(iteraciones,lista)
    else : 

        return funciones2(iteraciones,lista,simbolos)









    
def compone(f,g,simbolos):
    simbolos_aux = sy.symbols('y:'+str(len(simbolos)))
    aux = []

    for i in range(0,len(f)):
               
        aux.append(g[i].subs({simbolos[j]:f[j].subs({simbolos[w]:simbolos_aux[w] for w in range(0,len(simbolos)) })  for j in range(0,len(simbolos)) }))
        aux[-1] = aux[-1].subs( {simbolos_aux[j]:simbolos[j] for j in range(0,len(simbolos))} )
    

    return aux
    
    
    
    
    
    
    
    
    
    
    
 
def convierte1(funciones):
    final =[]
    x = sy.symbols('x')
    for i in funciones:

       final.append(sy.lambdify(x,i,modules=['numpy']))

    return final








def convierte_n(funciones,simbolos):
    final =[]
    for i in funciones:

       final.append(sy.lambdify(simbolos,i,modules=['numpy']))

    return final
    
    


def evaluar(funciones,conjunto,nombre,dim=3):
            p=[funciones[i](*conjunto) for i in range(0,len(funciones)) ]
            p1=[[p[i][k] for i in range(0,len(p)) ]for k in range(0,len(conjunto))]
            p2=[np.concatenate(p1[k]) for k in range(0,len(conjunto))]
            if dim==1:
                np.savez_compressed(nombre,x=p2[0],y=np.zeros(p2[0].shape[0]))
            elif len(conjunto)==2:
                np.savez_compressed(nombre,x=p2[0],y=p2[1])
            elif len(conjunto)==3:
                np.savez_compressed(nombre,x=p2[0],y=p2[1],z=p2[2])
        
            return p2
    






    
def cargar_puntos(nombre):
        return np.load(nombre)
        
  
  
    
    
def cargar_funciones(nombre):  
        
        archivo = np.genfromtxt(nombre ,delimiter=',', dtype='str')

        #return [[sy.sympify(archivo[i][0],x),sy.sympify(archivo[i][1],x),sy.sympify(archivo[i][2],x)] for i in range(0,len(archivo))]
        if len(archivo[0][0])==1:
            x = sy.symbols('x:1')
            return [[sy.sympify(archivo[i],x)] for i in range(0,len(archivo[0])) ]
        else:
            x = sy.symbols('x:'+str(len(archivo[0])))
            return [[sy.sympify(archivo[i][k],x) for k in range(0,len(archivo[0]))] for i in range(0,len(archivo))]
   
   
        
def plot_arch_2d(nombre,nombre2='fractal.svg',guarda=1,ancho_plot=0.2):
         
        fig = plt.figure()
        puntos = cargar_puntos(nombre)

        plt.scatter(puntos['x'],puntos['y'],s=ancho_plot)
        
        if guarda==1:
            plt.savefig(nombre2)
        
        plt.show()
        
        
    
def plot_arch_3d(nombre,nombre2='fractal.svg',guarda=1,ancho_plot=0.2):  
   
        fig = plt.figure()
        
        puntos = cargar_puntos(nombre)
        
     
        ax = Axes3D(fig)

        ax.scatter(puntos['x'],puntos['y'],puntos['z'],s=ancho_plot)
        
        
        if guarda==1:
            plt.savefig(nombre2)
        
        plt.show()
        
        
        
        
        
def plot(funciones,ancho_plot=0.1,nombre="fractal.png",conjunto=np.array([[0.5,0.5]]),guardar=1,dim=3):
        
        """Funciones = Lista de funciones de python que devuelven una lista 
           ancho_plot = ancho de los puntos que se plotean
           nombre = nombre para guardar el ploteo 
           conjunto = np.([[]]) , lista convertida a arrays
        
        """
        
        
        fig = plt.figure()
        
             
        p2= evaluar(funciones,conjunto,nombre[:-4],dim)
                
        if dim ==3:     
            ax = Axes3D(fig)

            ax.scatter(p2[0],p2[1],p2[2],s=ancho_plot)
        elif dim==2:
            plt.scatter(p2[0],p2[1],s=ancho_plot)
        elif dim ==1 :
            plt.scatter(p2[0],np.zeros(p2[0].shape[0]),s=ancho_plot)
            
            
            
        if guardar==1:
            plt.savefig(nombre)    

        plt.show()
    



   
   
   
    
    
def general(iteraciones,funcion_lista,simbolos,conjunto,ancho_plot,nombre,guardar=1,eva=0):


    print("Esto realizara un posible numero de operaciones : ",6*(len(funcion_lista[0])**2)*len(funcion_lista)*((2**iteraciones)-1) )
    
    dim = len(funcion_lista[0])
    
    print("Comenzando el proceso con iteraciones: ",iteraciones)
    print("Iniciando la composicion de funciones")
    
    f = funciones(iteraciones,funcion_lista,simbolos)
    
    
    print("Proceso de composicion terminado")
    print("Guardando funciones en : ",nombre[:-4]+'_funciones.txt')
    
    
    with open(nombre[:-4]+'_funciones.txt','a') as outf:    
        """if dim==3:
            for j in f:
                outf.write("  {0:}    {1:}   {2:}  \n ".format(str(j[0])+',', str(j[1])+',' , str(j[2]) ))
        elif dim==2:
            for j in f:
                outf.write("  {0:}    {1:}   \n ".format(str(j[0])+',', str(j[1]) ))
    
        elif dim==1:
            for j in f:
                outf.write("  {0:}   \n ".format(str(j[0])) )"""
                
        aux =''
        if dim==1:
            aux = '{0:}'
        else :
            for i in range(0,dim-1):
                aux = aux+' {'+str(i)+':},'
            aux = aux + '{'+str(dim-1)+':}'
        aux=aux+'\n'
        for j in f:
            outf.write(aux.format(*[str(j[k]) for k in range(0,len(j)) ] ) )
        
    print("-------------------------------------------------------------------------------------------------------------------------")
    
    if eva==1:
        print("Iniciando conversion de funciones simbolicas en funciones de python")
        a = convierte_n(f,simbolos)
        print("Proceso de conversion de funciones terminado")
        print("-------------------------------------------------------------------------------------------------------------------------")

  
    

        print("Comenzando ploteo de fractal")
        plot(a,0.1,nombre,conjunto,guardar,dim)
        print("Proceso terminado")
    
    else :
        print("Proceso terminado")

    
    
    

