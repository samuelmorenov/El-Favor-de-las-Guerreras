# -*- coding: utf-8 -*-

import numpy as np

import controller.Constantes as const


class Controller:
    def __init__(self):
        self.__tablero = np.zeros((const.NFILA,const.NCOLUMNA), dtype=int)
        self.__initMazo()
        
    def __initMazo(self):
        self.__mazoArmas = [1,1,2,2,3,3,4,4,4,5,5,5,6,6,6,6,7,7,7,7,7]
        
    def __borrarAcciones(self):
        self.__tablero[const.ACCIONES_USADAS_JUGADOR1] = np.zeros(const.NCOLUMNA, dtype=int)
        self.__tablero[const.ACCIONES_USADAS_JUGADOR2] = np.zeros(const.NCOLUMNA, dtype=int)
        
    def __borrarArmas(self):
        self.__tablero[const.ARMAS_USADAS_JUGADOR1] = np.zeros(const.NCOLUMNA, dtype=int)
        self.__tablero[const.ARMAS_USADAS_JUGADOR2] = np.zeros(const.NCOLUMNA, dtype=int)
        
    #Elimina del mazo de cartas una carta random y la devuelve en el return
    def __robarCarta(self):
        if(len(self.__mazoArmas) < 1):
            raise Exception("Mazo vacio")
        return self.__mazoArmas.pop(np.random.randint(len(self.__mazoArmas)))
        
    #Se reparten 6 cartas del mazo a cada jugador y ordena las manos
    def __repartoDeCartas(self):
        for i in range(const.N_CARTAS_INICIAL):
            self.__conseguirCarta(const.MANO_JUGADOR1)
            self.__conseguirCarta(const.MANO_JUGADOR2)
        self.__ordenarMano(const.MANO_JUGADOR1)
        self.__ordenarMano(const.MANO_JUGADOR2)
            
    #Se le asigna una carta del mazo a la mano del jugador
    def __conseguirCarta(self, jugadorIndex):
        manoList = self.__tablero[jugadorIndex]
        cartaNula = 0
        manoList = self.__eliminarCarta(manoList, cartaNula) #Eliminamos un hueco sin usar
        cartaValue = self.__robarCarta()
        manoList = np.append(manoList, cartaValue)
        self.__tablero[jugadorIndex] = manoList
        
    #Se le pasa el array de la mano y el valor de la carta que sustituye por 0
    def __soltarCarta(self, manoList, cartaValue):
        manoList = self.__eliminarCarta(manoList, cartaValue)
        cartaNula = 0
        manoList = np.append(manoList, cartaNula)
        return manoList
        
    #Se le pasa el array y el valor, devuelve el array eliminando el valor 1 vez
    def __eliminarCarta(self, lista, valor):
        return np.delete(lista, np.argwhere(lista == valor)[0])
    
    #Se le pasa el indice del jugador y te devuelve el indice de sus acciones usadas
    def __getFilaAcciones(self, jugadorIndex):
        filaAccionesIndex = const.ACCIONES_USADAS_JUGADOR1
        if(jugadorIndex == const.JUGADOR2):
            filaAccionesIndex = const.ACCIONES_USADAS_JUGADOR2
        return filaAccionesIndex
    
    #Se le pasa el indice del jugador y te devuelve el indice de su mano
    def __getMano(self, jugadorIndex):
        manoIndex = const.MANO_JUGADOR1
        if(jugadorIndex == const.JUGADOR2):
            manoIndex = const.MANO_JUGADOR2
        return manoIndex
    
    #Se le pasa el indice de la mano del jugador y ordena su mano
    def __ordenarMano(self, manoIndex):
        manoList = self.__tablero[manoIndex]
        manoList = np.sort(manoList)
        self.__tablero[manoIndex] = manoList
        
        
    def __comprobarAccion1(self, manoIndex, filaAcciones, accionArray):
        if(self.__tablero[filaAcciones][const.TIPO_SECRETO] != 0):
            raise Exception("Accion 1 ya usada")
        #TODO: Comprobar que la carta exista en la mano
        
    def __comprobarAccion2(self, manoIndex, filaAcciones, accionArray):
        if(self.__tablero[filaAcciones][const.TIPO_RENUNCIA_1] != 0 
           or self.__tablero[filaAcciones][const.TIPO_RENUNCIA_2] != 0):
            raise Exception("Accion 2 ya usada")
        #TODO: Comprobar que las cartas existan en la mano
        
    def __comprobarAccion3(self, manoIndex, filaAcciones, accionArray):
        if(self.__tablero[filaAcciones][const.TIPO_REGALO] != 0):
            raise Exception("Accion 3 ya usada")
        #TODO: Comprobar que las cartas existan en la mano
        
    def __comprobarAccion4(self, manoIndex, filaAcciones, accionArray):
        if(self.__tablero[filaAcciones][const.TIPO_COMPETICION] != 0):
            raise Exception("Accion 4 ya usada")
        #TODO: Comprobar que las cartas existan en la mano
        
    def __comprobarAccionDecision3(self, manoIndex, accionArray):
        if(self.__tablero[const.ACCION_PENDIENTE][const.TIPO_SECRETO] != const.TIPO_DECISION_REGALO):
            raise Exception("Accion de decision 3 no disponible")
        #TODO: Comprobar que la carta exista en la 
        
    def __comprobarAccionDecision4(self, manoIndex, accionArray):
        if(self.__tablero[const.ACCION_PENDIENTE][const.TIPO_SECRETO] != const.TIPO_DECISION_COMPETICION):
            raise Exception("Accion de decision 4 no disponible")
        #TODO: Comprobar que las cartas existan en la mano
        
        
    def __guardarAccion1(self, manoIndex, filaAccionesIndex, accionArray):
        carta1 = accionArray[const.ACCION_1]
        self.__tablero[filaAccionesIndex][const.TIPO_SECRETO] = carta1
        manoList = self.__tablero[manoIndex]
        manoList = self.__soltarCarta(manoList, carta1)
        self.__tablero[manoIndex] = manoList
        
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
        cartasListOrdenada = np.sort(cartasList)
        decisionList[const.PENDIENTE_6_1_1] = cartasListOrdenada[0]
        decisionList[const.PENDIENTE_6_1_2] = cartasListOrdenada[1]
        decisionList[const.PENDIENTE_6_2_1] = cartasListOrdenada[2]
        decisionList[const.PENDIENTE_6_2_2] = cartasListOrdenada[3]
        decisionList[const.PENDIENTE_TIPO] = const.TIPO_DECISION_COMPETICION
        
        #Eliminar cartas de la mano
        manoList = self.__tablero[manoIndex]
        manoList = self.__soltarCarta(manoList, carta1)
        manoList = self.__soltarCarta(manoList, carta2)
        manoList = self.__soltarCarta(manoList, carta3)
        manoList = self.__soltarCarta(manoList, carta4)
        self.__tablero[manoIndex] = manoList
        
    
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
        
    def __guardarSecreto(self, accionesJugadorIndex, filaArmasIndex):
        carta = self.__tablero[accionesJugadorIndex][const.TIPO_SECRETO]
        self.__sumarCarta(filaArmasIndex, carta)
        
    def __sumarCarta(self, filaArmasIndex, carta):
        self.__tablero[filaArmasIndex][carta-1] = self.__tablero[filaArmasIndex][carta-1]+1
        
    def __getGanador(self):
        puntosGuerreras = [2, 2, 2, 3, 3, 4, 5]
        puntosJugador1 = 0
        puntosJugador2 = 0
        favorJugador1 = 0
        favorJugador2 = 0
        
        for i in range(const.NCOLUMNA):
            if(self.__tablero[const.FAVOR_DE_GUERRERA][i] == 1):
                puntosJugador1 = puntosJugador1 + puntosGuerreras[i]
                favorJugador1 = favorJugador1 + 1
            elif(self.__tablero[const.FAVOR_DE_GUERRERA][i] == 2):
                puntosJugador2 = puntosJugador2 + puntosGuerreras[i]
                favorJugador2 = favorJugador2 + 1
            
        if(puntosJugador1 >= 11):
            return 1
        elif (puntosJugador2 >= 11):
            return 2
        elif (favorJugador1 >= 4):
            return 1
        elif (favorJugador2 >= 4):
            return 2
        else:
            return 0

    #Se inicializa el mazo con todas las cartas menos una y se reparten las cartas iniciales
    def initRonda(self):
        self.__initMazo()
        self.__robarCarta()
        self.__repartoDeCartas()
        self.__borrarAcciones()
        self.__borrarArmas()
        
    #Se le pasa el indice del jugador
    def jugadorRobaCarta(self, jugadorIndex):
        manoIndex = self.__getMano(jugadorIndex)
        self.__conseguirCarta(manoIndex)
        self.__ordenarMano(manoIndex)
    
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
    
    
    def realizarAccion(self, jugadorIndex, accionArray):
        if(jugadorIndex != const.JUGADOR1 and jugadorIndex != const.JUGADOR2):
            raise Exception("Jugador no existente")
            
        filaAcciones = self.__getFilaAcciones(jugadorIndex)
        manoIndex = self.__getMano(jugadorIndex)
            
        if(accionArray[const.ACCION_REALIZADA] == const.TIPO_SECRETO):
            self.__comprobarAccion1(manoIndex, filaAcciones, accionArray)
            self.__guardarAccion1(manoIndex, filaAcciones, accionArray)

            
        elif (accionArray[const.ACCION_REALIZADA] == const.TIPO_RENUNCIA): 
            self.__comprobarAccion2(manoIndex, filaAcciones, accionArray)
            self.__guardarAccion2(manoIndex, filaAcciones, accionArray)
            
        elif (accionArray[const.ACCION_REALIZADA] == const.TIPO_REGALO): 
            self.__comprobarAccion3(manoIndex, filaAcciones, accionArray)
            self.__guardarAccion3(manoIndex, filaAcciones, accionArray)
            
        elif (accionArray[const.ACCION_REALIZADA] == const.TIPO_COMPETICION): 
            self.__comprobarAccion4(manoIndex, filaAcciones, accionArray)
            self.__guardarAccion4(manoIndex, filaAcciones, accionArray)
            
        elif (accionArray[const.ACCION_REALIZADA] == const.TIPO_DECISION_REGALO): 
            self.__comprobarAccionDecision3(jugadorIndex, accionArray)
            self.__guardarAccionDecision3(jugadorIndex, accionArray)
        
        elif (accionArray[const.ACCION_REALIZADA] == const.TIPO_DECISION_COMPETICION): 
            self.__comprobarAccionDecision4(jugadorIndex, accionArray)
            self.__guardarAccionDecision4(jugadorIndex, accionArray)
            
        else:
            raise Exception("Accion no encontrada")
            
    def hayAccionPendiente(self):
        pendiente = self.__tablero[const.ACCION_PENDIENTE][const.PENDIENTE_TIPO]
        return pendiente != 0
        
    def finalizarTurno(self):
        self.__guardarSecreto(const.ACCIONES_USADAS_JUGADOR1, const.ARMAS_USADAS_JUGADOR1)
        self.__guardarSecreto(const.ACCIONES_USADAS_JUGADOR2, const.ARMAS_USADAS_JUGADOR2)
        
        for i in range(const.NCOLUMNA):
            armas1 = self.__tablero[const.ARMAS_USADAS_JUGADOR1][i]
            armas2 = self.__tablero[const.ARMAS_USADAS_JUGADOR2][i]
            
            if(armas1 > armas2):
                self.__tablero[const.FAVOR_DE_GUERRERA][i] = 1
            elif(armas2 > armas1):
                self.__tablero[const.FAVOR_DE_GUERRERA][i] = 2
                
        return self.__getGanador()
    
    def printTableroCompleto(self):
        print(self.__tablero)
    

