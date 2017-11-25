#!/usr/bin/env python3

import numpy as np
import sys
from matplotlib import pyplot as plt
from matplotlib import gridspec
from mpl_toolkits.mplot3d import Axes3D

import sympy as sy


import funciones_fractal as ff

"""

24-Nov-2017

Metodo general para ver fractales



Proyecto echo para la clase de Topologia II en ESFM-IPN 
Omega16 (nombre omitido por privacidad)
https://github.com/omega16/Fractal_plot

Ver Readme en git para encontrar instrucciones sobre las librerias usadas




Metodo de uso :

Para usar una funcion ya echa de este archivo, basta con importarlo a python usando:
import driver as dv 

(dv es un apodo corto para la libreria )

y luego hacer dv.funcion(parametros)





Se puede generar un fractal propio de la siguiente forma:






Se recomienda definir una nueva funcion que sirva para dibujar distintas versiones del fractal, con la forma:

def nombre_funcion_que_se_quiere(num_puntos,iteraciones,evaluar=0)

x=sy.symbols('x:i') declaran como variables de la funcion a los simbolos x0,x1,x2,...,xi


conjunto = np.random.random_sample((dim,num_puntos)) genera puntos aleatorios en [0,1]^dim  , solo es necesario si se planea dibujar el fractal usando los puntos (se puede remplazar estos puntos aleatorios por puntos sobre una curva o superficie)


funciones = [[f1,f2,...,fdim],[g1,g2,...,gdim],...,[h1,h2,...,hdim]]

[f1,f2,...,fdim] es una sola funcion simbolica y cada fi es una funcion componente , por ejemplo para el conjunto de cantor el sistema de funciones que se puede usar es f(x)=x/3 y g(x)=1- x/3, para este sistema en particular se escribe :
funciones = [[sy.sympify('x0/3')],[sy.sympify('x0/3')]]

Para un IFS en [0,1]^2 que tenga por funciones f(x,y) = (cos(x)/2,sen(y)) , g(x,y) = (12+(y/10) , (x/4)+2 ) se escribe:
funciones = [[sy.sympify('cos(x0)/2'),sy.sympify('sin(x1)')],[sy.sympify('(x1/10)+12'),sy.sympify('(x0/4)+2')]]

Note que x se remplazo por x0, mientras y se a remplazado por x1, en este caso se tendria x=sy.symbols('x:2')

Por supuesto como en los ejemplos se puede acortar este proceso en algunos casos.


finalmente  se llama a la funcion general en funciones_fractal como :

ff.general(iteraciones,funcion_lista,simbolos,conjunto,ancho_plot,nombre,guardar=1,eva=0)

iteraciones: numero de iteraciones a mostrar (al momento de ejecutar se dira que se hicieron n-1 iteraciones de las pedidas)
funcion_lista : funciones como fue declarado antes
simbolos : x =sy.symbols('x:i')
conjunto : como fue declarado antes
ancho_plot: transparencia de los puntos cuando se dibuje el fractal (valor entre 0 y 1)
nombre : 'Direccion/a/la/carpeta/donde/guardara/el/fractal/nombre_del_fractal_a_dibujar.svg'
guardar: La composicion de las funciones iteradas siempre se guarda en un archivo txt, este parametro guarda una imagen del dibujo del fractal si guardar = 1 , en caso contrario no guarda el dibujo.
eva: Si eva=0 solamente se componen y se guardan las funciones en un txt, si eva=1 se procede a convertir las funciones a funciones de python y evaluar las funciones en los puntos de conjunto para luego dibujar el fractal


Advertencia:
NO se admiten funciones constantes en el IFS


Se guardan a lo mas tres archivos al termino de la llamada a esta funcion, correspondientemente son : 
txt donde se almacenan las composiciones del IFS
.npz donde se guardan los puntos que componen el dibujo del fractal
.svg imagen vectorial del dibujo del fractal

para ver un fractal ya procesado se usan las funciones plot_arch_ y cargar en ff 








"""

def cantor_1d(num_puntos,iteraciones,evaluar=0):
    x= sy.symbols('x:1')
    conjunto = np.random.random_sample((1,num_puntos))
    f=[[x[0]/3],[1- x[0]/3]]    
    ff.general(iteraciones,f,x,conjunto,0.9,"Cantor_1d_iter_"+str(iteraciones)+'_puntos_'+str(num_puntos)+'.svg',1,evaluar)     
    return 
    

def cantor_2d(num_puntos,iteraciones,evaluar=0):
    x= sy.symbols('x:2')
    general =    [x[0]/3,x[1]/3]  
    puntos = [ [0,0] ,[2.0/3,0],[0,2.0/3], [2.0/3,2.0/3]  ]
    funciones = [ [general[0]+i[0] , general[1]+i[1]] for i in puntos]
    conjunto = np.random.random_sample((2,num_puntos))
    ff.general(iteraciones,funciones,x,conjunto,0.9,"Cantor_2d_iter_"+str(iteraciones)+'_puntos_'+str(num_puntos)+'.svg',1) 


def casi_cantor_2d(num_puntos,iteraciones,evaluar=0):
    x= sy.symbols('x:2')
    general =    [x[0]/3,x[1]/3]  
    puntos = [ [0,0] ,[2.0/3,0],[0,2.0/3],[0.3333333,0.33333333], [2.0/3,2.0/3]  ]
    funciones = [ [general[0]+i[0] , general[1]+i[1]] for i in puntos]
    conjunto = np.random.random_sample((2,num_puntos))
    ff.general(iteraciones,funciones,x,conjunto,0.9,"casi_Cantor_2d_iter_"+str(iteraciones)+'_puntos_'+str(num_puntos)+'.svg',1,evaluar) 


def cantor_3d(num_puntos,iteraciones,evaluar=0):
    x= sy.symbols('x:3')
    general =    [x[0]/3,x[1]/3,x[2]/3]  
    puntos=[[0,0,0] ,[0.666666,0,0],[0,0.66666,0],[0.66666,0.666666,0],[0,0,0.66666666],[0.66666,0,0.66666666666],[0,0.666666666666,0.666666666666],[0.66666,0.666666,0.66666666666]]
    funciones = [ [general[0]+i[0] , general[1]+i[1], general[2]+i[2]] for i in puntos]
    conjunto = np.random.random_sample((3,num_puntos))
    ff.general(iteraciones,funciones,x,conjunto,0.9,"Cantor_3d_iter_"+str(iteraciones)+'_puntos_'+str(num_puntos)+'.svg',1,evaluar) 
    
def casi_cantor_3d(num_puntos,iteraciones,evaluar=0):
    x= sy.symbols('x:3')
    general =    [x[0]/3,x[1]/3,x[2]/3]  
    puntos=[[0,0,0] ,[0.666666,0,0],[0,0.66666,0],[0.66666,0.666666,0],[0,0,0.66666666],[0.66666,0,0.66666666666],[0,0.666666666666,0.666666666666],[0.66666,0.666666,0.66666666666],[0.333333,0.333333,0.3333333333]]
    funciones = [ [general[0]+i[0] , general[1]+i[1], general[2]+i[2]] for i in puntos]
    conjunto = np.random.random_sample((3,num_puntos))
    ff.general(iteraciones,funciones,x,conjunto,0.9,"casi_Cantor_2d_iter_"+str(iteraciones)+'_puntos_'+str(num_puntos)+'.svg',1,evaluar) 


def nuevo_1(num_puntos,iteraciones,evaluar=0):
    x= sy.symbols('x:3')
    general =    [sy.sympify('sin(x0)'),sy.sympify('sin(x1)'),sy.sympify('sin(x2)')]  
    puntos=[[1,1,1],[2,2,2]]
    funciones = [ [general[0]+i[0] , general[1]+i[1], general[2]+i[2]] for i in puntos]
    conjunto = np.random.random_sample((3,num_puntos))
    ff.general(iteraciones,funciones,x,conjunto,0.9,"nuevo_1"+str(iteraciones)+'_puntos_'+str(num_puntos)+'.svg',1,evaluar)

def nuevo_2(num_puntos,iteraciones,evaluar=0):
    x= sy.symbols('x:3')
    general =    [sy.sympify('(cos(x0)*sin(x0))/4 + (cos(x1)*sin(x1))/4 + (cos(x2)*sin(x2))/4'),sy.sympify('(cos(x0)*sin(x0))/4 + (cos(x1)*sin(x1))/4 + (cos(x2)*sin(x2))/4'),sy.sympify('(cos(x0)*sin(x0))/4 + (cos(x1)*sin(x1))/4 + (cos(x2)*sin(x2))/4')]  
    puntos=[[1,1,1],[2,2,2]]
    funciones = [ [general[0]+i[0] , general[1]+i[1], general[2]+i[2]] for i in puntos]
    conjunto = np.random.random_sample((3,num_puntos))
    ff.general(iteraciones,funciones,x,conjunto,0.9,"nuevo_2"+str(iteraciones)+'_puntos_'+str(num_puntos)+'.svg',1,evaluar)

def sierpinski_3d(num_puntos,iteraciones,evaluar=0):
    x= sy.symbols('x:3')
    general =    [x[0]/2,x[1]/2,x[2]/2]  
    puntos=[[0,0,0] ,[0.5,0,0],[0,0.5,0],[0.5,0.5,0],[0.25,0.25,0.5]]
    funciones = [ [general[0]+i[0] , general[1]+i[1], general[2]+i[2]] for i in puntos]
    conjunto = np.random.random_sample((3,num_puntos))
    ff.general(iteraciones,funciones,x,conjunto,0.9,"Sierpinski_3d_iter_"+str(iteraciones)+'_puntos_'+str(num_puntos)+'.svg',1,evaluar) 


"""

set = np.random.random_sample((3,100))
p=[F[i](*set) for i in range(0,len(F)) ]
p1=[p[i][0] for i in range(0,len(p))]
p2 = np.concatenate(p1,axis=0)


set = np.random.random_sample((3,100))
p=[F[i](*set) for i in range(0,len(F)) ]
p1=[[p[i][k] for i in range(0,len(p)) ]for k in [0,1,2]]
p2=[[np.concatenate(p1[k])] for k in [0,1,2]]

"""



#Para los siguientes se usa general =    [x[0]/2,x[1]/2]  
#Para cantor puntos = [ [0,0] ,[2.0/3,0],[1.0/3,1.0/3],[0,2.0/3], [2.0/3,2.0/3]  ]

#Para serpinskie puntos = [ [0,0] ,[0.25,0.25*(3**0.5)],[0.5,0]  ]

#puntos = [ [i,j,k] for i in [0.0,0.3333333333,0.66666666] for j in [0.0,0.3333333333,0.66666666] for k in [0.0,0.3333333333,0.66666666]  ]








#ff.general(int(sys.argv[1]),funciones,x,conjunto,float(sys.argv[2]),"fractal2.svg",1) 

