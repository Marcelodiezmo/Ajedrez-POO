# Ajedrez-POO

movimientos de ficha de ajedrez
 permite simular los movimientos de todas las piezas de ajedrez dada una posición aleatoria dentro del tablero.
 
 en este script hay una clase "padre" llamado Pieza, y hay clases "hijos" que representa todos las las fichas del ajedrez (torre,peon,dama,rey,alfil y caballo) cada ficha tiene su logica de movimiento en el tablero , ademas de esto, tenemos una clase llamada "dama", esta clase hereda las funciones que tengan la torre y el alfil, ya que la dama, puede moverse con la combinacion de ellos .
 finalmente hay una clase llamada "tablero" su funcion es crear el tablero del ajedrez (8x8) y poder reiniciarlo cada vez que se desea mostrar los movimientos de las fichas correspondientes.

#### Ejemplos :
* si se quiere mostrar los posibles movimientos de una ficha de ajedrez dada se hace lo siguiente:

tablero=Tablero()\
alfil=Alfil()\
alfil.obtener_movimientos((5,2),tablero)\
print(tablero)

el resultado saldrá el siguiente:

Alfil\
[0 0 0 0 0 0 0 1]\
  [0 0 0 0 0 0 1 0]\
   [0 0 0 0 0 1 0 0]\
   [1 0 0 0 1 0 0 0]\
   [0 1 0 1 0 0 0 0]\
   [0 0 8 0 0 0 0 0]\
   [0 1 0 1 0 0 0 0]\
   [1 0 0 0 1 0 0 0]

en donde se (5,2) pertenece  a la posicion  que se quiera posicionar el alfil, el "5" pertenece a las filas y el "2"  a las columnas.
luego de la posicion dada,se debe instanciar un objeto de la clase tablero para poder plasmar los resultados.

* en la clase peon se tuvo que tener en cuenta que color pertenece el peon, ya que cada color va a diferente lado, Ademas de esto hay posiciones en especifico que puede avanzar 2 casillas en vez de una.

en el caso de que no se defina el color que se quiere , quedara de color blanco por defecto

peon=Peon()\
peon.obtener_movimientos((5,2),tablero)\
print("peon blanco")\
print(tablero)\

Peon blanco\

 [0 0 0 0 0 0 0 0]\
 [0 0 0 0 0 0 0 0]\
 [0 0 0 0 0 0 0 0]\
 [0 0 0 0 0 0 0 0]\
 [0 0 1 0 0 0 0 0]\
 [0 0 8 0 0 0 0 0]\
 [0 0 0 0 0 0 0 0]\
 [0 0 0 0 0 0 0 0]

peon=Peon(lado="negro")\
peon.obtener_movimientos((5,2),tablero)\
print("peon negro")\
print(tablero)
 
peon negro

 [0 0 0 0 0 0 0 0]\
 [0 0 0 0 0 0 0 0]\
 [0 0 0 0 0 0 0 0]\
 [0 0 0 0 0 0 0 0]\
 [0 0 0 0 0 0 0 0]\
 [0 0 8 0 0 0 0 0]\
 [0 0 1 0 0 0 0 0]\
 [0 0 0 0 0 0 0 0]
 
 * dado la posicion (2,2), se puede observar como el peon blanco puede avanzar una casilla, mientras que el peon negro puede avanzar 2 casillas.
 
 peon blanco\
[[0 1 0 0 0 0 0 0]\
 [0 8 0 0 0 0 0 0]\
 [0 0 0 0 0 0 0 0]\
 [0 0 0 0 0 0 0 0]\
 [0 0 0 0 0 0 0 0]\
 [0 0 0 0 0 0 0 0]\
 [0 0 0 0 0 0 0 0]\
 [0 0 0 0 0 0 0 0]]
 
peon negro

[0 0 0 0 0 0 0 0]\
 [0 8 0 0 0 0 0 0]\
 [0 1 0 0 0 0 0 0]\
 [0 1 0 0 0 0 0 0]\
 [0 0 0 0 0 0 0 0]\
 [0 0 0 0 0 0 0 0]\
 [0 0 0 0 0 0 0 0]\
 [0 0 0 0 0 0 0 0]
