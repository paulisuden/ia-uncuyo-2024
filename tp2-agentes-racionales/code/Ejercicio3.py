import random

class Environment:
    def __init__(self,sizeX,sizeY,init_posX,init_posY,dirt_rate):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.init_posX = init_posX
        self.init_posY = init_posY
        self.dirt_rate = dirt_rate
        self.performance = 0
        self.matrix = [[round(random.random(), 2) for _ in range(self.sizeX)] for _ in range(self.sizeY)]

    def is_dirty(self):
        if self.matrix[self.init_posY][self.init_posX] <= self.dirt_rate: 
            return True
        else:
            return False

    def accept_action(self, accion):
        if accion == 1 and (self.init_posY - 1) >= 0:
            self.init_posY -= 1
        elif accion == 2 and (self.init_posY + 1) < self.sizeY:
            self.init_posY += 1
        elif accion == 3 and (self.init_posX + 1) < self.sizeX:
            self.init_posX += 1
        elif accion == 4 and (self.init_posX - 1) >= 0:
            self.init_posX -= 1
        elif accion == 5:
            pass

    def get_performance(self):
        return self.performance

    def print_environment(self):
        print(self.sizeX,
        self.sizeY,
        self.init_posX,
        self.init_posY,
        self.dirt_rate)


class Agent:
    def __init__(self,env): # recibe como parametro un objeto
                            # de la clase Environment
        self.env = env

    def perspective(self,env): # sensa el entorno
        return self.env.is_dirty()

    def think(self): # implementa las acciones a seguir por el agente
        if self.perspective(self.env):
            self.env.matrix[self.env.init_posY][self.env.init_posX] = 1
            self.env.performance += 1
        else:
            action = random.randint(1,5)  #ALEATORIA
            self.env.accept_action(action)

    
