import math
import random
import tablero3enRaya
import reglas3enRaya
import datetime
#print(int(datetime.datetime.timestamp(datetime.datetime.now())))
#print(time.microsecond)
random.seed(int(datetime.datetime.timestamp(datetime.datetime.now())))
#random.seed(5) 



jugadores=[]
numeroJugadores=tablero3enRaya.numero("Numero de jugadores: ",0,2)
for i in range(numeroJugadores):
   jugadores.append({"nombre":input("Nombre del jugador "+str(i+1)+": "),"tipo":"H"})
for i in range(2-numeroJugadores):
   jugadores.append({"nombre":"Maquina "+str(i+1),"tipo":"M"})

print("\n Empezamos la partica con los jugadores")
for jugador in jugadores:
   print("\t",jugador["nombre"])
numeroPartidas=1
if(numeroJugadores>0):
   empieza=tablero3enRaya.numero("¿Que jugador empieza? [1="+jugadores[0]["nombre"]+",2="+jugadores[1]["nombre"]+"]: ",1,2)
   if(empieza==2):
      jugadores.reverse()
else:
   numeroPartidas=tablero3enRaya.numero("Número de partidas a jugas [0-500]: ",0,500)
logJugada=""
resultados={"Ganadas":0,"Perdidas":0,"Empatadas":0}
for jugada in range(numeroPartidas):
   #Iniciamos el juego
   #if len(logJugada)>0:
   #   print(logJugada)
   logJugada=""
   tablero3enRaya.inicializar()
   continuar=True
   fichasEnTablero=0
   while continuar:
      #Pedimos posición de la ficha
      if(numeroJugadores!=0):
         tablero3enRaya.pintarTablero()
      numJugador=(fichasEnTablero&1)
      ficha='X' if numJugador==1 else 'O'
      logJugada+="Juega "+ficha+" - "
      if(jugadores[numJugador]["tipo"]=="H"):
         casilla=reglas3enRaya.colocarFicha(ficha)
      else:
         casilla=reglas3enRaya.colocarFichaMaquina(ficha,'X' if numJugador==0 else 'O',tablero3enRaya.tablero)
      if casilla==-1:
         tablero3enRaya.pintarTablero()
         continuar=False
         continue
      logJugada+="casilla "+str(casilla)+" - "
      tablero3enRaya.casillasVacias.remove(casilla)
      if(reglas3enRaya.hemosGanado(casilla,ficha,tablero3enRaya.tablero)):
         continuar=False
         if numeroJugadores>0:
            print(jugadores[numJugador]["nombre"],"¡¡¡¡¡Has ganado!!!!")
         else:
            logJugada+="Ha ganado "+jugadores[numJugador]["nombre"]+"\n"
         if(numJugador==0):
            resultados["Ganadas"]=resultados["Ganadas"]+1
         else:
            resultados["Perdidas"]=resultados["Perdidas"]+1
      fichasEnTablero+=1
      if(fichasEnTablero==9 and continuar):
         continuar=False
         resultados["Empatadas"]=resultados["Empatadas"]+1
         if numeroJugadores>0:
            print("TABLAS")
         else:
            logJugada+="Ha quedado en tablas \n"
   if numeroJugadores>0:
      tablero3enRaya.pintarTablero()
print(resultados)