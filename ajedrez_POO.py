# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 14:24:52 2020

@author: chelo
"""
import numpy as np
class Pieza:
    def __init__(self,lado="blancas",posicion=None):
        self.lado=lado
        self.posicion=posicion
    
    def obtener_movimientos(self,posicion,tablero):
        self.posicion=posicion
        
        
        pass
        
    
    
    
class Alfil(Pieza):
    def obtener_movimientos(self,posicion,tablero):
        super().obtener_movimientos(posicion,tablero)
        

        fila,columna=self.posicion
        posiciones=tablero.tablero
        
        fila_original = fila
        columna_orignal = columna
        #izquierda superior
        while fila >= 0 and columna >= 0:
            posiciones[fila,columna] = 1
            fila = fila - 1
            columna = columna -1
            
        
        #derecha superior
        fila = fila_original
        columna = columna_orignal
        while fila >= 0 and columna <= 7:
            posiciones[fila,columna] = 1
            fila = fila - 1
            columna = columna + 1
            
        #izquierda inferior
        fila = fila_original
        columna = columna_orignal
        while fila <= 7 and columna >= 0:
            posiciones[fila,columna] = 1
            fila = fila + 1
            columna = columna - 1
            
        #derecho inferior
        fila = fila_original
        columna = columna_orignal
        while fila <= 7 and columna <= 7:
            posiciones[fila,columna] = 1
            fila = fila + 1
            columna = columna + 1
        posiciones[fila_original,columna_orignal] = 8
        
        return posiciones
    
class Peon(Pieza):
    def obtener_movimientos(self,posicion,tablero):
        super().obtener_movimientos(posicion,tablero)
        fila,columna=self.posicion
        posiciones=tablero.tablero
        posiciones[fila,columna] = 8
         
        if self.lado=="blancas":
            if fila!=0:
                if fila==6:
                    posiciones[fila-2,columna] = 1
   
                fila=fila-1
                posiciones[fila,columna] = 1
            
               
        else:
            if fila!=7:
                if  fila==1:
                    posiciones[fila+2,columna] = 1
                fila=fila+1
                posiciones[fila,columna] = 1
            
        
        

        
        
        
        
class Torre(Pieza):
    def obtener_movimientos(self,posicion,tablero):
        super().obtener_movimientos(posicion,tablero)
        fila,columna=self.posicion
        posiciones=tablero.tablero
        
     
        
        posiciones[:, columna] = 1
        posiciones[fila, :] = 1
        posiciones[fila,columna] = 8
        return posiciones
   
    pass
class Rey(Pieza):
     def obtener_movimientos(self,posicion,tablero):
        super().obtener_movimientos(posicion,tablero)
        fila,columna=self.posicion
        posiciones=tablero.tablero
        
        posiciones[fila,columna] = 8
        #no coge los extremos
        if (fila!=0 and columna!=0) and (fila!=7 and columna!=7):
            posiciones[fila+1,columna] = 1 #abajo
            posiciones[fila-1,columna] = 1 #arriba
            
            posiciones[fila,columna+1] = 1 #derecha
            posiciones[fila,columna-1] = 1 #izquierda
            
            #diagonales
            posiciones[fila+1,columna+1] = 1 #diagolan inferior derecha
            posiciones[fila-1,columna-1] = 1 #diagonal superior izquierda
            posiciones[fila-1,columna+1] = 1 #diagonal superior derecha
            posiciones[fila+1,columna-1] = 1 #diagonal inferior izq
            
            #coge extremo izquierdo
        elif columna==0:
            if fila==0:
               posiciones[fila+1,columna] = 1 #abajo
               posiciones[fila,columna+1] = 1 #derecha
              #posiciones[fila,columna-1] = 1 #izquierda
               posiciones[fila+1,columna+1] = 1 #diagolan inferior derecha
              #posiciones[fila+1,columna-1] = 1 #diagonal inferior izq
            elif fila!=7:
                 posiciones[fila+1,columna] = 1 #abajo
                 posiciones[fila,columna+1] = 1 #derecha
                 #tablero[fila,columna-1] = 1 #izquierda
                 posiciones[fila+1,columna+1] = 1 #diagolan inferior derecha
                 #tablero[fila+1,columna-1] = 1 #diagonal inferior izq
                 posiciones[fila-1,columna] = 1 #arriba
                 posiciones[fila-1,columna+1] = 1 #diagonal superior derecha
            else:
                posiciones[fila,columna+1] = 1 #derecha
                posiciones[fila-1,columna+1] = 1 #diagonal superior derecha
                posiciones[fila-1,columna] = 1 #arriba
                
                #coge extremo de arriba
        elif fila==0 and columna!=7:
          
            if  columna!=0:
                 posiciones[fila+1,columna] = 1 #abajo
                 posiciones[fila,columna+1] = 1 #derecha
                 posiciones[fila,columna-1] = 1 #izquierda
                 posiciones[fila+1,columna+1] = 1 #diagolan inferior derecha
                 posiciones[fila+1,columna-1] = 1 #diagonal inferior izq
        
        #coge extremo izquierda
        elif columna==7:
            if fila==0:
                posiciones[fila+1,columna] = 1 #abajo
              # tablero[fila,columna+1] = 1 #derecha
                posiciones[fila,columna-1] = 1 #izquierda
               #tablero[fila+1,columna+1] = 1 #diagolan inferior derecha
                posiciones[fila+1,columna-1] = 1 #diagonal inferior izq
            elif fila!=0 and fila!=7:
                 posiciones[fila+1,columna] = 1 #abajo
                 #tablero[fila,columna+1] = 1 #derecha
                 posiciones[fila,columna-1] = 1 #izquierda
                 #tablero[fila+1,columna+1] = 1 #diagolan inferior derecha
                 posiciones[fila+1,columna-1] = 1 #diagonal inferior izq
                 posiciones[fila-1,columna] = 1 #arriba
                 posiciones[fila-1,columna-1] = 1 #diagonal superior izq
            else:
                #tablero[fila,columna+1] = 1 #derecha
                #tablero[fila-1,columna+1] = 1 #diagonal superior derecha
                posiciones[fila-1,columna] = 1 #arriba
                posiciones[fila,columna-1] = 1 #izquierda
                posiciones[fila-1,columna-1] = 1 #diagonal superior izq
        
        #extremo abajo
        else:
                
               posiciones[fila,columna+1] = 1 #derecha
               posiciones[fila,columna-1] = 1 #izquierd
               posiciones[fila-1,columna-1] = 1 #diagonal superior izq
               posiciones[fila-1,columna+1] = 1 #diagonal superior derecha
               posiciones[fila-1,columna] = 1 #arriba
               
           
            
           
        
        
class Dama(Alfil,Torre):
    def obtener_movimientos(self,posicion,tablero):
        
        #super().obtener_movimientos(posicion,tablero)
        Torre.obtener_movimientos(self,posicion,tablero)
        Alfil.obtener_movimientos(self,posicion,tablero)
        
    
        
        
class Caballo(Pieza):
     def obtener_movimientos(self,posicion,tablero):
        super().obtener_movimientos(posicion,tablero)
        fila,columna=self.posicion
        posiciones=tablero.tablero
        
        posiciones[fila,columna] = 8
        
        
            #abajo  parte izquierda  largo
        rfila=fila+2
        rcolumna=columna-1
        if rfila <= 7 and 0 <= rcolumna:
         
        # posiciones[fila+1,columna]=1 #mover abajo
         #posiciones[fila+2,columna]=1 #mover 2 abajo
         #tablero[fila+2,columna+1]=1 #derecha
         posiciones[fila+2,columna-1]=1 #izquierda
         
         
         #abajo parte derecha largo
         
        rcolumna4=columna+1
        rfila4=fila+2
        if rcolumna4 <=7 and rfila4 <=7:
         
         #posiciones[fila+1,columna]=1 
         #posiciones[fila+2,columna]=1
         posiciones[fila+2,columna+1]=1 
         #tablero[fila-2,columna+1]=1 
         
        
        #abajo parte derecha corto
        rfila2=fila+1
        rcolumna2=columna+2
        if rfila2 <= 7 and rcolumna2 <= 7:
            #posiciones[fila+1,columna+1]=1 
            posiciones[fila+1,columna+2]=1 
            
            #posiciones[fila+1,columna]=1
        
           
        
        #abajo parte izquierda corto
        rfila5=fila+1
        rcolumna5=columna-2
        if rfila5 <=7  and 0 <=rcolumna5:
            posiciones[fila+1,columna-2]=1 
          #  posiciones[fila+1,columna-1]=1 
         
           # posiciones[fila+1,columna]=1 
            #tablero[fila-1,columna+1]=1 
        
        #arriba parte izquiera corto
        rfila6=fila-1
        rcolumna6=columna-2
        if 0 <= rfila6 and 0 <=rcolumna6 :
          #  posiciones[fila-1,columna-1]=1
            posiciones[fila-1,columna-2]=1 
          
           
           # posiciones[fila-1,columna]=1 
          
        #arriba parte izq largo   
        rfila7=fila-2
        rcolumna7=columna-1 
        if 0 <= rfila7 and 0 <=rcolumna7 :
          
            posiciones[fila-2,columna-1]=1 
           # posiciones[fila-2,columna]=1  
            #posiciones[fila-1,columna]=1
            
        
        #arriba parte derecha largo    
        rfila10=fila-2
        rcolumna10=columna+1     
        if rcolumna10<=7  and 0 <=rfila10:
             posiciones[fila-2,columna+1]=1 
             
             
            # posiciones[fila-2,columna]=1
             #posiciones[fila+1,columna]=1
             
             
             
         # arriba parte derecha corto    
        rfila11=fila-1
        rcolumna11=columna+2     
        if rcolumna11<=7  and 0 <=rfila11:
             posiciones[fila-1,columna+2]=1 
             
             
           #  posiciones[fila-1,columna]=1
           #posiciones[fila-1,columna+1]=1
             
    
   
    
    
class Tablero:
    def __init__(self):
        self.reiniciar_tablero()
        
    def reiniciar_tablero(self):
        self.tablero = np.zeros((8,8), dtype=int)
    def __str__(self):
        return str(self.tablero)


tablero=Tablero()
alfil=Alfil()
alfil.obtener_movimientos((5,2),tablero)
print("Alfil")
print(tablero)


tablero.reiniciar_tablero()



torre=Torre()
torre.obtener_movimientos((5,2),tablero)
print("torre")
print(tablero)

tablero.reiniciar_tablero()

dama=Dama()
dama.obtener_movimientos((5,2),tablero)
print("Dama")

print(tablero)
tablero.reiniciar_tablero()

peon=Peon()
peon.obtener_movimientos((5,2),tablero)
print("peon blanco")
print(tablero)

tablero.reiniciar_tablero()


peon=Peon(lado="negro")
peon.obtener_movimientos((5,2),tablero)
print("peon negro")
print(tablero)

tablero.reiniciar_tablero()

rey=Rey()
rey.obtener_movimientos((5,2),tablero)
print("rey")
print(tablero)

tablero.reiniciar_tablero()

caballo=Caballo()
caballo.obtener_movimientos((2,7),tablero)
print("caballo")
print(tablero)
