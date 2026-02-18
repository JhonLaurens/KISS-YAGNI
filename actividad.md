Actividad: Principios de Diseño Aplicados – Exposición Práctica

🎯 Objetivo de la Actividad
Analizar, ejemplificar y aplicar principios de diseño de software en un contexto práctico, evidenciando cómo su correcta aplicación transforma un modelo de clases y su código asociado, mejorando la mantenibilidad, extensibilidad, simplicidad y calidad del diseño.
El propósito central de esta actividad es que los estudiantes tomen decisiones de diseño fundamentadas, comprendiendo los beneficios, costos y trade-offs asociados a cada principio, más allá de su definición teórica.

🧩 Contexto
Los principios de diseño son pilares fundamentales del desarrollo de software de calidad. No obstante, con frecuencia se abordan de forma abstracta o mediante exposiciones conceptuales. En esta actividad, los equipos deberán demostrar el valor real de los principios llevándolos a la práctica, mediante:
Modelos de clases antes y después de aplicar los principios.
Código que evidencie problemas de diseño y su posterior refactorización.
Discusión técnica sobre decisiones, compromisos y limitaciones.
Cada equipo trabajará con una pareja de principios de diseño, asignada por el docente, los cuales presentan una dificultad conceptual similar y una relación directa o complementaria.

🚫 Restricción Metodológica (Obligatoria)
Durante la exposición:
NO se permiten diapositivas teóricas ni texto explicativo proyectado.
La exposición deberá apoyarse exclusivamente en código y diagramas de clases.
La explicación será oral, guiada por los artefactos técnicos presentados.
El objetivo es que la exposición sea dinámica, técnica y práctica, centrada en el diseño y no en definiciones.

asignación:

KISS (Keep It Simple, Stupid) + YAGNI (You Aren’t Gonna Need It) (G3)

Cada pareja incluye preguntas fundamentales que deberán ser abordadas durante la exposición y la discusión. No están limitadas a las siguientes: 
1️⃣ SRP (Single Responsibility Principle) + High Cohesion (GRASP)
🟢 Responsabilidad interna y foco conceptual
Preguntas fundamentales
¿Cómo defino que una responsabilidad pertenece realmente a una clase?


¿Una clase puede tener varios métodos y seguir cumpliendo SRP?


¿Cómo se relaciona la cohesión con SRP?


¿Qué métricas ayudan a detectar violaciones?


LCOM


Número de razones de cambio


¿Qué code smells aparecen?


God Class


Large Class


Shotgun Surgery



2️⃣ DRY (Don’t Repeat Yourself) + Low Coupling (GRASP)
🟢 Duplicación vs dependencia
Preguntas fundamentales
¿Toda duplicación es mala?


¿Cuándo eliminar duplicación aumenta el acoplamiento?


¿Cómo balancear DRY sin crear clases utilitarias artificiales?


¿Qué smells indican problemas?


Duplicate Code


Feature Envy


¿Cómo evaluar acoplamiento más allá del número de dependencias?



3️⃣ OCP (Open/Closed Principle) + Polymorphism (GRASP)
🟡 Extensión controlada del comportamiento
Preguntas fundamentales
¿Qué significa “cerrado a modificación” en la práctica?


¿Cuándo el polimorfismo es excesivo?


¿Interfaces vs herencia abstracta?


¿Cómo identificar un diseño frágil ante cambios?


Switch/if por tipo


Condicionales encadenados


¿Qué impacto tiene en pruebas unitarias?



4️⃣ LSP (Liskov Substitution Principle) + ISP (Interface Segregation Principle)
🟡 Contratos correctos
Preguntas fundamentales
¿Cómo detectar una violación de LSP sin ejecutar el código?


¿Cuándo una interfaz está “gorda”?


¿LSP se rompe solo con herencia?


¿Qué señales aparecen?


Métodos no usados


Excepciones inesperadas


Condiciones especiales


¿Cómo afectan estos principios al diseño de APIs?



5️⃣ DIP (Dependency Inversion Principle) + Low Coupling (GRASP)
🟡 Dirección de dependencias
Preguntas fundamentales
¿Qué significa “depender de abstracciones” realmente?


¿Interfaces siempre son la respuesta?


¿Qué diferencia hay entre inyección y simple desacoplamiento?


¿Qué smells aparecen?


Dependencias concretas


Rigidez ante cambios tecnológicos


¿Cómo afecta el testing?



6️⃣ SoC (Separation of Concerns) + Controller (GRASP)
🟡 Organización del sistema
Preguntas fundamentales
¿Cómo identificar un concern?


¿Un controller puede crecer indefinidamente?


¿Dónde termina la lógica de negocio?


¿Qué problemas surgen si se viola SoC?


Fat Controller


Anemic Domain Model


¿Cómo se refleja SoC en el diagrama de clases?



7️⃣ KISS (Keep It Simple, Stupid) + YAGNI (You Aren’t Gonna Need It)
🟢 Complejidad innecesaria
Preguntas fundamentales
¿Cómo distinguir simplicidad de diseño pobre?


¿Cuándo una abstracción es prematura?


¿Qué señales indican sobreingeniería?


Clases sin uso


Jerarquías profundas


¿Cómo impacta YAGNI en la evolución del sistema?



8️⃣ Creator (GRASP) + SRP
🟢 Creación responsable de objetos
Preguntas fundamentales
¿Quién debe crear a quién y por qué?


¿Cómo afecta la creación a SRP?


¿Factories violan SRP?


¿Qué smells aparecen?


Demasiados new


Creación dispersa


¿Cómo se refleja esto en el modelo de clases?



9️⃣ High Cohesion (GRASP) + ISP
🟡 Interfaces alineadas con responsabilidades
Preguntas fundamentales
¿Cómo diseñar interfaces cohesionadas?


¿Cuándo dividir una interfaz?


¿Una interfaz pequeña siempre es mejor?


¿Qué problemas aparecen?


Interfaces vacías


Implementaciones forzadas


¿Cómo impacta la cohesión en mantenibilidad?



🔟 OCP + DIP
🔴 Arquitectura extensible
Preguntas fundamentales
¿Se puede cumplir OCP sin DIP?


¿Cómo fluye la dependencia en una arquitectura limpia?


¿Qué decisiones arquitectónicas emergen?


¿Qué costos reales aparecen?


Más clases


Mayor abstracción


¿En qué contextos NO vale la pena?

📦 Entregables por Equipo (Obligatorios)
Cada equipo deberá entregar:
📁 Repositorio Git
Un repositorio público o privado (con acceso al docente) que contenga:
Código antes de aplicar los principios.
Código después de la refactorización.
Diagramas de clases correspondientes a ambos estados.
Organización clara del contenido.
📄 Archivo README
El repositorio deberá incluir un README con:
Dominio elegido (ej. e-commerce, reservas, cursos, streaming, etc.).
Descripción del problema de diseño inicial.
Principios aplicados.
Decisiones de diseño relevantes y justificación breve.

🧠 Contenido Mínimo de la Exposición
Cada equipo deberá construir una mini-narrativa práctica, compuesta por:
Definición breve de los principios
Máximo 3 minutos.
Explicados con sus propias palabras, apoyándose en el código o diagramas.
Planteamiento del problema
Presentación del dominio.
Modelo de clases y código que incumplen los principios asignados.
Consecuencias del incumplimiento
Problemas de mantenibilidad, duplicación, rigidez, dificultad de prueba, etc.
Aplicación de los principios
Refactorización del modelo y del código.
Cambios en responsabilidades, dependencias y estructura.
Comparación antes vs. después
Evidencia clara y visual del impacto del rediseño.
Discusión y trade-offs
Costos del nuevo diseño.
Limitaciones.
Viabilidad en sistemas reales o de gran escala.

⏱️ Dinámica de la Sesión
Tiempo máximo por equipo: 25 minutos
15 minutos de exposición.
10 minutos de discusión, reto guiado y debate.
Cada equipo deberá formular un reto técnico a otro equipo asignado al azar.
El equipo retado deberá responder basándose en la exposición presentada.
Los demás equipos actuarán como críticos técnicos, identificando fortalezas, debilidades o inconsistencias.
El docente cerrará cada bloque conectando los principios con una visión arquitectónica más amplia.

📊 Evaluación
La evaluación se realizará con base en la siguiente rúbrica:
Criterio
Peso
Claridad del problema y de la refactorización
20%
Uso efectivo de código y diagramas de clases
20%
Coherencia y correcta aplicación de los principios
20%
Discusión técnica, defensa y trade-offs
40%

La discusión evaluará la capacidad del equipo para justificar decisiones, responder preguntas críticas, reconocer limitaciones y argumentar técnicamente.

📌 Consideraciones Finales
El repositorio es parte esencial de la evaluación.
No se evaluará la cantidad de código, sino la calidad del diseño y la claridad del razonamiento.
Se espera una actitud crítica, técnica y participativa durante toda la sesión.

