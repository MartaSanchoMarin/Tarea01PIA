from enum import Enum
import random

#region Variables
opcionUsuario, opcionOrdenador, resultado = 0, 0, ""
#endregion Variables

#region Constantes
StrGanador = "¡Enhorabuena, has ganado!\n"
StrPerdedor = "Ha ganado el ordenador, prueba otra vez.\n"
StrEmpate = "¡Vaya, habéis sacado lo mismo! Prueba otra vez.\n"

StrPedirOpcionPPT = "Teclea el número correspondiente a la opción que quieres escoger (Piedra = 1, Papel = 2, Tijera = 3) o escribe 'quit' para salir.\n"
StrErrorInput = "Opción seleccionada incorrecta.\n"
StrInformativoFinal = "Has escogido {0}, el ordenador ha escogido {1}.\n{2}\n"
StrSalirJuego = "Has decidido acabar el juego."
#endregion Constantes

#region Enumerados
#Enumerado con valores posibles del juego
class Opcion(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3
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

def opcionToStringSP(opcionEscogida: Opcion):
    match opcionEscogida:
        case Opcion.ROCK:
                return "Piedra"
        case Opcion.PAPER:
                return "Papel"
        case Opcion.SCISSOR:
                return "Tijera"  
#endregion Funciones

def main():
    while(True):
        #pedimos al usuario la opción y comprobamos qué ha introducido
        inputUsuario = input(StrPedirOpcionPPT).strip().lower()
        #si pone quit se acaba el juego
        if inputUsuario == "quit":
            print(StrSalirJuego)
            break
        #revisamos si el usuario ha introducido un número y si coincide con los que proporcionamos en el enum
        while not (inputUsuario.isdigit() and int(inputUsuario) in {1, 2, 3}):
            #si no coincide lo volvemos a pedir
            print(StrErrorInput)
            inputUsuario = input(StrPedirOpcionPPT).strip().lower()
            
            if inputUsuario == "quit":
                print(StrSalirJuego)
                return
        opcionUsuario = Opcion(int(inputUsuario))
        
        #seleccionamos la opción del ordenador pasandole una lista de las opciones que hay
        opcionOrdenador = random.choice(list(Opcion))
        #llamamos a la función que determina quién gana
        resultado = decidir_ganador(opcionUsuario, opcionOrdenador)
        #mostramos el resultado
        print(StrInformativoFinal.format(opcionToStringSP(opcionUsuario), opcionToStringSP(opcionOrdenador), resultado))

if __name__ == "__main__":
    main()
