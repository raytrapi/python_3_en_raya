import math
import random
import tablero3enRaya
import estrategia13enRaya
import estrategia23enRaya
NIVEL_DESPISTE=-1
#Colaca una ficha en el tablero

def numeroHermanos(casilla, ficha, v, h,tablero):
   f=math.floor(casilla/tablero3enRaya.TABLERO_COLUMNAS) #Obtengo la fila
   c=casilla % tablero3enRaya.TABLERO_COLUMNAS #columna
   fila_nueva=f+v
   if(fila_nueva<0 or fila_nueva>=tablero3enRaya.TABLERO_FILAS):
      return 0
   columna_nueva=c+h
   if(columna_nueva<0 or columna_nueva>=tablero3enRaya.TABLERO_COLUMNAS):
      return 0
   #No estamos en el limite así que
   #calculamos la nueva posición y vemos si hay la misma ficha
   pos=(fila_nueva*tablero3enRaya.TABLERO_COLUMNAS+columna_nueva)
   if(tablero[pos]!=ficha):
      return 0
   else:
      return 1+numeroHermanos(pos,ficha,v,h,tablero)

# comprobamos que la ficha colocada en la casilla indica tiene dos fichas similares en casillas contiguas
def hemosGanado(casilla, ficha, tablero):
   hermanos=numeroHermanos(casilla,ficha,-1,-1,tablero)+numeroHermanos(casilla,ficha,1,1,tablero)
   if(hermanos==2):
      return True
   hermanos=numeroHermanos(casilla,ficha,1,-1,tablero)+numeroHermanos(casilla,ficha,-1,1,tablero)
   if(hermanos==2):
      return True
   hermanos=numeroHermanos(casilla,ficha,-1,0,tablero)+numeroHermanos(casilla,ficha,1,0,tablero)
   if(hermanos==2):
      return True
   hermanos=numeroHermanos(casilla,ficha,0,-1,tablero)+numeroHermanos(casilla,ficha,0,1,tablero)
   if(hermanos==2):
      return True

def colocarFicha(ficha):
   print("Dame la posición de una ficha")
   while True:
      fila=tablero3enRaya.numero("Fila entre [1 y 3]: ", 1,3)-1 #Restamos uno ya que nuestro rango real está entre 0 y 2
      columna=tablero3enRaya.numero("Columna entre [1 y 3]: ",1,3)-1
      #Como mi tablero es de 3x3
      casilla=fila*tablero3enRaya.TABLERO_COLUMNAS+columna
      if(tablero3enRaya.tablero[casilla]!=' '):
         #Esa casilla ya está cubierta
         print("La casilla está ocupada")
      else:
         tablero3enRaya.tablero[casilla]=ficha
         return casilla
def colocarFichaMaquina(ficha, fichaContrincante, tablero):
   random.shuffle(tablero3enRaya.casillasVacias)
   despiste=random.randint(0,100)
   
   
   for casilla in tablero3enRaya.casillasVacias:
      if(hemosGanado(casilla,ficha, tablero)):
         if(despiste>NIVEL_DESPISTE):
            tablero3enRaya.tablero[casilla]=ficha
            return casilla
         else:
            print("No nos hemos fijado en que podíamos ganar")
   despiste=random.randint(0,100)
   for casilla in tablero3enRaya.casillasVacias:
      if(hemosGanado(casilla,fichaContrincante, tablero)):
         if(despiste>NIVEL_DESPISTE):
            tablero3enRaya.tablero[casilla]=ficha
            return casilla
         else:
            print("No nos hemos dado cuenta de que nos podían ganar")
   if ficha =="X":
      mejorOpcion=estrategia23enRaya.laOpcion(tablero,tablero3enRaya.casillasVacias,ficha,False)
   else:
      mejorOpcion=estrategia13enRaya.laOpcion(tablero,tablero3enRaya.casillasVacias,ficha,False)

   if(mejorOpcion!=-1):
      casilla=mejorOpcion
   else:
      if(len(tablero3enRaya.casillasVacias)>0):
         print("No hay mejor opción así que escojemos la primera de todas")
         casilla=tablero3enRaya.casillasVacias[0]
      else:
         return -1
   tablero3enRaya.tablero[casilla]=ficha
   return casilla


