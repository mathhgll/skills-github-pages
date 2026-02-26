import time
import os

def limpiar():
    os.system("cls")  # En Windows limpia la consola

def crear_corazon(nombre, escala):
    base = """
      @@@@@@@@           @@@@@@@@
   @@@@@@@@@@@@@     @@@@@@@@@@@@@
 @@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
     @@@@@@@@@@@@@@@@@@@@@@@@@@@
       @@@@@@@@@@@@@@@@@@@@@@@
         @@@@@@@@@@@@@@@@@@@
           @@@@@@@@@@@@@@@
             @@@@@@@@@@@
               @@@@@@@
                 @@@
                  @
"""

    # Escala el corazón (lo hace más grande o pequeño)
    lineas = []
    for linea in base.split("\n"):
        nueva = ""
        for caracter in linea:
            nueva += caracter * escala
        for _ in range(escala):
            lineas.append(nueva)

    corazon = "\n".join(lineas)

    letras = list(nombre)
    i = 0
    while '@' in corazon:
        corazon = corazon.replace('@', letras[i % len(letras)], 1)
        i += 1

    return corazon


def main():
    nombre = "Itzel"

    while True:
        # Latido grande
        limpiar()
        print(crear_corazon(nombre, 2))
        print(f"\nTe amo, {nombre} 💖")
        time.sleep(0.4)

        # Latido pequeño
        limpiar()
        print(crear_corazon(nombre, 1))
        print(f"\nTe amo, {nombre} 💖")
        time.sleep(0.4)


if __name__ == "__main__":
    main()