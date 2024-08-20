import random
import Ejercicio3


entorno = [2, 4, 8, 16, 32, 64, 128]
suciedad = [0.1, 0.2, 0.4, 0.8]

for i in range (0, len(entorno)):

    sizeY = entorno[i]
    sizeX = entorno[i]
    init_posX = random.randint(0, sizeX-1)
    init_posY = random.randint(0, sizeY-1)

    for j in range (0, len(suciedad)):

        rendimiento = 0
        dirt_rate = suciedad[j]
        environment = Ejercicio3.Environment(sizeX, sizeY, init_posX, init_posY,dirt_rate)
        agent = Ejercicio3.Agent(environment)
        print("ENTORNO: ",  entorno[i], " x ", entorno[i])
        print("DIRT_RATE: ", suciedad[j])

        for k in range (0, 9):
            agent.think()
        print("Medida de desempeño para matriz de dimensión ", entorno[i], " x ", entorno[i], ", con dirt_rate = ", suciedad[j],  ":", environment.get_performance())

