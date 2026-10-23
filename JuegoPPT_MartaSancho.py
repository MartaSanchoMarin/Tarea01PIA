from enum import StrEnum, Enum

#region Constantes
StrGanador = "¡Enhorabuena, has ganado!"
StrPerdedor = "Ha ganado el ordenador, prueba otra vez."
StrEmpate = "¡Vaya, habéis sacado lo mismo! Prueba otra vez."
#endregion Constantes

#region Enumerados
#Enumerado con valores posibles del juego
class Opcion(StrEnum):
    ROCK = "Piedra",
    PAPER = "Papel",
    SCISSOR = "Tijera"

#Enumerado con resultados partidas
class Resultado(StrEnum):
    WINNER = "Ganador",
    LOSER = "Perdedor",
    TIE = "Empate"

#Enumerado de acciones del juego
class Accion(Enum):
    JUGAR = 1,
    SALIR = 2
#endregion Enumerados

#region Funciones
def decidir_ganador(user_action, computer_action):
    match user_action:
    case Opcion.ROCK:
        if(computer_action == Opcion.ROCK):
            return Resultado.TIE
        elif(computer_action == Opcion.PAPER):
            return Resultado.LOSER
        else
            return Resultado.WINNER
    case Opcion.PAPER:
        if(computer_action == Opcion.ROCK):
            return Resultado.WINNER
        elif(computer_action == Opcion.PAPER):
            return Resultado.TIE
        else
            return Resultado.LOSER
    case Opcion.SCISSOR:
        if(computer_action == Opcion.ROCK):
            return Resultado.LOSER
        elif(computer_action == Opcion.PAPER):
            return Resultado.WINNER
        else
            return Resultado.TIE   

def menu_acciones_juego()
#endregion Funciones

def main()