# Diagramas C4 - KISS vs Sobreingeniería

Comparación arquitectónica usando el modelo C4 (Context, Container, Component) aplicada al sistema de reservas de salas. El objetivo es visualizar cómo un mismo problema puede resolverse con dos niveles de complejidad muy distintos.

## Índice

- [Nivel 1: Contexto](#nivel-1-diagrama-de-contexto)
- [Nivel 2: Contenedores](#nivel-2-diagrama-de-contenedores)
- [Nivel 3: Componentes - Sobreingeniería](#nivel-3-diagrama-de-componentes---sobreingeniería)
- [Nivel 3: Componentes - KISS+YAGNI](#nivel-3-diagrama-de-componentes---kissyagni)
- [Comparación](#comparación-visual)

---

## Nivel 1: Diagrama de Contexto

El contexto del sistema es el mismo independientemente del enfoque de diseño.

```mermaid
C4Context
    title Diagrama de Contexto - Sistema de Reservas de Salas

    Person(usuario, "Usuario", "Empleado que necesita reservar salas de reuniones")

    System(sistema_reservas, "Sistema de Reservas", "Permite gestionar reservas de salas de reuniones")

    Rel(usuario, sistema_reservas, "Crea, consulta y cancela reservas")
```

Un empleado interactúa con el sistema para crear, consultar o cancelar reservas de salas.

---

## Nivel 2: Diagrama de Contenedores

A nivel de contenedores, ambos enfoques son idénticos: una app Python con almacenamiento en memoria.

```mermaid
C4Container
    title Diagrama de Contenedores - Sistema de Reservas

    Person(usuario, "Usuario", "Empleado")

    Container(app, "Aplicación de Reservas", "Python", "Sistema de gestión de reservas de salas")

    ContainerDb(bd, "Base de Datos", "In-Memory", "Almacena reservas y salas (simulado)")

    Rel(usuario, app, "Usa", "CLI/API")
    Rel(app, bd, "Lee/Escribe", "Datos de reservas")
```

La diferencia entre ambos enfoques no está en la infraestructura, sino en cómo se organiza internamente la lógica.

---

## Nivel 3: Diagrama de Componentes - Sobreingeniería

### Diseño Sobreingenierizado (Anti-Patrón)

Arquitectura base del enfoque sobreingenierizado:

```mermaid
graph LR
    A["Usuario"]
    B["Interfaz"]
    C["ReservMgr"]
    D["Reserva"]
    E["Sala"]
    F["BD"]

    A -->|usa| B
    B -->|gestiona| C
    C -->|crea| D
    C -->|usa| E
    C -->|persiste| F

    style A fill:#1976d2,color:#fff,stroke:#fff
    style B fill:#f57f17,color:#fff,stroke:#fff
    style C fill:#f57f17,color:#fff,stroke:#fff
    style D fill:#f57f17,color:#fff,stroke:#fff
    style E fill:#f57f17,color:#fff,stroke:#fff
    style F fill:#f57f17,color:#fff,stroke:#fff
```

Capa de servicios con abstracción innecesaria:

```mermaid
graph TB
    A["INotificationService<br/>(Interface)"]
    B["EmailService"]
    C["SMSService (no requerido)"]
    D["PushService (no requerido)"]

    A --> B
    A --> C
    A --> D

    style A fill:#c62828,color:#fff,stroke:#fff
    style C fill:#ff5252,color:#fff,stroke:#fff
    style D fill:#ff5252,color:#fff,stroke:#fff
    style B fill:#ffa726,color:#000,stroke:#fff
```

Servicios que se implementaron sin tener un requisito real:

```mermaid
graph LR
    A["PaymentGateway<br/>(las salas son gratis)"]
    B["AuditLogger<br/>(sin requisito de compliance)"]

    style A fill:#ff5252,color:#fff,stroke:#fff
    style B fill:#ff5252,color:#fff,stroke:#fff
```

**Problemas de este enfoque:**

- Se crearon 11 clases cuando el problema se resuelve con 4
- Se implementaron 3 canales de notificación (Email, SMS, Push) cuando solo Email era requisito
- Se introdujo una interfaz abstracta sin justificación técnica
- PaymentGateway para un servicio que es gratuito
- AuditLogger sin ningún requisito de compliance

| Métrica | Valor |
|---------|-------|
| Clases | 11 |
| Dependencias | 15+ |
| Líneas de código | ~500 |
| Tiempo estimado | 3 semanas |

---

## Nivel 3: Diagrama de Componentes - KISS+YAGNI

### Diseño Simple (KISS + YAGNI)

Arquitectura directa, sin capas innecesarias:

```mermaid
graph LR
    A["Usuario"]
    B["Sistema"]
    C["GestorReserv"]
    D["Reserva"]
    E["Sala"]
    F["Email"]
    G["BD"]

    A -->|usa| B
    B -->|gestiona| C
    C -->|crea| D
    C -->|usa| E
    C -->|notifica| F
    C -->|persiste| G

    style A fill:#1976d2,color:#fff,stroke:#fff
    style B fill:#2e7d32,color:#fff,stroke:#fff
    style C fill:#2e7d32,color:#fff,stroke:#fff
    style D fill:#2e7d32,color:#fff,stroke:#fff
    style E fill:#2e7d32,color:#fff,stroke:#fff
    style F fill:#2e7d32,color:#fff,stroke:#fff
    style G fill:#2e7d32,color:#fff,stroke:#fff
```

Comparación directa de complejidad:

```mermaid
graph LR
    A["Sobreingeniería<br/>11 clases, 15+ deps<br/>~500 líneas, 3 sem"]
    B["KISS+YAGNI<br/>4 clases, 5 deps<br/>~200 líneas, 1 sem"]

    style A fill:#c62828,color:#fff,stroke:#fff
    style B fill:#2e7d32,color:#fff,stroke:#fff

    A -->|vs| B
```

Con este enfoque se usan solo 4 clases, un único canal de notificación (el que realmente se necesita), sin abstracciones prematuras ni funcionalidades especulativas. El código es directo y fácil de mantener.

---

## Comparación Visual

### Tabla Comparativa

| Aspecto                     | Sobreingeniería              | KISS+YAGNI                |
| --------------------------- | ---------------------------- | ------------------------- |
| **Componentes**             | 11 clases                    | 4 clases                  |
| **Interfaces abstractas**   | 1 (innecesaria)              | 0                         |
| **Canales notificación**    | 3 (Email, SMS, Push)         | 1 (Email)                 |
| **Servicios extras**        | PaymentGateway, AuditLogger  | Ninguno                   |
| **Dependencias**            | 15+                          | 5                         |
| **Líneas de código**        | ~500 líneas                  | ~200 líneas               |
| **Tiempo desarrollo**       | 3 semanas                    | 1 semana                  |
| **Bugs potenciales**        | Alto                         | Bajo                      |
| **Facilidad mantenimiento** | Baja                         | Alta                      |
| **Extensibilidad futura**   | Difícil (mucho acoplamiento) | Fácil (bajo acoplamiento) |

### Impacto en cascada de la complejidad

```mermaid
graph LR
    A["Requisitos<br/>Simples"] -->|Sobreingeniería| C["8+ Clases<br/>Alta complejidad"]
    A -->|KISS+YAGNI| D["4 Clases<br/>Baja complejidad"]

    C --> E["Mantenimiento<br/>Costoso"]
    D --> F["Mantenimiento<br/>Fácil"]

    E --> G["Extensión<br/>Difícil"]
    F --> H["Extensión<br/>Simple"]

    style A fill:#0d47a1,color:#fff,stroke:#fff
    style C fill:#c62828,color:#fff,stroke:#fff
    style D fill:#2e7d32,color:#fff,stroke:#fff
    style E fill:#c62828,color:#fff,stroke:#fff
    style F fill:#2e7d32,color:#fff,stroke:#fff
    style G fill:#d32f2f,color:#fff,stroke:#fff
    style H fill:#388e3c,color:#fff,stroke:#fff
```

La complejidad no justificada se propaga: más código implica más mantenimiento, más bugs y más dificultad para extender.

---

## Análisis por Capa

### Notificaciones

En el diseño sobreingenierizado se creó una interfaz abstracta `INotificationService` con tres implementaciones (Email, SMS, Push), cuando el único requisito era enviar emails. Se trata de una abstracción prematura: se diseñó para un futuro que no se necesita hoy.

El enfoque simple usa una clase concreta `NotificadorEmail`. Si mañana se necesita SMS, se refactoriza en ese momento.

### Servicios Adicionales

El `PaymentGateway` se implementó asumiendo que las salas podrían cobrarse algún día. Las salas son gratis. El `AuditLogger` se añadió "por si acaso" sin que exista ningún requisito regulatorio.

En el diseño simple estos servicios no existen, porque no hay necesidad real.

---

## Principios Aplicados

### KISS - Keep It Simple, Stupid

```mermaid
graph LR
    A["Problema"] -->|Aplicar KISS| B["Solución Simple<br/>Fácil de mantener"]
    A -->|Ignorar KISS| C["Solución Compleja<br/>Difícil de mantener"]

    B --> D["Proyecto exitoso"]
    C --> E["Deuda técnica"]

    style B fill:#2e7d32,color:#fff,stroke:#fff
    style C fill:#c62828,color:#fff,stroke:#fff
    style D fill:#388e3c,color:#fff,stroke:#fff
    style E fill:#d32f2f,color:#fff,stroke:#fff
```

### YAGNI - You Aren't Gonna Need It

```mermaid
graph LR
    A["Función nueva"]
    B{"¿Es requisito<br/>documentado HOY?"}
    C{"¿Tiene 2-3<br/>casos de uso?"}
    D["Implementar"]
    E["No implementar"]
    F["Evaluar"]

    A --> B
    B -->|SÍ| C
    B -->|NO| E
    C -->|SÍ| F
    C -->|NO| E

    style D fill:#2e7d32,color:#fff,stroke:#fff
    style E fill:#ff5252,color:#fff,stroke:#fff
    style F fill:#ffa726,color:#000,stroke:#fff
```

---

## Conclusiones

El diseño simple es la opción correcta cuando los requisitos son claros y acotados: MVPs, proyectos pequeños/medianos, equipos reducidos o con restricciones de tiempo.

La complejidad adicional solo se justifica cuando hay evidencia concreta: requisitos de escalabilidad demostrados, múltiples clientes con necesidades divergentes, regulaciones estrictas o sistemas de misión crítica. Siempre con un análisis costo-beneficio que lo respalde.

> "Empieza simple. Agrega complejidad solo cuando tengas evidencia de que la necesitas."

---

## Referencias

- C4 Model: https://c4model.com/
- Martin Fowler - Software Design: https://martinfowler.com/
