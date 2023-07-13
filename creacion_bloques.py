from bloques import Blocks
from posiciones import Posicion


class BloqueT(Blocks):
    def __init__(self):
        super().__init__(id = 5)
        self.celdas = {
                        0:[Posicion(0,1), Posicion(1,0), Posicion(1,1), Posicion(1,2)],
                        1:[Posicion(0,1), Posicion(1,1), Posicion(1,2), Posicion(2,1)],
                        2:[Posicion(1,0), Posicion(1,1), Posicion(1,2), Posicion(2,1)],
                        3:[Posicion(0,1), Posicion(1,0), Posicion(1,1), Posicion(2,1)]
        }
        self.mover(0,3)


    
class BloqueCuadrado(Blocks):
    def __init__(self):
        super().__init__(id = 4)
        self.celdas = {
                        0:[Posicion(0,0), Posicion(0,1), Posicion(1,0), Posicion(1,1)],
                        1:[Posicion(0,0), Posicion(0,1), Posicion(1,0), Posicion(1,1)],
                        2:[Posicion(0,0), Posicion(0,1), Posicion(1,0), Posicion(1,1)],
                        3:[Posicion(0,0), Posicion(0,1), Posicion(1,0), Posicion(1,1)]
            }
        self.mover(0,4)



class BloqueI(Blocks):
    def __init__(self):
        super().__init__(id = 3)
        self.celdas = {
                        0:[Posicion(1,0), Posicion(1,1), Posicion(1,2), Posicion(1,3)],
                        1:[Posicion(0,2), Posicion(1,2), Posicion(2,2), Posicion(3,2)],
                        2:[Posicion(2,0), Posicion(2,1), Posicion(2,2), Posicion(2,3)],
                        3:[Posicion(0,1), Posicion(1,1), Posicion(2,1), Posicion(3,1)]
        }
        self.mover(0,3)



class BloqueL(Blocks):
    def __init__(self):
        super().__init__(id = 1)
        self.celdas = {
                        0:[Posicion(0,2), Posicion(1,0), Posicion(1,1), Posicion(1,2)],
                        1:[Posicion(0,1), Posicion(1,1), Posicion(2,1), Posicion(2,2)],
                        2:[Posicion(1,0), Posicion(1,1), Posicion(1,2), Posicion(2,0)],
                        3:[Posicion(0,0), Posicion(0,1), Posicion(1,1), Posicion(2,1)]

        }
        self.mover(0,3)
