# -*- coding: utf-8 -*-
import numpy as np

import main.python.parametrizacion.ParametrosTablero as const

'''
Clase controladora del tablero de juego, almacena la información de la 
situación actual del tablero en la que permite realizar acciones
'''
class ControladorTablero:
    '''
    Metodo constructor de la clase ControladorTablero, se definen e inicializan 
    todos los atributos privados de la misma
    '''
    def __init__(self):
        '''Atributo tablero: guarda una matriz con el estado actual del tablero'''
        self.__tablero = np.zeros((const.NFILA,const.NCOLUMNA), dtype=int)
        '''Atributo mazoArmas: garda un array con las cartas que quedan en el 
        mazo de robo'''
        self.__mazoArmas = []
        
        self.__initMazo()
        
    '''
    Metodo que inicializa el mazo de las cartas con todas las cartas de armas 
    disponibles
    '''
    def __initMazo(self):
        self.__mazoArmas = [1,1,2,2,3,3,4,4,4,5,5,5,6,6,6,6,7,7,7,7,7]
        
    '''
    Metodo que se encarga de borrar del tablero las acciones realizadas por 
    ambos jugadores
    '''
    def __borrarAcciones(self):
        self.__tablero[const.ACCIONES_USADAS_JUGADOR1] = np.zeros(const.NCOLUMNA, dtype=int)
        self.__tablero[const.ACCIONES_USADAS_JUGADOR2] = np.zeros(const.NCOLUMNA, dtype=int)
        
    '''
    Metodo que se encarga de borrar del tablero las armas usadas por 
    ambos jugadores
    '''
    def __borrarArmas(self):
        self.__tablero[const.ARMAS_USADAS_JUGADOR1] = np.zeros(const.NCOLUMNA, dtype=int)
        self.__tablero[const.ARMAS_USADAS_JUGADOR2] = np.zeros(const.NCOLUMNA, dtype=int)
        
    '''
    Metodo que limina del mazo de cartas una carta random y la devuelve en el 
    return. Lanza una exception si el mazo no tiene cartas que robar
    '''
    def __robarCarta(self):
        if(len(self.__mazoArmas) < 1):
            raise Exception("Mazo vacio")
        return self.__mazoArmas.pop(np.random.randint(len(self.__mazoArmas)))
        
    '''
    Metodo que se encarga de repartir 6 cartas del mazo a cada jugador y 
    ordenar las manos de dichos jugadores
    '''
    def __repartoDeCartas(self):
        for _ in range(const.N_CARTAS_INICIAL):
            self.__conseguirCarta(const.MANO_JUGADOR1)
            self.__conseguirCarta(const.MANO_JUGADOR2)
        self.__ordenarMano(const.MANO_JUGADOR1)
        self.__ordenarMano(const.MANO_JUGADOR2)
        
    '''
    Metodo que asigna una carta del mazo a la mano del jugador con el numero 
    dado por parametro
    '''
    def __conseguirCarta(self, jugadorIndex):
        manoList = self.__tablero[jugadorIndex]
        cartaNula = 0
        #Eliminamos un hueco sin usar
        manoList = self.__eliminarCarta(manoList, cartaNula)
        cartaValue = self.__robarCarta()
        manoList = np.append(manoList, cartaValue)
        self.__tablero[jugadorIndex] = manoList
        
    '''
    Metodo que recibe el array de la mano y el valor de la carta que sustituye 
    por 0
    '''
    def __soltarCarta(self, manoList, cartaValue):
        manoList = self.__eliminarCarta(manoList, cartaValue)
        cartaNula = 0
        manoList = np.append(manoList, cartaNula)
        return manoList
        
    '''
    Metodo que recibe un array y un valor, devuelve el array eliminando el 
    valor 1 vez
    '''
    def __eliminarCarta(self, lista, valor):
        return np.delete(lista, np.argwhere(lista == valor)[0])
        
    '''
    Metodo que recibe el indice del jugador y devuelve el indice de sus 
    acciones usadas
    '''
    def __getFilaAcciones(self, jugadorIndex):
        filaAccionesIndex = const.ACCIONES_USADAS_JUGADOR1
        if(jugadorIndex == const.JUGADOR2):
            filaAccionesIndex = const.ACCIONES_USADAS_JUGADOR2
        return filaAccionesIndex
        
    '''
    Metodo que recibe el indice del jugador y devuelve el indice de su mano
    '''
    def __getMano(self, jugadorIndex):
        manoIndex = const.MANO_JUGADOR1
        if(jugadorIndex == const.JUGADOR2):
            manoIndex = const.MANO_JUGADOR2
        return manoIndex
        
    '''
    Metodo que recibe el indice de la mano del jugador y ordena su mano
    '''
    def __ordenarMano(self, manoIndex):
        manoList = self.__tablero[manoIndex]
        manoList = np.sort(manoList)
        self.__tablero[manoIndex] = manoList
        
    '''
    Metodo que devuelve el numero de cartas que contiene el array que se le
    pasa por parametro, sin incluir la primera posicion que corresponde al 
    tipo de accion. Ademas lanza una excepcion si las cartas no estan bien 
    ordenadas en el array y contiene ceros en medio
    '''
    def __getNumeroCartasEnAccionSeleccionada(self, accionArray):
        num = 0
        encontrado0 = False
        for i in range(len(accionArray)):
            if(i == const.ACCION_REALIZADA):
                continue
            elif (encontrado0 != True and accionArray[i] != 0):
                num = num + 1
            elif (encontrado0 != True and accionArray[i] == 0):
                encontrado0 = True
            elif (encontrado0 and accionArray[i] == 0):
                continue
            else:
                raise Exception("Accion mal formada")
        return num
        
    '''
    Metodo que lanza una excepcion si el numero de cartas no concuerda con el 
    tipo de accion 1 o si esta accion ya ha sido usada
    '''
    def __comprobarAccion1(self, filaAcciones, numCartasEnAccion):
        if(numCartasEnAccion != const.ACCION_1_COUNT):
            raise Exception("Accion mal formada, esperadas "+str(const.ACCION_1_COUNT)+" cartas, recibidas: "+str(numCartasEnAccion))
        elif(self.__tablero[filaAcciones][const.TIPO_SECRETO] != 0):
            raise Exception("Accion 1 ya usada")
        
    '''
    Metodo que lanza una excepcion si el numero de cartas no concuerda con el 
    tipo de accion 2 o si esta accion ya ha sido usada
    '''
    def __comprobarAccion2(self, filaAcciones, numCartasEnAccion):
        if(numCartasEnAccion != const.ACCION_2_COUNT):
            raise Exception("Accion mal formada, esperadas "+str(const.ACCION_2_COUNT)+" cartas, recibidas: "+str(numCartasEnAccion))
        elif(self.__tablero[filaAcciones][const.TIPO_RENUNCIA_1] != 0 
           or self.__tablero[filaAcciones][const.TIPO_RENUNCIA_2] != 0):
            raise Exception("Accion 2 ya usada")
        
    '''
    Metodo que lanza una excepcion si el numero de cartas no concuerda con el 
    tipo de accion 3 o si esta accion ya ha sido usada
    '''
    def __comprobarAccion3(self, filaAcciones, numCartasEnAccion):
        if(numCartasEnAccion != const.ACCION_3_COUNT):
            raise Exception("Accion mal formada, esperadas "+str(const.ACCION_3_COUNT)+" cartas, recibidas: "+str(numCartasEnAccion))
        elif(self.__tablero[filaAcciones][const.TIPO_REGALO] != 0):
            raise Exception("Accion 3 ya usada")
        
    '''
    Metodo que lanza una excepcion si el numero de cartas no concuerda con el 
    tipo de accion 4 o si esta accion ya ha sido usada
    '''
    def __comprobarAccion4(self, filaAcciones, numCartasEnAccion):
        if(numCartasEnAccion != const.ACCION_4_COUNT):
            raise Exception("Accion mal formada, esperadas "+str(const.ACCION_4_COUNT)+" cartas, recibidas: "+str(numCartasEnAccion))
        elif(self.__tablero[filaAcciones][const.TIPO_COMPETICION] != 0):
            raise Exception("Accion 4 ya usada")
        
    '''
    Metodo que lanza una excepcion si el numero de cartas no concuerda con el 
    tipo de accion de decision 3 o si esta accion no concuerda con la esperada
    '''
    def __comprobarAccionDecision3(self, numCartasEnAccion):
        if(numCartasEnAccion != const.PENDIENTE_5_ELEGIDA_COUNT):
            raise Exception("Accion mal formada, esperadas "+str(const.PENDIENTE_5_ELEGIDA_COUNT)+" cartas, recibidas: "+str(numCartasEnAccion))
        elif(self.__tablero[const.ACCION_PENDIENTE][const.TIPO_SECRETO] != const.TIPO_DECISION_REGALO):
            raise Exception("Accion de decision 3 no disponible")
        
    '''
    Metodo que lanza una excepcion si el numero de cartas no concuerda con el 
    tipo de accion de decision 4 o si esta accion no concuerda con la esperada
    '''
    def __comprobarAccionDecision4(self, numCartasEnAccion):
        if(numCartasEnAccion != const.PENDIENTE_6_ELEGIDA_COUNT):
            raise Exception("Accion mal formada, esperadas "+str(const.PENDIENTE_6_ELEGIDA_COUNT)+" cartas, recibidas: "+str(numCartasEnAccion))
        elif(self.__tablero[const.ACCION_PENDIENTE][const.TIPO_SECRETO] != const.TIPO_DECISION_COMPETICION):
            raise Exception("Accion de decision 4 no disponible")
        
    '''
    Metodo que guarda la carta seleccionada del array dado por parametro para 
    la accion 1 en la fila de acciones del tablero dada por parametro y elimina
    esa carta de la mano dada por parametro 
    '''
    def __guardarAccion1(self, manoIndex, filaAccionesIndex, accionArray):
        carta1 = accionArray[const.ACCION_1]
        self.__tablero[filaAccionesIndex][const.TIPO_SECRETO] = carta1
        manoList = self.__tablero[manoIndex]
        manoList = self.__soltarCarta(manoList, carta1)
        self.__tablero[manoIndex] = manoList
        
    '''
    Metodo que guarda las cartas seleccionadas del array dado por parametro 
    para la accion 2 en la fila de acciones del tablero dada por parametro y 
    elimina esas cartas de la mano dada por parametro 
    '''
    def __guardarAccion2(self, manoIndex, filaAccionesIndex, accionArray):
        carta1 = accionArray[const.ACCION_2_1]
        carta2 = accionArray[const.ACCION_2_2]
        
        if(carta1 > carta2):
            carta1,carta2 = carta2,carta1
        
        self.__tablero[filaAccionesIndex][const.TIPO_RENUNCIA_1] = carta1
        self.__tablero[filaAccionesIndex][const.TIPO_RENUNCIA_2] = carta2
        manoList = self.__tablero[manoIndex]
        manoList = self.__soltarCarta(manoList, carta1)
        manoList = self.__soltarCarta(manoList, carta2)
        self.__tablero[manoIndex] = manoList
        
    '''
    Metodo que guarda las cartas seleccionadas del array dado por parametro 
    para la accion 3 en la fila de accion pendiente, establece la accion 3 
    como usada en la fila de acciones del tablero dada por parametro y 
    elimina esas cartas de la mano dada por parametro 
    '''
    def __guardarAccion3(self, manoIndex, filaAccionesIndex, accionArray):
        #Obtencion de las cartas
        carta1 = accionArray[const.ACCION_3_1]
        carta2 = accionArray[const.ACCION_3_2]
        carta3 = accionArray[const.ACCION_3_3]
        
        #Actualizacion de el flag de la accion 3
        self.__tablero[filaAccionesIndex][const.TIPO_REGALO] = 1
        
        #Preparar accion pendiente
        decisionList = self.__tablero[const.ACCION_PENDIENTE]
        cartasList = np.array([carta1, carta2, carta3])
        cartasListOrdenada = np.sort(cartasList)
        decisionList[const.PENDIENTE_5_1] = cartasListOrdenada[0]
        decisionList[const.PENDIENTE_5_2] = cartasListOrdenada[1]
        decisionList[const.PENDIENTE_5_3] = cartasListOrdenada[2]
        decisionList[const.PENDIENTE_TIPO] = const.TIPO_DECISION_REGALO
        
        #Eliminar cartas de la mano
        manoList = self.__tablero[manoIndex]
        manoList = self.__soltarCarta(manoList, carta1)
        manoList = self.__soltarCarta(manoList, carta2)
        manoList = self.__soltarCarta(manoList, carta3)
        self.__tablero[manoIndex] = manoList
        
    '''
    Metodo que guarda las cartas seleccionadas del array dado por parametro 
    para la accion 4 en la fila de accion pendiente, establece la accion 4 
    como usada en la fila de acciones del tablero dada por parametro y 
    elimina esas cartas de la mano dada por parametro 
    '''
    def __guardarAccion4(self, manoIndex, filaAccionesIndex, accionArray):
        #Obtencion de las cartas
        carta1 = accionArray[const.ACCION_4_1_1]
        carta2 = accionArray[const.ACCION_4_1_2]
        carta3 = accionArray[const.ACCION_4_2_1]
        carta4 = accionArray[const.ACCION_4_2_2]
        
        #Actualizacion de el flag de la accion 4
        self.__tablero[filaAccionesIndex][const.TIPO_COMPETICION] = 1
        
        #Preparar accion pendiente
        decisionList = self.__tablero[const.ACCION_PENDIENTE]
        cartasList = np.array([carta1, carta2, carta3, carta4])
        decisionList[const.PENDIENTE_6_1_1] = cartasList[0]
        decisionList[const.PENDIENTE_6_1_2] = cartasList[1]
        decisionList[const.PENDIENTE_6_2_1] = cartasList[2]
        decisionList[const.PENDIENTE_6_2_2] = cartasList[3]
        decisionList[const.PENDIENTE_TIPO] = const.TIPO_DECISION_COMPETICION
        
        #Eliminar cartas de la mano
        manoList = self.__tablero[manoIndex]
        manoList = self.__soltarCarta(manoList, carta1)
        manoList = self.__soltarCarta(manoList, carta2)
        manoList = self.__soltarCarta(manoList, carta3)
        manoList = self.__soltarCarta(manoList, carta4)
        self.__tablero[manoIndex] = manoList
        
    '''
    Metodo que guarda las cartas seleccionadas del array dado por parametro 
    para la accion de decision 3 en la fila de accion pendiente, sumamos las 
    cartas seleccionadas a los jugadores en las filas de armas usadas y deja 
    la fila de accion pendiente vacia
    '''
    def __guardarAccionDecision3(self, jugadorIndex, accionArray):

        #Obtenemos el index de las armas del jugador y del adversario
        armasJugadorIndex = const.ARMAS_USADAS_JUGADOR1
        armasAdversarioIndex = const.ARMAS_USADAS_JUGADOR2
        if(jugadorIndex == const.JUGADOR2):
            armasJugadorIndex = const.ARMAS_USADAS_JUGADOR2
            armasAdversarioIndex = const.ARMAS_USADAS_JUGADOR1
        
        #Obtenemos un array con las cartas
        accionPendienteList = self.__tablero[const.ACCION_PENDIENTE]
        cartasList = np.array([accionPendienteList[const.PENDIENTE_5_1],
                              accionPendienteList[const.PENDIENTE_5_2],
                              accionPendienteList[const.PENDIENTE_5_3]])
        
        #Eliminamos la carta obtenida del array y se la añadimos al jugador
        cartaElegida = accionArray[const.PENDIENTE_5_ELEGIDA]
        cartasList = self.__eliminarCarta(cartasList, cartaElegida)
        self.__sumarCarta(armasJugadorIndex, cartaElegida)
        
        #Añadimos al adversario sus cartas
        self.__sumarCarta(armasAdversarioIndex, cartasList[0])
        self.__sumarCarta(armasAdversarioIndex, cartasList[1])
        
        #Reseteamos la accion de seleccion
        self.__tablero[const.ACCION_PENDIENTE] = np.zeros(const.NCOLUMNA, dtype=int)
        
    '''
    Metodo que guarda las cartas seleccionadas del array dado por parametro 
    para la accion de decision 4 en la fila de accion pendiente, sumamos las 
    cartas seleccionadas a los jugadores en las filas de armas usadas y deja 
    la fila de accion pendiente vacia
    '''
    def __guardarAccionDecision4(self, jugadorIndex, accionArray):
        #Obtenemos el index de las armas del jugador y del adversario
        armasJugadorIndex = const.ARMAS_USADAS_JUGADOR1
        armasAdversarioIndex = const.ARMAS_USADAS_JUGADOR2
        if(jugadorIndex == const.JUGADOR2):
            armasJugadorIndex = const.ARMAS_USADAS_JUGADOR2
            armasAdversarioIndex = const.ARMAS_USADAS_JUGADOR1
        
        #Obtenemos un array con las cartas
        accionPendienteList = self.__tablero[const.ACCION_PENDIENTE]
        cartasList1 = np.array([accionPendienteList[const.PENDIENTE_6_1_1],
                              accionPendienteList[const.PENDIENTE_6_1_2]])
        cartasList2 = np.array([accionPendienteList[const.PENDIENTE_6_2_1],
                              accionPendienteList[const.PENDIENTE_6_2_2]])
        
        #Eliminamos la carta obtenida del array y se la añadimos al jugador
        cartasElegidas = np.array([accionPendienteList[const.PENDIENTE_6_ELEGIDA_1],
                              accionPendienteList[const.PENDIENTE_6_ELEGIDA_2]])
    
        #Dependiendo de que cartas se hayan elegido se dan a un jugador o a otro
        comparison1 = cartasList1 == cartasElegidas
        
        if(comparison1.all()):
            self.__sumarCarta(armasJugadorIndex, cartasList1[0])
            self.__sumarCarta(armasJugadorIndex, cartasList1[1])
            self.__sumarCarta(armasAdversarioIndex, cartasList2[0])
            self.__sumarCarta(armasAdversarioIndex, cartasList2[1])
            
        else:
            self.__sumarCarta(armasJugadorIndex, cartasList2[0])
            self.__sumarCarta(armasJugadorIndex, cartasList2[1])
            self.__sumarCarta(armasAdversarioIndex, cartasList1[0])
            self.__sumarCarta(armasAdversarioIndex, cartasList1[1])
            
        #Reseteamos la accion de seleccion
        self.__tablero[const.ACCION_PENDIENTE] = np.zeros(const.NCOLUMNA, dtype=int)
        
    '''
    Metodo que toma el valor de la carta de secreto de la fila del jugador 
    seleccionada y la guarda en la fila de armas del jugador seleccionada
    '''
    def __guardarSecreto(self, accionesJugadorIndex, filaArmasIndex):
        carta = self.__tablero[accionesJugadorIndex][const.TIPO_SECRETO]
        self.__sumarCarta(filaArmasIndex, carta)
        
    '''
    Metodo que dada una carta suma 1 al la columna correspondiente a esa 
    carta y a la fila dada
    '''
    def __sumarCarta(self, filaArmasIndex, carta):
        self.__tablero[filaArmasIndex][carta-1] = self.__tablero[filaArmasIndex][carta-1]+1
        
    '''
    Metodo que calcula todos los puntos de cada jugador y devuelve el ganador
    '''
    def __getGanador(self):
        puntosGuerreras = [2, 2, 2, 3, 3, 4, 5]
        puntosJugador1 = 0
        puntosJugador2 = 0
        favorJugador1 = 0
        favorJugador2 = 0
        
        for i in range(const.NCOLUMNA):
            if(self.__tablero[const.FAVOR_DE_GUERRERA][i] == const.FAVOR_JUGADOR_1):
                puntosJugador1 = puntosJugador1 + puntosGuerreras[i]
                favorJugador1 = favorJugador1 + 1
            elif(self.__tablero[const.FAVOR_DE_GUERRERA][i] == const.FAVOR_JUGADOR_2):
                puntosJugador2 = puntosJugador2 + puntosGuerreras[i]
                favorJugador2 = favorJugador2 + 1
            
        if(puntosJugador1 >= 11):
            return const.GANADOR_1_POR_11_PUNTOS
        elif (puntosJugador2 >= 11):
            return const.GANADOR_2_POR_11_PUNTOS
        elif (favorJugador1 >= 4):
            return const.GANADOR_1_POR_4_FAVORES
        elif (favorJugador2 >= 4):
            return const.GANADOR_2_POR_4_FAVORES
        else:
            return const.GANADOR_EMPATE
        
    '''
    Metodo que comprueba el numero de cartas en la mano dada y devuelve y esta 
    llena o no
    '''
    def __manoLlena(self, filaMano):
        n = 0
        for i in range(0, const.NCOLUMNA, 1):
            carta = filaMano[i]
            if (carta != 0):
                n = n + 1
        return n==const.NCOLUMNA
        
    '''
    Metodo que inicializa el mazo con todas las cartas menos una y reparte 
    las cartas iniciales
    '''
    def initRonda(self):
        self.__initMazo()
        self.__robarCarta()
        self.__repartoDeCartas()
        self.__borrarAcciones()
        self.__borrarArmas()
        
    '''
    Metodo que, dado el indice del jugador, roba una carta del mazo de cartas
    y la guarda en la mano de dicho jugador
    '''
    def jugadorRobaCarta(self, jugadorIndex):
        manoIndex = self.__getMano(jugadorIndex)
        if(self.__manoLlena(self.__tablero[manoIndex])):
            raise Exception("El jugador no puede robar mas cartas")
        self.__conseguirCarta(manoIndex)
        self.__ordenarMano(manoIndex)
        
    '''
    Metodo que, dado el indice del jugador, devuelve una matriz de informacion 
    parcial para ese jugador
    '''
    def getVistaTablero(self, jugadorIndex):
        if(jugadorIndex != const.JUGADOR1 and jugadorIndex != const.JUGADOR2):
            raise Exception("Jugador no existente")
        
        tableroParcial = np.zeros((const.NFILA,const.NCOLUMNA), dtype=int)
        
        """MANO"""
        manoIndex = self.__getMano(jugadorIndex)
        tableroParcial[const.MANO_JUGADOR1] = self.__tablero[manoIndex].copy()

        """ACCIONES"""
        accionesJugador = const.ACCIONES_USADAS_JUGADOR1
        accionesAdversario = const.ACCIONES_USADAS_JUGADOR2
        if(jugadorIndex == const.JUGADOR2):
            accionesJugador = const.ACCIONES_USADAS_JUGADOR2
            accionesAdversario = const.ACCIONES_USADAS_JUGADOR1
        
        tableroParcial[const.ACCIONES_USADAS_JUGADOR1] = self.__tablero[accionesJugador].copy()

        accionesVistas = self.__tablero[accionesAdversario].copy()
        accionesOcultas = np.zeros(const.NCOLUMNA, dtype=int)
        for i in range(const.NCOLUMNA):
            if(accionesVistas[i] != 0):
                accionesOcultas[i] = 1
            
        tableroParcial[const.ACCIONES_USADAS_JUGADOR2] =  accionesOcultas
        
        """ARMAS USADAS"""
        armasJugador = const.ARMAS_USADAS_JUGADOR1
        armasAdversario = const.ARMAS_USADAS_JUGADOR2
        if(jugadorIndex == const.JUGADOR2):
            armasJugador = const.ARMAS_USADAS_JUGADOR2
            armasAdversario = const.ARMAS_USADAS_JUGADOR1
        
        tableroParcial[const.ARMAS_USADAS_JUGADOR1] = self.__tablero[armasJugador].copy()
        tableroParcial[const.ARMAS_USADAS_JUGADOR2] = self.__tablero[armasAdversario].copy()
        
        tableroParcial[const.FAVOR_DE_GUERRERA] = self.__tablero[const.FAVOR_DE_GUERRERA].copy()
        tableroParcial[const.ACCION_PENDIENTE] = self.__tablero[const.ACCION_PENDIENTE].copy()
        
        return tableroParcial.copy()
        
    '''
    Metodo que, dado el indice del jugador y una accion, comprueba que ese 
    jugador puede realizar la accion, que esta está bien formada y de ser asi 
    la ejecuta haciendo los cambios correspondientes en el tablero
    '''
    def realizarAccion(self, jugadorIndex, accionArray):
        if(jugadorIndex != const.JUGADOR1 and jugadorIndex != const.JUGADOR2):
            raise Exception("Jugador no existente")
            
        filaAcciones = self.__getFilaAcciones(jugadorIndex)
        manoIndex = self.__getMano(jugadorIndex)
        numCartasEnAccion = self.__getNumeroCartasEnAccionSeleccionada(accionArray)
        
        if(accionArray[const.ACCION_REALIZADA] == const.TIPO_SECRETO):
            self.__comprobarAccion1(filaAcciones, numCartasEnAccion)
            self.__guardarAccion1(manoIndex, filaAcciones, accionArray)
            
        elif (accionArray[const.ACCION_REALIZADA] == const.TIPO_RENUNCIA): 
            self.__comprobarAccion2(filaAcciones, numCartasEnAccion)
            self.__guardarAccion2(manoIndex, filaAcciones, accionArray)
            
        elif (accionArray[const.ACCION_REALIZADA] == const.TIPO_REGALO): 
            self.__comprobarAccion3(filaAcciones, numCartasEnAccion)
            self.__guardarAccion3(manoIndex, filaAcciones, accionArray)
            
        elif (accionArray[const.ACCION_REALIZADA] == const.TIPO_COMPETICION): 
            self.__comprobarAccion4(filaAcciones, numCartasEnAccion)
            self.__guardarAccion4(manoIndex, filaAcciones, accionArray)
            
        elif (accionArray[const.ACCION_REALIZADA] == const.TIPO_DECISION_REGALO): 
            self.__comprobarAccionDecision3(numCartasEnAccion)
            self.__guardarAccionDecision3(jugadorIndex, accionArray)
            
        elif (accionArray[const.ACCION_REALIZADA] == const.TIPO_DECISION_COMPETICION): 
            self.__comprobarAccionDecision4(numCartasEnAccion)
            self.__guardarAccionDecision4(jugadorIndex, accionArray)
            
        else:
            raise Exception("Accion no encontrada")
        
    '''
    Metodo que, dado el indice del jugador y una accion, comprueba que ese 
    jugador puede realizar la accion, que esta está bien formada y de ser asi 
    la ejecuta haciendo los cambios correspondientes en el tablero
    '''
    def hayAccionPendiente(self):
        pendiente = self.__tablero[const.ACCION_PENDIENTE][const.PENDIENTE_TIPO]
        return pendiente != 0
        
    '''
    Metodo que realiza todas las acciones necesarias para dar el turno por 
    terminado y devuelve el jugador ganador en caso de que lo hubiera
    '''
    def finalizarTurno(self):
        self.__guardarSecreto(const.ACCIONES_USADAS_JUGADOR1, const.ARMAS_USADAS_JUGADOR1)
        self.__guardarSecreto(const.ACCIONES_USADAS_JUGADOR2, const.ARMAS_USADAS_JUGADOR2)
        
        for i in range(const.NCOLUMNA):
            armas1 = self.__tablero[const.ARMAS_USADAS_JUGADOR1][i]
            armas2 = self.__tablero[const.ARMAS_USADAS_JUGADOR2][i]
            
            if(armas1 > armas2):
                self.__tablero[const.FAVOR_DE_GUERRERA][i] = const.FAVOR_JUGADOR_1
            elif(armas2 > armas1):
                self.__tablero[const.FAVOR_DE_GUERRERA][i] = const.FAVOR_JUGADOR_2
                
        return self.__getGanador()
    
