from celdas import Celdas
from creacion_bloques import *
import random
class Game:
    def __init__(self):
        self.celda = Celdas()
        self.blocks = [BloqueCuadrado(), BloqueI(), BloqueL(), BloqueT()]
        self.bloque_actual = self.bloques_random()
        self.bloque_siguiente = self.bloques_random()
        self.game_over = False
        self.score = 0
    
    def actualizar_score(self, filas_limpias, puntos):
        if filas_limpias == 1:
            self.score += 100
        elif filas_limpias == 2:
            self.score += 200
        elif filas_limpias == 3:
            self.score += 300
        self.score += puntos




    def bloques_random(self):
        if (len(self.blocks) == 0):
            self.blocks = [BloqueCuadrado(), BloqueI(), BloqueL(), BloqueT()]
        bloque = random.choice(self.blocks)
        self.blocks.remove(bloque)
        return bloque

    def mover_izquierda(self):
        self.bloque_actual.mover(0, -1)
        if(self.bloque_en_limite() == False or self.bloque_encajado() == False):
            self.bloque_actual.mover(0,1)

    def mover_derecha(self):
        self.bloque_actual.mover(0, 1)
        if(self.bloque_en_limite()==False or self.bloque_encajado() == False):
            self.bloque_actual.mover(0,-1)

    def mover_abajo(self):
        self.bloque_actual.mover(1,0)
        if(self.bloque_en_limite()==False or self.bloque_encajado() == False):
            self.bloque_actual.mover(-1,0)
            self.lock_block()


    def lock_block(self):
        tiles  = self.bloque_actual.posiciones_celdas()
        for position in tiles:
            self.celda.grid[position.fila][position.columna] = self.bloque_actual.id
        self.bloque_actual = self.bloque_siguiente
        self.bloque_siguiente = self.bloques_random()
        filas_limpias = self.celda.limpiar_todas_las_filas()
        self.actualizar_score(filas_limpias, 0)
        if(self.bloque_encajado() == False):
            self.game_over = True

    def reset(self):
        self.celda.reset()
        self.blocks = [BloqueCuadrado(), BloqueI(), BloqueL(), BloqueT()]
        self.bloque_actual = self.bloques_random()
        self.bloque_siguiente = self.bloques_random()
        self.score = 0

    def bloque_encajado(self):
        tiles = self.bloque_actual.posiciones_celdas()
        for tile in tiles:
            if(self.celda.vacio(tile.fila, tile.columna) == False):
                return False
        return True

    def bloque_en_limite(self):
        tiles = self.bloque_actual.posiciones_celdas()
        for tile in tiles:
            if(self.celda.dentro_del_limite(tile.fila , tile.columna) == False):
                return False
            
        return  True


    def rotar(self):
        self.bloque_actual.rotacion()
        if(self.bloque_en_limite() == False or self.bloque_encajado() == False):
            self.bloque_actual.undo_rotation()

    def draw(self, ventana):
        self.celda.draw(ventana)
        self.bloque_actual.dibujar(ventana)
