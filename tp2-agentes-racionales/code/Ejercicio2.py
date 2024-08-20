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


entorno = [2, 4, 8, 16, 32, 64, 128]
suciedad = [0.1, 0.2, 0.4, 0.8]

for i in range (0, len(entorno)):

    environment = [[round(random.random(), 2) for _ in range(entorno[i])] for _ in range(entorno[i])]
    sizeY = entorno[i]
    sizeX = entorno[i]
    init_posX = random.randint(0, sizeX-1)
    init_posY = random.randint(0, sizeY-1)

    for j in range (0, len(suciedad)):

        rendimiento = 0
        dirt_rate = suciedad[j]
        print("ENTORNO: ",  entorno[i], " x ", entorno[i])
        print("DIRT_RATE: ", suciedad[j])
        performance = 0

        for k in range (0, 999):

            accion = random.randint(1,5)
            rendimiento += aceptar_accion(accion, rendimiento, sizeX, sizeY, init_posX, init_posY, dirt_rate, environment)    
        print("Medida de desempeño para matriz de dimensión ", entorno[i], " x ", entorno[i], ", con dirt_rate = ", suciedad[j],  ":", rendimiento)




