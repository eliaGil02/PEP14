from personajes import Guerrero, Mago, Arma


def combate(personaje1, personaje2):
    print("⚔️  ¡Comienza el combate!")
    print(f"{personaje1.nombre} vs {personaje2.nombre}\n")

    # Combate por turnos
    while personaje1.vivo and personaje2.vivo:
        personaje1.atacar(personaje2)
        print(f"Vida de {personaje2.nombre}: {personaje2.vida}\n")

        if personaje2.vivo:
            personaje2.atacar(personaje1)
            print(f"Vida de {personaje1.nombre}: {personaje1.vida}\n")

    # Resultado final
    if personaje1.vivo:
        print(f"🏆 {personaje1.nombre} gana con {personaje1.vida} de vida restante")
    else:
        print(f"🏆 {personaje2.nombre} gana con {personaje2.vida} de vida restante")


def main():
    # Crear arma
    espada = Arma("Espada", 15)

    # Crear personajes
    guerrero = Guerrero("Kuma", 100, espada)

    hechizos = {"Bola de fuego": 18, "Rayo": 22}
    mago = Mago("Merlín", 80, hechizos)

    # Iniciar combate
    combate(guerrero, mago)


main()
