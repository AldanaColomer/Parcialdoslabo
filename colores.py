class  Colores:

    BLANCO = (255,255,255)
    ROJO = (255,0,0)
    VERDE = (0,255,0)
    ROSA = (255,0,255)
    AZUL_OSCURO = (44,44,127)
    NEGRO = (0,0,0)
    AZUL_CLARO = (59, 85, 162)


    @classmethod
    def color_celda(cls):
        return [cls.NEGRO, cls.ROJO, cls.AZUL_OSCURO, cls.VERDE, cls.ROSA, cls.BLANCO]