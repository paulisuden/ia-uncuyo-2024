# **Trabajo Práctico 2: Agentes racionales**

## **1. Para cada una de las siguientes actividades, describa el PEAS para cada tarea y caracterizarlo en término de las propiedades vistas.**

### **a. Jugar al CS (o cualquier otro 3d Shooter).** 
#### **1. Definición del Entorno (E):** mapas
#### **2. Sensores (S):** pantalla, sonidos
#### **3. Actuadores (A):** mouse y teclado
#### **4. Medida de desempeño o Performance (P):** lograr los objetivos y eliminar a los enemigos.

Caracteristicas:
Multiagente, continuo, parcialmente observable (no se puede ver el mapa completo ni a todos los enemigos al mismo tiempo) y dinámico (el entorno cambia constantemente con los movimientos y acciones de los jugadores)

### **b) Explorar los océanos. **
#### **1. Definición del Entorno (E):** océano
#### **2. Sensores (S):** vista, sonidos (cámaras submarinas, hidrófonos)
#### **3. Actuadores (A):** helicóptero, barco, submarino
#### **4. Medida de desempeño o Performance (P):** realizar nuevos descubrimientos (por ejemplo especies)

Características:
Multiagente, continuo, parcialmente observable (hay áreas desconocidas y fuera del alcance de los sensores) y dinámico (el océano cambia constantemente)

### **c) Comprar y vender tokens crypto (alguno).**

#### **1. Definición del Entorno (E):** alguna app de crypto (ejemplo bitcoin wallet)
#### **2. Sensores (S):** notificación de la app o información sobre precios
#### **3. Actuadores (A):** mouse y teclado, dedos para realizar compra y venta
#### **4. Medida de desempeño o Performance (P):** ganancias y pérdidas

Características:
Único agente, discreto (las transacciones ocurren en intervalos específicos de tiempo), parcialmente observable y dinámico (los precios de las criptomonedas cambian constantemente).


### **d)Practicar tenis contra una pared.**

#### **1. Definición del Entorno (E):** pared y piso
#### **2. Sensores (S):** vista, sonido, tacto
#### **3. Actuadores (A):** raqueta, movimientos del cuerpo
#### **4. Medida de desempeño o Performance (P):** consistencia, precisión en el juego

Características:
Único agente, continuo, completamente observable (el jugador puede ver todo como la pared, pelota y piso), y dinámico (la situación cambia con cada golpe de la pelota).


### ** e) Realizar un salto de altura.**

#### **1. Definición del Entorno (E):** listón (barra horizontal)
#### **2. Sensores (S):** vista, cálculo de altura
#### **3. Actuadores (A):** movimiento de piernas y cuerpo en general (para realizar el salto)
#### **4. Medida de desempeño o Performance (P):** si sobrepasó o no la altura determinada por el listón

Características:
Único agente, continuo, completamente observable y estátic (el listón y el entorno no cambian mientras se realiza el salto).

### **f ) Pujar por un artículo en una subasta.**

#### **1. Definición del Entorno (E):** casa de subastas, postores, artículos
#### **2. Sensores (S):** sonido, vista
#### **3. Actuadores (A):** la voz (realizar ofertas)
#### **4. Medida de desempeño o Performance (P):** ganar el artículo al mejor precio posible

Características:
Multiagente, discreto, parcialmente observable (no se conocen las estrategias ni límites de los demás postores) y dinámico.
