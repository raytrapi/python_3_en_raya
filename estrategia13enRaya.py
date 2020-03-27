import random
import reglas3enRaya

#Retorna una un Objeto de tipo {"casilla":, "probabilidad"}
def opciones(tablero,casillasVacias,ficha, juegaOponente,nivelMaximo=5,casillas_probar=9, mejor=True):
   
   fichaOponente="X" if ficha=="O" else "O"
   candidatos={}
   casillasVaciasT=[]
   for j in range(len(casillasVacias)):
      casillasVaciasT.append(casillasVacias[j])
   while len(candidatos)<casillas_probar and len(casillasVaciasT)>0:
      candidato=random.randint(0,len(casillasVaciasT)-1)
      candidatos[casillasVaciasT[candidato]]=0.5
      casillasVaciasT.remove(casillasVaciasT[candidato])
   if(len(candidatos)==0):
      return candidatos
   #Comprobamos que resultado tenemos con cada uno de los candidatos
   for candidato in candidatos:
      #Comprobamos si ganamos
      if reglas3enRaya.hemosGanado(candidato,ficha,tablero):
         candidatos[candidato]=1 if juegaOponente else 0
      else:
         if(nivelMaximo>0):
            tableroT=[]
            for j in range(len(tablero)):
               tableroT.append(tablero[j])
            casillasVaciasT=[]
            for j in range(len(casillasVacias)):
               casillasVaciasT.append(casillasVacias[j])
            tableroT[candidato]=ficha
            casillasVaciasT.remove(candidato)

            opcionesT=opciones(tableroT,casillasVaciasT,fichaOponente,not juegaOponente,nivelMaximo-1,casillas_probar,mejor)
            for opcion in opcionesT:
               candidatos[opcion]=(candidatos[opcion]+opcionesT[opcion])/2
   return candidatos


def laOpcion(tablero,casillasVacias,ficha, juegaOponente,nivelMaximo=5,casillas_probar=9):
   probabilidades=opciones(tablero,casillasVacias,ficha,juegaOponente,nivelMaximo,casillas_probar,True)
   mejorOpcion=-1
   mejorProbabilidad=-1
   for opcion in probabilidades:
      if(mejorProbabilidad<probabilidades[opcion]):
         mejorOpcion=opcion
         mejorProbabilidad=probabilidades[opcion]

   print("La mejor opción tiene como probabilidad ",mejorProbabilidad)
   return mejorOpcion