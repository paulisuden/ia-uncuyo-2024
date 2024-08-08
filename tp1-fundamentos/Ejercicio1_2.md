# **EJERCICIO 1**

Primero, algo de terminología: la afirmación de que las máquinas podrían actuar como si fueran inteligentes se llama la hipótesis de IA débil por los filósofos, y la afirmación de que las máquinas que lo hacen realmente están pensando (no solo simulando pensar) se llama la hipótesis de IA fuerte.

## **_IA DÉBIL_**

Alan Turing examinó una amplia variedad de posibles objeciones a la posibilidad de máquinas inteligentes, incluyendo prácticamente todas las que se han planteado en el medio siglo desde que apareció su artículo. Aquí alguna de ellas:

### **1. El argumento de la discapacidad**

Aquí se sugiere que "una máquina nunca podrá hacer X", como por ejemplo ser amable, tener sentido del humor, enamorarse, aprender de la experiencia y realizar algo verdaderamente nuevo. Pero existen ciertas contradicciones a este argumento como por ejemplo, que las computadoras pueden cometer errores y hacer que alguien se "enamore" de ellas, como con el oso de peluche. Además, las computadoras ya realizan muchas tareas a nivel de expertos humanos, como jugar ajedrez, diagnosticar enfermedades, hacer descubrimientos científicos, etc.

Es decir, como conclusión, las computadoras pueden hacer muchas cosas tan bien o mejor que los humanos, aunque esto no significa que usen perspicacia y comprensión humana. Pero, aun asi, todavía hay muchas tareas en las que las computadoras no sobresalen, como mantener una conversación abierta.


### **2. Objeción matemática:**

Teorema de Gödel:

•	G(F) is a sentence of F, but cannot be proved within F. 

•	If F is consistent, then G(F) is true.

J. R. Lucas afirma que este teorema muestra que las máquinas son mentalmente inferiores a los humanos, porque las máquinas son sistemas formales que están limitados por el teorema de incompletitud (no pueden establecer la verdad de su propia oración de Gödel), mientras que los humanos no tienen tal limitación. Pero tenemos tres problemas con esta afirmación. 

Primero, el teorema se aplica solo a sistemas formales que son lo suficientemente poderosos para hacer aritmética. Las máquinas de Turing son infinitas, mientras que las computadoras son finitas, y cualquier computadora puede describirse como un gran sistema en lógica proposicional, que no está sujeto al teorema de incompletitud de Gödel.

Segundo, un agente no debería sentirse demasiado avergonzado de no poder establecer la verdad de alguna oración mientras otros agentes pueden. Tercero, y lo más importante, incluso si concedemos que las computadoras tienen limitaciones sobre lo que pueden probar, no hay evidencia de que los humanos sean inmunes a esas limitaciones.

###	**3. Argumento de la informalidad del comportamiento:**

Esto sugiere que el comportamiento humano es demasiado complejo para ser capturado por un conjunto simple de reglas, y que las computadoras, al seguir solo reglas, no pueden alcanzar la inteligencia humana. Este problema se conoce como el problema de la calificación en la IA.

Dreyfus, junto con su hermano Stuart, critican la "Inteligencia Artificial de la Vieja Escuela" (GOFAI), que afirma que todo comportamiento inteligente puede ser capturado mediante reglas lógicas. Esto es debido a que, según ellos, GOFAI es vulnerable al problema de la calificación, ya que no puede manejar dominios abiertos con la misma eficacia que los sistemas de razonamiento probabilístico. Y, además, la pericia humana incluye conocimiento de reglas, pero en un contexto holístico que las computadoras no pueden replicar completamente. Un ejemplo de comportamiento humano es dar regalos. Los humanos responden intuitivamente en situaciones sociales, algo que Dreyfus dice que las reglas lógicas no pueden capturar.

Por otro lado, Dreyfus y Dreyfus proponen un proceso de cinco etapas para adquirir pericia, comenzando con el procesamiento basado en reglas (similar al propuesto en GOFAI) y culminando con la capacidad de seleccionar respuestas correctas instantáneamente. 

**1.	Generalización con conocimiento previo:**
   
- La generalización de ejemplos no se puede lograr sin conocimiento previo y no hay forma de incorporar dicho conocimiento en el proceso de aprendizaje de redes neuronales.

**2.	Aprendizaje supervisado:**

- El aprendizaje en redes neuronales es supervisado, requiriendo identificación previa de entradas y salidas correctas, y no puede operar autónomamente sin un entrenador humano.

**3.	Rendimiento con muchas características:**

- Los algoritmos de aprendizaje no funcionan bien con muchas características y que no hay forma conocida de añadir nuevas características si las actuales son insuficientes.

- Métodos modernos como las máquinas de soporte vectorial manejan bien grandes conjuntos de características, y hay formas de generar nuevas características.

**4.	Dirección de sensores y procesamiento de información:**

- El cerebro dirige sus sensores para buscar información relevante y procesarla, pero no se entienden los detalles de este mecanismo. La visión activa, respaldada por la teoría del valor de la información, aborda este problema y ya ha sido implementada en algunos robots.

Muchos de los problemas en los que Dreyfus se ha centrado, como el conocimiento de sentido común, el problema de la calificación, la incertidumbre, el aprendizaje y la toma de decisiones compilada, son temas importantes y ya se han incorporado en el diseño estándar de agentes inteligentes, lo que evidencia el progreso de la IA.

Por otro lado, Dreyfus destaca la importancia de los agentes situados en lugar de motores de inferencia lógica desencarnados. Un agente con experiencia directa y física (por ejemplo, interactuar con perros) tiene ventaja sobre uno que solo entiende "perro" a través de sentencias lógicas. La "cognición corporizada" sugiere que el cerebro debe considerarse dentro de un cuerpo y un entorno, estudiando el sistema completo. Bajo este enfoque, la robótica, la visión y otros sensores son centrales, no periféricos.

## **_IA FUERTE_**

Si bien es fácil estar de acuerdo en que las simulaciones de tormentas en computadoras no nos mojan, no está claro cómo llevar esta analogía a las simulaciones de procesos mentales en computadoras. 

### **Teoría dualista**

Se basa en el problema mente-cuerpo la cual sirve para la pregunta de si las máquinas podrían tener mentes reales. Para esto, consideraron la actividad mental del pensamiento y los procesos físicos del cuerpo, concluyendo que ambos deben existir en reinos separados. 

El problema es cómo la mente puede controlar el cuerpo si realmente son entidades separadas. Descartes especuló que los dos podrían interactuar a través de la glándula pineal, lo que simplemente plantea la pregunta de cómo la mente controla la glándula pineal.

### **Teoría mionista**

Dicha teoría, a menudo llamada fisicalismo, afirma que la mente no está separada del cuerpo, es decir, que los estados mentales son estados físicos. El fisicalismo permite, al menos en principio, la posibilidad de una IA fuerte.

### **1. Estados mentales y el cerebro en una cubeta**

¿Qué significa decir que una persona y, una computadora se encuentra en un estado mental particular? Para esto, nos centramos en particular en los estados intencionales. Estos son estados, como creer, saber, desear, temer, y otros similares, que se refieren a algún aspecto del mundo externo

Si el fisicalismo es correcto, la descripción adecuada del estado mental de una persona está determinada por el estado cerebral de esa persona

Por ejemplo, imagina que tu cerebro fue removido de tu cuerpo al nacer y colocado en una cubeta maravillosamente diseñada. Tienes una vida simulada que replica exactamente la vida que habrías vivido, si tu cerebro no hubiera sido colocado en la cubeta. Así, podrías tener un estado cerebral idéntico al de alguien que realmente está comiendo una hamburguesa real, pero sería literalmente falso decir que tienes el estado mental "saber que uno está comiendo una hamburguesa"

El contenido de los estados mentales puede ser interpretado desde dos puntos de vista diferentes:

La visión de "contenido amplio" considera que el contenido de los estados mentales involucra tanto el estado cerebral como la historia ambiental. Por otro lado, el contenido estrecho considera solo el estado cerebral. El contenido estrecho de los estados cerebrales de un verdadero comedor de hamburguesas y un "comedor" de "hamburguesas" con cerebro en una cubeta es el mismo en ambos casos.

Entonces, si uno está preocupado por la cuestión de si los sistemas de IA están realmente pensando y realmente tienen estados mentales, entonces el contenido estrecho es apropiado; simplemente no tiene sentido decir que si un sistema de IA está realmente pensando depende de condiciones externas a ese sistema. Esto lleva a la idea de que lo que importa acerca de un estado cerebral es su rol funcional dentro de la operación mental de la entidad involucrada.

### **El funcionalismo y el experimento de reemplazo cerebral**

La teoría del funcionalismo dice que un estado mental es cualquier condición causal intermedia entre la entrada y la salida. Según la teoría funcionalista, dos sistemas cualesquiera con procesos causales isomórficos tendrían los mismos estados mentales. Por lo tanto, un programa informático podría tener los mismos estados mentales que una persona.

Consideremos un experimento el cual consiste en reemplazar gradualmente todas las neuronas de la cabeza de una persona con dispositivos electrónicos. Nos preocupamos tanto por el comportamiento externo como por la experiencia interna del sujeto, durante y después de la operación. Según la definición del experimento, el comportamiento externo del sujeto debe permanecer inalterado en comparación con lo que se observaría si la operación no se llevara a cabo. Ahora bien, la presencia o ausencia de conciencia no puede ser fácilmente determinada por un tercero. Algunos, están convencidos de que su conciencia no se vería afectada, y otros están igualmente convencidos de que su conciencia se desvanecería. Por lo que llegamos a tres conclusiones posibles: 

1. Los mecanismos causales de la conciencia que generan este tipo de salidas en los cerebros normales todavía están operando en la versión electrónica, que por lo tanto es consciente. 

2. Los eventos mentales conscientes en el cerebro normal no tienen conexión causal con el comportamiento, y están ausentes del cerebro electrónico, que por lo tanto no es consciente.  

3. El experimento es imposible y, por lo tanto, la especulación sobre él no tiene sentido.

### **El naturalismo biológico y la habitación china**

John Searle afirma que los estados mentales son características emergentes de alto nivel que son causadas por procesos físicos de bajo nivel en las neuronas, y son las propiedades (no especificadas) de las neuronas las que importan. Por lo tanto, los estados mentales no pueden duplicarse sólo sobre la base de algún programa que tenga la misma estructura funcional con el mismo comportamiento de entrada-salida; Necesitaríamos que el programa se ejecutara en una arquitectura con el mismo poder causal que las neuronas. Su conclusión es que ejecutar el programa apropiado (es decir, tener las salidas correctas) no es una condición suficiente para ser una mente.

Para respaldar su punto de vista, Searle describe un sistema hipotético que consta de un humano, que solo entiende inglés, equipado con un libro de reglas, escrito en inglés, y varias pilas de papel, algunas en blanco, otras con inscripciones indescifrables. El sistema está dentro de una habitación con una pequeña abertura hacia el exterior. Por la abertura aparecen papelitos con símbolos indescifrables. El humano encuentra símbolos coincidentes en el libro de reglas y sigue las instrucciones. Las instrucciones pueden incluir escribir símbolos en tiras de papel nuevas, encontrar símbolos en las pilas, reorganizar las pilas, etc. Eventualmente, las instrucciones harán que uno o más símbolos se transcriban en una hoja de papel que se devuelve al mundo exterior. Por lo tanto, el ser humano desempeña el papel de la CPU, el libro de reglas es el programa y las pilas de papel son el dispositivo de almacenamiento.

Desde el exterior, vemos un sistema que toma información en forma de oraciones chinas y genera respuestas en chino que son tan "inteligentes" como las de la conversación imaginada por Turing. Searle luego argumenta: la persona en la habitación no entiende chino. El libro de reglas y las pilas de papel, al ser solo pedazos de papel, no entienden chino. Por lo tanto, no hay comprensión del chino. Por lo tanto, según Searle, ejecutar el programa correcto no genera necesariamente comprensión.

### **La conciencia, los qualia y la brecha explicativa**

La conciencia a menudo se descompone en aspectos como la comprensión y la autoconciencia. Por otro lado, qualia es el término técnico para la naturaleza intrínseca de las experiencias (significa, aproximadamente, "tales cosas"). 

Los qualia presentan un desafío para las explicaciones funcionalistas de la mente porque diferentes qualia podrían estar involucrados en lo que de otro modo serían procesos causales isomórficos. Supongamos, que hemos completado el proceso de investigación científica sobre el cerebro: hemos descubierto que el proceso neuronal P12 en la neurona N177 transforma la molécula A en molécula B, y así sucesivamente. Sencillamente, no existe ninguna forma de razonamiento actualmente aceptada que conduzca a partir de tales hallazgos a la conclusión de que la entidad propietaria de esas neuronas tenga alguna experiencia subjetiva particular. 

Esta laguna explicativa ha llevado a algunos filósofos a concluir que los seres humanos son simplemente incapaces de formar una comprensión adecuada de su propia conciencia. Otros, evitan la brecha negando la existencia de los qualia, atribuyéndolos a una confusión filosófica. Y por último, el propio Turing admite que la cuestión de la conciencia es difícil, pero niega que tenga mucha relevancia para la práctica de la IA

### **La ética y los riesgos de desarrollar Inteligencia Artificial.**

Debemos considerar si debemos desarrollar IA. Si es más probable que los efectos de la tecnología de IA sean negativos que positivos, entonces sería responsabilidad moral de los trabajadores en el campo redirigir su investigación. Muchas nuevas tecnologías han tenido efectos secundarios negativos no deseados, por ejemplo, la fisión nuclear trajo a Chernobyl y la amenaza de destrucción global.

La IA, plantea algunos problemas éticos nuevos más allá de, por ejemplo, construir puentes que no se caigan (como es en el caso de los ingenieros): 

- Las personas podrían perder sus empleos debido a la automatización. 

- Las personas pueden tener demasiado (o muy poco) tiempo libre. 

- Las personas pueden perder su sentido de ser únicas. 

- Los sistemas de IA pueden ser utilizados para fines indeseables. 

- El uso de sistemas de IA puede dar lugar a una pérdida de responsabilidad. 

- El éxito de la IA podría significar el fin de la raza humana.

## **Mapa mental**

  ![Fundamentos filosóficos](https://github.com/paulisuden/ia-uncuyo-2024/commit/73c4cf904ab86c7180a6747825573b4bdb5ae9b4#diff-8fed976453cc1d1c5909b1d9f80163b988093e10f4fe23ab3f3481e016710287)

## **Opinión personal**

Básicamente, el capítulo explora de manera profunda las diferencias entre la IA débil y fuerte, destacando los desafíos filosóficos y técnicos que enfrentan estos enfoques. Mientras que la IA débil se centra en la simulación de la inteligencia sin necesariamente comprender o experimentar, la IA fuerte plantea preguntas más profundas sobre la posibilidad de que las máquinas realmente piensen o tengan estados mentales. Ambos enfoques tienen su relevancia, pero, en mi opinión, la IA débil es la más viable y aplicable en la práctica, mientras que la IA fuerte enfrenta ciertos aspectos que creo que están lejos de resolverse, como por ejemplo que una máquina tenga sentimientos o, los llamados estados mentales.

# **EJERCICIO 2**

## **1. ¿Es posible considerar a los agentes conversacionales basados en grandes modelos de lenguaje (LLMs) como conscientes?**

Los agentes conversacionales basados en LLMs no pueden considerarse conscientes en un sentido literal. Aunque estos agentes pueden simular comportamientos humanos y participar en conversaciones de manera convincente, no tienen las capacidades necesarias para ser considerados conscientes. Específicamente, carecen de un cuerpo, historia personal, y memoria autobiográfica, lo que significa que sus "intenciones" y "deseos" no son auténticos, sino simplemente simulaciones o juegos de rol. Además, el proceso de generación de texto por parte de estos modelos es estocástico y puede generar múltiples continuaciones posibles de una conversación, lo que añade una capa de exotismo a su funcionamiento interno. En conclusión, aunque pueden parecer conscientes en la superficie, su funcionamiento subyacente es fundamentalmente diferente al de una mente consciente

## **2. ¿Cuáles son las implicaciones éticas de atribuir conciencia y, por ende, "derechos morales" a los agentes de IA avanzados?**

Atribuir conciencia a los agentes de IA avanzados conlleva serias implicaciones éticas, ya que esto podría llevar a reconocerles "derechos morales". Si se llegara a considerar a un sistema de IA como un ser consciente, se le admitiría en la "comunidad de seres conscientes", lo que implicaría que deberíamos comportarnos moralmente hacia ellos. Esta atribución podría complicar la interacción con estos sistemas, ya que podría llevar a expectativas y responsabilidades que actualmente se reservan para seres conscientes, como los humanos o ciertos animales. Sin embargo, dado que los agentes basados en LLMs son simulaciones de comportamiento humano y carecen de una verdadera conciencia, tal atribución sería problemática y podría generar confusión respecto a sus capacidades reales
