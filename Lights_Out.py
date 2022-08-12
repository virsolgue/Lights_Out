import random

LETRAS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LUZ_APAGADA=("-")
LUZ_ENCENDIDA=("o")

#PUNTAJES
PUNTAJE_LUCES_APAGADAS=500
PUNTAJE_SIN_MOVIMIENTOS=-300
PUNTAJE_POR_LUZ_ENCENDIDA=-50

#MODO ALEATORIO
DIMENSION_MINIMA_POSIBLE=5
DIMENSION_MAXIMA_POSIBLE=10

#MODO PREDETERMINADO
DIMENSION_TABLERO_PREDETERMINADO=5

TABLERO_NIVEL_1=[LUZ_ENCENDIDA,LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_ENCENDIDA,LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_ENCENDIDA,
LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_ENCENDIDA,LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_ENCENDIDA,
LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_ENCENDIDA]

TABLERO_NIVEL_2=[LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_ENCENDIDA,
LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_ENCENDIDA,
LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_ENCENDIDA]

TABLERO_NIVEL_3=[LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_APAGADA,LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_ENCENDIDA,LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_ENCENDIDA,
LUZ_APAGADA,LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_ENCENDIDA,
LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_ENCENDIDA]

TABLERO_NIVEL_4=[LUZ_ENCENDIDA,LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_APAGADA,LUZ_APAGADA,LUZ_APAGADA,LUZ_APAGADA,
LUZ_ENCENDIDA,LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_APAGADA,LUZ_APAGADA,LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_ENCENDIDA,
LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_APAGADA,LUZ_APAGADA]

TABLERO_NIVEL_5=[LUZ_APAGADA,LUZ_APAGADA,LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_APAGADA,LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_ENCENDIDA,
LUZ_APAGADA,LUZ_APAGADA,LUZ_APAGADA,LUZ_APAGADA,LUZ_APAGADA,LUZ_ENCENDIDA,LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_APAGADA,LUZ_APAGADA,LUZ_ENCENDIDA,
LUZ_ENCENDIDA,LUZ_APAGADA,LUZ_APAGADA,LUZ_APAGADA]

LISTA_NIVELES_PREDETERMINADOS=[TABLERO_NIVEL_1,TABLERO_NIVEL_2,TABLERO_NIVEL_3,TABLERO_NIVEL_4,TABLERO_NIVEL_5]
CANTIDAD_NIVELES=len(LISTA_NIVELES_PREDETERMINADOS)

PREGUNTA_INICIAL="¿Desea comenzar una nueva partida? S / N \n¿Primera vez en LIGHTS OUT? Ingrese A (Ayuda) para aprender a jugar.\n"

def determinar_tablero_segun_nivel(nivel):
	"""Función que dado el nivel, devuelve el tablero correspondiente al mismo."""
	tablero=LISTA_NIVELES_PREDETERMINADOS[nivel-1].copy()
	return tablero
	
def elegir_opcion_del_menu():
	"""Función que imprime por pantalla las opciones que son recibidas por parámetro, de una lista; solicita al usuario que ingrese una opción. 
	Devuele el valor asociado a la opción."""  
	LISTA_MODOS_DE_JUEGO=[("Modo Predeterminado",ejecutar_modo_predeterminado),("Modo Aleatorio",ejecutar_modo_aleatorio)]
	lista_de_opciones=LISTA_MODOS_DE_JUEGO
	numero_de_opcion=0
	separador()
	print("MODALIDADES DE JUEGO")
	for nombre_de_opcion,valor_de_la_opcion in lista_de_opciones:
		numero_de_opcion+=1
		print (str(numero_de_opcion) + " - " + nombre_de_opcion)		
	opcion_elegida=input("Por favor ingrese una opción.\n")
	while not opcion_elegida.isdigit() or int(opcion_elegida)>len(lista_de_opciones) or int(opcion_elegida)<1:
		print ("Opción Inválida. Por favor vuelva a ingresarla.")
		opcion_elegida=input("Por favor ingrese una opción.\n")
	return lista_de_opciones[int(opcion_elegida)-1][1]

def elegir_dimension_del_juego():
	"""Función que le pide al usuario que ingrese un número comprendido entre un máximo y un mínimo. En el caso de que no sea un número o que se 
	encuentre fuera de rango, lo vuelve a solicitar hasta que el mismo sea válido. Devuelve dicho valor como número."""
	opcion_elegida=input("Por favor ingrese la dimensión elegida para el tablero entre " +str(DIMENSION_MINIMA_POSIBLE)+ " y " 
						+str(DIMENSION_MAXIMA_POSIBLE)+ ".\n")
	while not opcion_elegida.isdigit() or int(opcion_elegida)>DIMENSION_MAXIMA_POSIBLE or int(opcion_elegida)<DIMENSION_MINIMA_POSIBLE:
		opcion_elegida=input("Opción inválida. Por favor, vuelva a ingresar una opción entre " +str(DIMENSION_MINIMA_POSIBLE)+ " y " 
						+str(DIMENSION_MAXIMA_POSIBLE)+ ".\n")
	return int(opcion_elegida)
	
def dar_bienvenida():
	"""Imprime por pantalla el nombre del juego."""
	print ("\n  _      _       _     _          ____        _   "                                     
			"\n | |    (_)     | |   | |        / __ \      | |"  
			"\n | |     _  __ _| |__ | |_ ___  | |  | |_   _| |_ " 
			"\n | |    | |/ _` | '_ \| __/ __| | |  | | | | | __|"  
			"\n | |____| | (_| | | | | |_\__ \ | |__| | |_| | |_ "  
			"\n |______|_|\__, |_| |_|\__|___/  \____/ \__,_|\__|"  
			"\n            __/ |                                 "  
			"\n           |___/      ") 			         

def imprimir_nivel_actual(nivel):
	"""Función que recibe por parámetro un número que indica el nivel, y lo imprime por pantalla."""
	separador()
	print ("NIVEL " + str(nivel))
	separador()

def separador():
	"""Imprime un separador de guiones medios"""
	print("--------------------------------------------------------------------------------")
	
def preguntar_si_no_ayuda(mensaje):
	"""Función que en base a un mensaje, le solicita al usuario que ingrese por consola qué desea hacer; devuelve True en caso de que la respuesta
	sea afirmativa, False en caso negativo, y además muestra por pantalla un indicador de ayuda en el caso de que el usuario lo requiera."""
	while True:
		entrada=input(mensaje)
		if entrada.upper()=="A":
			print("")
			reglamentar_juego()
		elif entrada.upper()=="S": 
			return True
		elif entrada.upper()=="N": 
			return False
		else:
			print("Opción inválida. Por favor, vuelva a ingresar una respuesta.") 	
	
def reglamentar_juego():
	"""Muestra por pantalla las reglas del juego Lights Out."""
	print ("\nREGLAS DEL JUEGO"                                     
			"\n -----------------------------------------------------------------------------"  
			"\n El juego Lights Out, se desarrolla sobre un tablero en el que habrán" 
			"\n luces apagadas (representadas por la letra A) y luces encendidas (representadas" 
			"\n por la letra E). Comienza el jugador, ingresando la posición elegida; de"  
			"\n encontrarse una luz encendida, esta se apagará y viceversa. Lo mismo ocurrirá"   
			"\n con las posiciones contiguas, ubicadas en las posiciones verticales y"   
			"\n horizontales a la luz modificada." 
			"\n Se considerará ganador en el caso de que haya logrado apagar la totalidad" 
			"\n de las luces del tablero, logrando pasar de nivel. En el caso de quedarse sin"
			"\n jugadas posibles para realizar o que no haya más niveles, se considera terminada"
			"\n la partida."
			"\n -----------------------------------------------------------------------------")

def solicitar_nombre_jugador():
	"""Se le solicitará a cada uno de los dos jugadores que ingresen su nombre por consola. Para el primer nombre ingresado devuelve la 
	variable nombre_jugador_1 y para el segundo, devolverá la variable nombre_jugador_2.""" 
	nombre_jugador=input("¡Bienvenido Jugador! Por favor, a continuación ingrese su nombre.\n")
	return nombre_jugador
	
def imprimir_tablero_en_juego(tablero,dimension_tablero):	
	"""Recibe la variable tablero (lista de cadenas), e imprime el tablero en pantalla con las luces en juego."""
	separacion_filas= " +----+"+"----+"*(dimension_tablero-2)+"----+"
	fila_tablero=[]
	encabezado=" "
	for i in range (1,dimension_tablero+1):
		if i<10:
			encabezado+="   "+str(i)+" "	
		else:
			encabezado+="  "+str(i)+" " 
	print (encabezado)
	print (separacion_filas)
	for fila in range (1,dimension_tablero+1):
		contenido_fila="|"
		fila_tablero=tablero[dimension_tablero*(fila-1):dimension_tablero*fila]
		for element in range (0,dimension_tablero):
			contenido_fila+="  "+fila_tablero[element]+" |"
		print (LETRAS[fila-1]+contenido_fila)
		print (separacion_filas)
	print("")
	separador()

def mostrar_por_pantalla_estado_de_juego(dimension_tablero,tablero,total_mov_realizados):
	"""Función que recibe por parámetro la dimensión del tablero, el tablero y la cantidad de movimientos realizados, e imprime por pantalla el
	tablero y la cantidad de movimientos restantes."""
	separador()
	imprimir_tablero_en_juego(tablero,dimension_tablero)
	imprimir_movimientos_restantes(dimension_tablero,total_mov_realizados)
	separador()
	
def definir_letras_posibles_segun_dimension_tablero(dimension_tablero):
	"""Define según la dimensión del tablero, cúales son las letras válidas que podrán ser utilizadas por el usuario para indicar una posición. Considerando
	las letras de la A a la Z, la dimensión máxima del tablero será de 26x26."""
	letras_para_filas=LETRAS[:dimension_tablero]
	return letras_para_filas
	
def convertir_fila_de_letra_a_numero(letras_para_filas, letra_de_fila,dimension_tablero):
	"""Recibe la variable letra_de_fila que representa la letra de la fila (en mayúscula) en la que el usuario desea realizar la jugada,y la devuelve 
	convertida al valor numérico correspondiente (número_de_fila). Es decir, para la A corresponderá el número 1, así sucesivamente hasta la Z que se 
	corresponderá con el número 26.""" 
	numero_de_fila=0
	if letra_de_fila not in letras_para_filas:
		return -1
	else:
		for i in range (dimension_tablero):
			if letras_para_filas[i]!=letra_de_fila:
				numero_de_fila+=1
			else:
				break
		return numero_de_fila+1		

def vector_dentro_de_rango(vector,dimension_tablero):
	"""Dado un vector que es recibido por parámetro, determina que la misma sea válida, teniendo en cuenta si que la misma esté dentro de las dimensiones del tablero 
	(y no fuera de rango)."""
	if vector[0]>=1 and vector[1]>=1 and vector[0]<=dimension_tablero and vector[1]<=dimension_tablero:
		return True
	else:
		return False

def posicion_alfa_numerica_dentro_de_rango(posicion,dimension_tablero):
	"""Dada la posición, determina que la misma sea válida, teniendo en cuenta si el usuario ingresó una fila y columna tal y como le fue 
	solicitado, es decir, que la misma esté dentro de las dimensiones del tablero (y no fuera de rango)."""
	numero_de_fila,numero_de_columna=obtener_coordenadas_de_posicion(posicion,dimension_tablero)
	if numero_de_columna.isdigit() and vector_dentro_de_rango((int(numero_de_columna),numero_de_fila),dimension_tablero):
		return True
		
def obtener_coordenadas_de_posicion(posicion,dimension_tablero):
	"""Recibe una variable str del tipo "letra-número", la separa y convierte en los correspondientes valores numéricos para fila y columna; devuelve
	las coordenadas de la posicion por separado como fila y columna."""
	letras_para_filas=definir_letras_posibles_segun_dimension_tablero(dimension_tablero)
	letra_de_fila,numero_de_columna=posicion.split("-")
	letra_de_fila=letra_de_fila.upper()
	numero_de_fila=convertir_fila_de_letra_a_numero(letras_para_filas,letra_de_fila,dimension_tablero)
	return numero_de_fila,numero_de_columna

def solicitar_posicion(dimension_tablero):
	"""Le solicita al usuario que indique por consola cúal es la posición elegida de manera tal que se utilicen letras de la A 
	a la Z para indicar la fila, y números de 1 a 26 para indicar la columna (esto dependerá de la dimensión del tablero), separados por un guión (-), 
	y la devuelve."""
	letras_para_filas=definir_letras_posibles_segun_dimension_tablero(dimension_tablero)
	posicion_elegida=input("Por favor, indique la posición elegida. Recuerde que deberá utilizar una letra \n"+ 
	"de la A a la " + str(LETRAS[(dimension_tablero)-1]) + " para indicar la fila, y un numéro de 1 a " + (str(dimension_tablero)) +
	" para indicar la columna,\n" + "separados por un guión (LETRA-NÚMERO), o bien ingrese (R) para resetear el nivel.\n")	
	return posicion_elegida

def contar_cantidad_de_elementos(caracter,cadena):
	"""Función que dado un caracter y una cadena que son recibidos por parámetro, devuelve las repeticiones de dicho caracter en la misma. """
	repeticiones=0
	for element in cadena:
		if element==caracter:
			repeticiones+=1
	return repeticiones
	
def evaluar_si_dato_esta_dentro_de_opciones(posicion_elegida):
	"""Función que recibe por parámetro un string, lo devuelve en el caso de que contenga un '-', devuelve 0 en el caso de que el mismo sea 'R' (reset)
	o bien devuelve -1 en el caso de que el mismo no esté dentro de las opciones dadas."""
	if posicion_elegida.upper()=="R":
		return 0
	else:
		repeticiones=contar_cantidad_de_elementos("-",posicion_elegida)
		if repeticiones==1:
			letra_de_fila,numero_de_columna=posicion_elegida.split("-")
			if letra_de_fila.upper() in LETRAS and numero_de_columna.isdigit():
				return posicion_elegida
			else:
				return -1
		else:
			return -1	

def calcular_cantidad_luces_apagadas(tablero,dimension_tablero):
	"""Dada la variable que representa las luces en el tablero, se contarán la cantidad de luces apagadas; la 
	cantidad se devolverá en una variable (cantidad_luces_apagadas)."""
	cantidad_luces_apagadas=0
	for i in range (0,dimension_tablero*dimension_tablero):
		if tablero[i]==LUZ_APAGADA:
			cantidad_luces_apagadas+=1
	return cantidad_luces_apagadas

def establecer_estado_de_partida(total_mov_realizados,dimension_tablero,tablero):
	"""Dado los movimientos realizados y la dimensión del tablero que son variables recibidas por parámetro, se determina el estado del juego (si ganó, 
	perdió o ninguna de las dos), devolviendo un string que representa el estado en cada caso e imprimiendo por pantalla si ganó o perdió."""
	luces_apagadas=calcular_cantidad_luces_apagadas(tablero,dimension_tablero)
	if sin_movimientos_posibles(total_mov_realizados,dimension_tablero):
		print ("Se ha queadado sin movimientos disponibles!")
		return "perdio"
	elif  luces_apagadas==dimension_tablero*dimension_tablero:
		print ("Felicitaciones! Ha ganado la partida!")
		return "gano"
	else:
		return "continua jugando"
	
def calcular_puntaje_de_partida_segun_estado_de_partida(total_mov_realizados,dimension_tablero,tablero):
	"""Función que recibe las variasbles total de movimientos, la dimension del tablero y l determina el estado de la partida, y en base a ello 
	calcula y devuelve el puntaje parcial de la misma."""
	puntaje_parcial=0
	estado_de_juego=establecer_estado_de_partida(total_mov_realizados,dimension_tablero,tablero)
	if estado_de_juego=="perdio":
		puntaje_parcial+=PUNTAJE_SIN_MOVIMIENTOS
		return puntaje_parcial
	elif  estado_de_juego=="gano":
		puntaje_parcial+=PUNTAJE_LUCES_APAGADAS
		return puntaje_parcial
	else:
		return puntaje_parcial
	
def reportar_resultado_del_juego(jugador,puntaje_parcial,puntaje_total):
	"""Recibe el nombre del jugador y los puntajes parcial y final. Imprime por pantalla dichos resultados."""
	separador()
	print (jugador+":")
	print("Su puntaje en la última partida es " + str(puntaje_parcial) + " puntos.\n")
	print("Su puntaje total es " + str(puntaje_total) + " puntos.\n")	
	separador()
		
def obtener_numero_de_posicion(numero_de_fila,numero_de_columna,dimension_tablero):
	"""Dado el valor de la fila y de la columna, calcula el número que representa la posición en la lista tablero"""
	numero_de_posicion=((numero_de_fila)-1)*dimension_tablero+((numero_de_columna)-1)
	return numero_de_posicion
		
def generar_tablero_random(dimension_tablero):
	"""Función que dada una dimension recibida por parámetro y una lista de elementos base, genera y devuelve una nueva lista en forma aleatoria, 
	tomandolos de esa lista base."""
	lista_base=[LUZ_APAGADA,LUZ_ENCENDIDA]
	tablero_aleatorio=[]
	for i in range (dimension_tablero*dimension_tablero):
		tablero_aleatorio+=random.choice(lista_base)
	return tablero_aleatorio
	
def sin_movimientos_posibles(total_mov_realizados,dimension_tablero):
	"""Función que recibe un indicador numérico por parámetro, y devuelve True en el caso de que aún hayan movimientos posibles."""
	mov_max_posibles=establecer_movimientos_maximos_posibles(dimension_tablero)
	if total_mov_realizados==mov_max_posibles:
		return True

def establecer_movimientos_maximos_posibles(dimension_tablero):
	"""Función que recibe la dimensión por parámetro y devuelve la correspondiente cantidad máxima de movimientos"""
	return 3*dimension_tablero
	
def imprimir_movimientos_restantes(dimension_tablero,total_mov_realizados):
	"""Función que dada la dimensión del tablero, calcula e imprime la cantidad de movimiemtos restantes."""
	movimientos_restantes=establecer_movimientos_maximos_posibles(dimension_tablero)-total_mov_realizados+1
	print("CANTIDAD DE MOVIMIENTOS RESTANTES:"+str(movimientos_restantes))
	
def modificar_luces_tablero(numero_de_fila,numero_de_columna,tablero,dimension_tablero):
	"""Función que recibe número de fila y columna por parámetro, además del tablero, y modifica el contenido en el mismo de la propia posición, así como el 
	de las posiciones vertical y horizontal contiguas. Si la luz está encendida, la apaga y viceversa. Devuelve el tablero modificado."""
	vector_posicion=(numero_de_fila,numero_de_columna)
	vectores_directores=[(0,0),(0,1),(1,0),(0,-1),(-1,0)]
	for vector in vectores_directores:
		posicion_a_modificar=(vector_posicion[0]+vector[0],vector_posicion[1]+vector[1])
		if vector_dentro_de_rango((posicion_a_modificar[0],posicion_a_modificar[1]),dimension_tablero)==True:
			numero_de_posicion_a_modificar=obtener_numero_de_posicion(posicion_a_modificar[0],posicion_a_modificar[1],dimension_tablero)
			if tablero[numero_de_posicion_a_modificar]==LUZ_ENCENDIDA:
				tablero[numero_de_posicion_a_modificar]=LUZ_APAGADA
			else:
				tablero[numero_de_posicion_a_modificar]=LUZ_ENCENDIDA
		else:
			continue
	return tablero		

def resetear_nivel(tablero_inicial,nivel,puntaje_total,jugador,tablero_modificado,dimension_tablero):
	"""Función que recibe por parámetro el tablero inicial, el tablero modificado la dimensión de los mismos; reemplaza el tablero modificado
	por el tablero inicial, y devuelve el puntaje parcial que deriva del reseteo de la partida."""
	luces_apagadas=calcular_cantidad_luces_apagadas(tablero_modificado,dimension_tablero)
	luces_encendidas=dimension_tablero*dimension_tablero-luces_apagadas
	puntaje_parcial=luces_encendidas*PUNTAJE_POR_LUZ_ENCENDIDA
	puntaje_total+=puntaje_parcial
	total_mov_realizados=1
	reportar_resultado_del_juego(jugador,puntaje_parcial,puntaje_total)
	imprimir_nivel_actual(nivel)
	tablero_modificado=tablero_inicial.copy()
	mostrar_por_pantalla_estado_de_juego(dimension_tablero,tablero_modificado,total_mov_realizados)
	posicion_elegida=ingresar_y_validar_posicion(dimension_tablero)
	return tablero_modificado,posicion_elegida,puntaje_total,total_mov_realizados
	
def ingresar_y_validar_posicion(dimension_tablero):
	"""Función que se encarga de llamar a las funciones que le pedirán al usuario que ingrese su jugada. Se validará el dato ingresado (para esto recibe la
	dimension del tablero por parámetro); devolverá 'reset' en el caso de que quiera resetear el nivel o bien la posicion elegida para realizar la jugada.
	En el caso de que no se ingrese el dato en las condiciones solicitadas, se le volverá a solicitar al usuario que lo ingrese hasta que este lo haga
	correctamente."""
	while True:
		posicion_elegida=solicitar_posicion(dimension_tablero)
		resultado=evaluar_si_dato_esta_dentro_de_opciones(posicion_elegida)
		#SI DESEA RESETEAR NIVEL
		if resultado==0: 
			print ("Se ha reseteado el nivel.")
			return ("reset")
			break
		#SI EL RESULTADO ES DE TIPO INVÁLIDO
		elif resultado==-1:
			print("Usted ha ingresado una posición inválida.")
			continue
		#SI EL RESULTADO ES DEL TIPO VÁLIDO:
		else:
			if not posicion_alfa_numerica_dentro_de_rango(posicion_elegida,dimension_tablero):
				print ("Ha ingresado una posición fuera de rango.")
				continue
			else:
				return posicion_elegida
				break		
				
def establecer_ciclo_de_partida(jugador,dimension_tablero,tablero_inicial,nivel,puntaje_total):
	"""Función que se encarga de controlar el flujo de cada partida. Recibe por parámetro el tablero inicial y el modificado, el nivel y el puntaje 
	total. Devuelve los puntajes parcial y final correspondientes a la partida. """
	total_mov_realizados=0
	mov_max_posibles=establecer_movimientos_maximos_posibles(dimension_tablero)
	tablero=tablero_inicial.copy()
	while establecer_estado_de_partida(total_mov_realizados,dimension_tablero,tablero) not in ("gano","perdio"):
			total_mov_realizados+=1
			mostrar_por_pantalla_estado_de_juego(dimension_tablero,tablero,total_mov_realizados)
			posicion_elegida=ingresar_y_validar_posicion(dimension_tablero)
			while posicion_elegida==("reset"):
				tablero,posicion_elegida,puntaje_total,total_mov_realizados=resetear_nivel(tablero_inicial,nivel,puntaje_total,jugador,tablero,dimension_tablero)
				continue
			numero_de_fila,numero_de_columna=obtener_coordenadas_de_posicion(posicion_elegida,dimension_tablero)
			tablero=modificar_luces_tablero(int(numero_de_fila),int(numero_de_columna),tablero,dimension_tablero)
			if total_mov_realizados==mov_max_posibles:
				imprimir_tablero_en_juego(tablero,dimension_tablero)
				break
	puntaje_parcial=calcular_puntaje_de_partida_segun_estado_de_partida(total_mov_realizados,dimension_tablero,tablero)
	puntaje_total+=puntaje_parcial
	reportar_resultado_del_juego(jugador,puntaje_parcial,puntaje_total)
	return puntaje_total
	
def ejecutar_modo_aleatorio(puntaje_total,jugador):
	"""Función que establece el flujo de la ejecución del juego en modo aleatorio."""
	separador()
	print ("MODO ALEATORIO")
	separador()
	dimension_tablero=elegir_dimension_del_juego()
	puntaje_total=0
	for i in range (1,CANTIDAD_NIVELES+1):
		imprimir_nivel_actual(i)
		tablero_inicial=generar_tablero_random(dimension_tablero)
		puntaje_total=establecer_ciclo_de_partida(jugador,dimension_tablero,tablero_inicial,i,puntaje_total)
	print ("Ha finalizado los " + str(CANTIDAD_NIVELES) + "niveles del modo aleatorio! Su puntaje es:" + str(puntaje_total))
		
def ejecutar_modo_predeterminado(puntaje_total,jugador):
	"""Función que establece el flujo de la ejecución del juego en modo predeterminado."""	
	separador()
	print ("MODO PREDETERMINADO")
	separador()
	dimension_tablero=DIMENSION_TABLERO_PREDETERMINADO
	puntaje_total=0
	for i in range (1,CANTIDAD_NIVELES+1):
		imprimir_nivel_actual(i)
		tablero_inicial=determinar_tablero_segun_nivel(i)
		puntaje_total=establecer_ciclo_de_partida(jugador,dimension_tablero,tablero_inicial,i,puntaje_total)
	print ("Ha finalizado los "+ str(CANTIDAD_NIVELES) + "niveles del modo predeterminado! Su puntaje es:" + str(puntaje_total))
		
def main():
	"""Se encargará de orquestar las funciones de manera tal que el juego 'Lights Out' pueda desarrollarse."""
	dar_bienvenida()
	while preguntar_si_no_ayuda(PREGUNTA_INICIAL)==True:
		jugador=solicitar_nombre_jugador()
		puntaje_total=0
		elegir_opcion_del_menu()(puntaje_total,jugador)
	
main()			
		