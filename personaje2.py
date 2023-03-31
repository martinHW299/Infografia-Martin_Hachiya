import time
import random

class Personaje:
    def __init__(self, nombre, vitalidad):
        self.nombre = nombre
        self.vitalidad = vitalidad
    
    def saludo(self):
        print(f"Hola, mi nombre es {self.nombre}")

    def esta_vivo(self):
        return self.vitalidad > 0

class Jugador(Personaje):
    def __init__(self, nombre, vitalidad, habilidades):
        super().__init__(nombre, vitalidad)
        self.habilidades = habilidades
    
    def recibir_daño(self, daño):
        self.vitalidad -= daño

    def contraatacar(self, enemigo):
        probabilidad_critico = random.randint(1, 10) # 10% de probabilidad de daño crítico
        if probabilidad_critico == 1:
            print(f"{self.nombre} ha realizado un contraataque crítico!")
            enemigo.recibir_daño(self.habilidades["Contraataque"] * 2)
        else:
            print(f"{self.nombre} ha realizado un contraataque!")
            enemigo.recibir_daño(self.habilidades["Contraataque"])

class Enemigo(Personaje):
    def __init__(self, nombre, vitalidad, daño_min, daño_max, ataque_esp):
        super().__init__(nombre, vitalidad)
        self.daño_min = daño_min
        self.daño_max = daño_max
        self.ataque_esp = ataque_esp
    
    def atacar_jugador(self, jugador):
        daño = random.randint(self.daño_min, self.daño_max)
        print(f"Enemigo {self.nombre} atacando a jugador {jugador.nombre} con daño: {daño}")
        jugador.recibir_daño(daño)
        if jugador.esta_vivo() and self.ataque_esp:
            print(f"Enemigo {self.nombre} está realizando un ataque especial...")
            time.sleep(2)
            probabilidad_esquivar = random.randint(1, 10)
            if probabilidad_esquivar == 1:
                print(f"{jugador.nombre} ha esquivado el ataque especial!")
            else:
                print(f"{jugador.nombre} ha recibido el ataque especial!")
                jugador.recibir_daño(self.ataque_esp)

jugador = Jugador("Juan", 100, {"Contraataque": 20})
jugador.saludo()

enemigo = Enemigo("Raul", 50, 2, 8, 20)

while jugador.esta_vivo():
    enemigo.atacar_jugador(jugador)
    if jugador.esta_vivo():
        probabilidad_contraataque = random.randint(1, 10)
        if probabilidad_contraataque == 1:
            jugador.contraatacar(enemigo)
    print(f"vitalidad {jugador.nombre}: {jugador.vitalidad}")
    time.sleep(2)

print(f"El jugador {jugador.nombre} ha muerto")
