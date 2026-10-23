from enum import Enum
import random

#region Variables
opcionUsuario, opcionOrdenador, resultado = ""
#endregion Variables

#region Constantes
StrGanador = "¡Enhorabuena, has ganado!"
StrPerdedor = "Ha ganado el ordenador, prueba otra vez."
StrEmpate = "¡Vaya, habéis sacado lo mismo! Prueba otra vez."
StrEnunciadoInicial = "Bienvenid@ al juego PPT, juega a piedra papel o tijera contra el ordenador. Selecciona 1 para jugar o 2 para salir del juego."
StrPedirOpcion = "Teclea el número correspondiente a la opción que quieres escoger: Piedra = 1, Papel = 2, Tijera = 3."
StrErrorInput = "Opción seleccionada incorrecta."
StrInformativoFinal = f"Has escogido {opcionUsuario}, el ordenador ha escogido {opcionOrdenador}. \n El resultado final es: {resultado}"
#endregion Constantes

#region Enumerados
#Enumerado con valores posibles del juego
class Opcion(Enum):
    ROCK = 1,
    PAPER = 2,
    SCISSOR = 3

#Enumerado de acciones del juego
class Accion(Enum):
    JUGAR = 1,
    SALIR = 2
#endregion Enumerados

#region Funciones
def decidir_ganador(user_action: Opcion, computer_action: Opcion):
    match user_action:
        case Opcion.ROCK:
            if(computer_action == Opcion.ROCK):
                return StrEmpate
            elif(computer_action == Opcion.PAPER):
                return StrPerdedor
            else:
                return StrGanador
        case Opcion.PAPER:
            if(computer_action == Opcion.ROCK):
                return StrGanador
            elif(computer_action == Opcion.PAPER):
                return StrEmpate
            else:
                return StrPerdedor
        case Opcion.SCISSOR:
            if(computer_action == Opcion.ROCK):
                return StrPerdedor
            elif(computer_action == Opcion.PAPER):
                return StrGanador
            else:
                return StrEmpate  
#endregion Funciones

def main():
    salir = True
    while(salir):
        accionElegida = input(StrEnunciadoInicial)
        while(accionElegida not in{1,2}):
            print(StrErrorInput)
            accionElegida = input(StrEnunciadoInicial)
        if(accionElegida == 1):
            opcionUsuario = input(StrPedirOpcion)
            while(accionElegida not in{1,2,3}):
                print(StrErrorInput)
                opcionUsuario = input(StrPedirOpcion)
            opcionOrdenador = random.choice(Opcion)
            resultado = decidir_ganador(opcionUsuario, opcionOrdenador)
            print(StrInformativoFinal, opcionOrdenador, opcionOrdenador, resultado)
            
        else:
            salir = False

