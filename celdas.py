import pygame
from colores import Colores
class Celdas:
    def __init__(self):
        self.num_filas = 20
        self.num_columnas = 10
        self.tamaño_celdas = 30
        self.grid = [[0 for j in range(self.num_columnas)]for i in range(self.num_filas)] #-->creacion de filas y columnas
        self.colors = Colores.color_celda()

    def mostrar_celdas(self):
        for fila in range(self.num_filas):
            for columna in range(self.num_columnas):
                print(self.grid[fila][columna] , end= "  ")
            print()

    def dentro_del_limite(self , fila , columna):
        if(fila >= 0 and fila < self.num_filas and columna >= 0 and columna < self.num_columnas):
            return True
        
        return False

    def  vacio(self, fila, columna):
        if(self.grid[fila][columna] == 0):
            return True
        return False


    def fila_completa(self , fila):
        for columna in range(self.num_columnas):
            if(self.grid[fila][columna] == 0):
                return False
        return True

    def limpiar_fila(self, fila):
        for columna in range(self.num_columnas):
            self.grid[fila][columna] = 0
    

    def mover_fila_hacia_abajo(self, fila, num_filas):
        for columna in range(self.num_columnas):
            self.grid[fila + num_filas][columna] = self.grid[fila][columna]
            self.grid[fila][columna] = 0


    def limpiar_todas_las_filas(self):
        completed = 0
        for fila in range(self.num_filas -1, 0, -1):
            if(self.fila_completa(fila)):
                self.limpiar_fila(fila)
                completed += 1
            elif(completed > 0):
                self.mover_fila_hacia_abajo(fila, completed)
        return completed

    def reset(self):
        for fila in range(self.num_filas):
            for columna in range(self.num_columnas):
                self.grid[fila][columna] = 0




    def draw(self , ventana):
        for fila in range(self.num_filas):
            for columna in range(self.num_columnas):
                valor_celda = self.grid[fila][columna]
                color_celda = self.colors[valor_celda]
                rect = pygame.Rect(columna*self.tamaño_celdas +11, fila*self.tamaño_celdas +11, self.tamaño_celdas -1 , self.tamaño_celdas -1)
                pygame.draw.rect(ventana , color_celda , rect)