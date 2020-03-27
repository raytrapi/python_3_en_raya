tablero=[]  #Nuestro tablero inicalmente serán nueva callisas vacias
casillasVacias=[]
TABLERO_FILAS=3
TABLERO_COLUMNAS=3
def inicializar():
   #inicializamos el tablero
   tablero.clear()
   casillasVacias.clear()
   for i in range(TABLERO_FILAS*TABLERO_COLUMNAS):
      tablero.append(' ')
      casillasVacias.append(i)
def numero(literal, inferior, superior):
   while True:
      valor=input(literal)
      while(not valor.isnumeric()):
         print("Solo se adminten números entre {0} y {1}".format(inferior,superior))
         valor=input(literal)
      coor=int(valor)
      if(coor>=inferior and coor<=superior):
         return coor

      else:
         print("El valor indicado es incorrecto, introduzca un número entre {0} y {1}".format(inferior,superior))
def pintarTablero():
   pos=0
   print(("-"*18))
   for fila in range(3):
      for columna in range(3):
         print("| ",tablero[pos]," ", end="")
         pos+=1
      print("|\n",("-"*18))