from colores import Colores
from celdas import Celdas
from posiciones import Posicion
import pygame
class Blocks: 
    def __init__(self , id):
       self.id = id
       self.celdas = {}
       self.tamaño_celdas = 30
       self.rotation_state = 0
       self.colors =  Colores.color_celda()
       self.desplazar_fila = 0
       self.desplazar_columna = 0
    

    def mover(self , filas, columnas):
        self.desplazar_fila += filas
        self.desplazar_columna += columnas


    def posiciones_celdas(self):
        tiles = self.celdas[self.rotation_state]
        moved_tiles = []
        for posicion in tiles:
            posicion = Posicion(posicion.fila + self.desplazar_fila, posicion.columna + self.desplazar_columna)
            moved_tiles.append(posicion)
        return moved_tiles 

    def rotacion(self):
        self.rotation_state += 1

        if(self.rotation_state == len(self.celdas)):
            self.rotation_state = 0

    def undo_rotation(self):
        self.rotation_state -= 1
        if(self.rotation_state == 0):
            self.rotation_state = len(self.celdas) -1


    def dibujar(self, ventana):
        tiles = self.posiciones_celdas()
        for tile in tiles:
            tile_rect = pygame.Rect(tile.columna*self.tamaño_celdas +11, tile.fila*self.tamaño_celdas +11, self.tamaño_celdas -1, self.tamaño_celdas -1)
            pygame.draw.rect(ventana, self.colors[self.id], tile_rect)
            


