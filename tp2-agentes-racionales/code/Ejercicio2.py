import random

def esta_sucio(init_posX, init_posY, dirt_rate, environment):
    if environment[init_posY][init_posX] <= dirt_rate: 
        environment[init_posY][init_posX] = 1
        return 1
    else: return 0

def aceptar_accion(accion, rendimiento, sizeX, sizeY, init_posX, init_posY, dirt_rate, environment):
    if accion == 1:
        if (init_posY - 1) >= 0:
            init_posY -= 1

    elif accion == 2:
        if (init_posY + 1) < sizeY:
            init_posY += 1

    elif accion == 3:
        if (init_posX + 1) < sizeX:
            init_posX += 1

    elif accion == 4:
        if (init_posX - 1) >= 0:
            init_posX -= 1
            
    elif accion == 5: #limpiar
        return esta_sucio(init_posX, init_posY, dirt_rate, environment) 
    else: #no hacer nada
        pass 
    return 0


