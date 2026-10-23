from enum import StrEnum, Enum

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
def decidir_ganador()
def menu_acciones_juego()
#endregion Funciones

def main()