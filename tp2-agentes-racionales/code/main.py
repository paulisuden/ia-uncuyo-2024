import random
import Ejercicio3
import Ejercicio2 as ej2
import copy

entorno = [2, 4, 8, 16, 32, 64, 128]
suciedad = [0.1, 0.2, 0.4, 0.8]

for i in range (0, len(entorno)):

    sizeY = entorno[i]
    sizeX = entorno[i]
    init_posX = random.randint(0, sizeX-1)
    init_posY = random.randint(0, sizeY-1)
    print("ENTORNO: ",  entorno[i], " x ", entorno[i])
    listaR = []
    listaA = []
    for j in range (0, len(suciedad)):
        
        rendimientoA = 0
        dirt_rate = suciedad[j]
        sumaR = 0
        promedioR = 0
        sumaA = 0
        promedioA = 0
        
        for k in range (0, 9):
            
            environment = Ejercicio3.Environment(sizeX, sizeY, init_posX, init_posY,dirt_rate)
            agent = Ejercicio3.Agent(environment)
            matrizA = copy.deepcopy(environment.matrix)

            if k == 0 and sizeX == 4 and dirt_rate == 0.4:
                print(environment.matrix)
            
            for l in range (0,999):
                agent.think()

                accion = random.randint(1,5)
                rendimientoA += ej2.aceptar_accion(accion, rendimientoA, sizeX, sizeY, init_posX, init_posY, dirt_rate, matrizA)   
            
                
            sumaR += environment.get_performance()  
            
        promedioR = sumaR / 10
        listaR.append(promedioR)
        promedioA = rendimientoA / 10
        listaA.append(promedioA)

    print("aleatorio:")
    print(listaA)
    print("reflexivo:")
    print(listaR)
