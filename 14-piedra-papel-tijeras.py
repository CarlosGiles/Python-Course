"""
Piedra, papel o tijeras con input() para dos jugadores.
    - El juego consiste en que dos jugadores eligen entre piedra, papel o tijeras.
    - El jugador que elige piedra gana al que elige tijeras, el que elige tijeras gana al que
    elige papel y el que elige papel gana al que elige piedra.
"""

# Definimos las opciones
opciones = ["piedra", "papel", "tijeras"]
# Pedimos la opción al jugador 1
jugador1 = input("Jugador 1, elige piedra, papel o tijeras: ").lower()
# Pedimos la opción al jugador 2
jugador2 = input("Jugador 2, elige piedra, papel o tijeras: ").lower()
# Comprobamos que las opciones son válidas
if jugador1 not in opciones or jugador2 not in opciones:
    print("Opción no válida. Elige entre piedra, papel o tijeras.")
else:
    # Comprobamos quién gana
    if jugador1 == jugador2:
        print("Empate")
    elif (jugador1 == "piedra" and jugador2 == "tijeras") or \
         (jugador1 == "papel" and jugador2 == "piedra") or \
         (jugador1 == "tijeras" and jugador2 == "papel"):
        print("Jugador 1 gana")
    else:
        print("Jugador 2 gana")
