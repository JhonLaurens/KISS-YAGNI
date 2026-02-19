# Actividad: KISS (Keep It Simple, Stupid) + YAGNI (You Aren't Gonna Need It)

## Historia de Contexto para la Exposición

**"El Caso de TechCorp: Cuando Menos es Más"**

Imagina que trabajas como desarrollador en TechCorp, una empresa mediana con 200 empleados. El departamento de Recursos Humanos te pide un sistema simple para reservar salas de reuniones. Actualmente usan un calendario físico en la puerta de cada sala, lo que genera conflictos y reservas duplicadas.

**Requisitos iniciales:**
- Los empleados deben poder reservar salas indicando fecha, hora y duración
- Deben poder cancelar sus propias reservas
- Deben poder consultar qué salas están disponibles

El arquitecto senior del equipo, con años de experiencia en grandes corporaciones, propone un diseño "preparado para el futuro": interfaces genéricas para diferentes tipos de reservas, integración con pasarelas de pago (por si en el futuro cobran por salas premium), soporte para múltiples canales de notificación (email, SMS, push notifications), sistema de auditoría complejo, y mucho más.

Tres meses después, el proyecto está atrasado, el código es difícil de entender incluso para el equipo, y los usuarios siguen usando el calendario físico.

Un nuevo desarrollador junior llega al equipo y pregunta: **"¿Por qué no hacemos algo simple que funcione hoy y lo mejoramos cuando sea necesario?"**

Esta historia ilustra perfectamente por qué KISS y YAGNI son fundamentales: la sobreingeniería mata proyectos, mientras que la simplicidad los hace exitosos.

---

## 1. Dominio elegido
Dominio: sistema de reservas de salas de reuniones en una empresa.

Características actuales del problema:

- Los usuarios pueden reservar salas indicando fecha, hora y duración.
- El sistema debe permitir:
  - Crear una reserva.
  - Cancelar una reserva.
  - Consultar reservas por sala o por usuario.
- No se requiere:
  - Pagos.
  - Integración con calendarios externos.
  - Múltiples empresas o múltiples monedas.
  - Módulos avanzados de auditoría, notificaciones complejas, etc.
Este dominio es adecuado para ilustrar KISS y YAGNI porque es fácil caer en sobreingeniería cuando se intenta anticipar demasiados requisitos futuros.

## 2. Diseño inicial (antes de aplicar KISS y YAGNI)
### 2.1 Idea general del diseño sobreingenierizado
El diseño inicial intenta ser genérico y extensible desde el primer momento. Introduce varias abstracciones que no responden a necesidades reales actuales, por ejemplo:

- Interfaces generales para reservas y notificaciones.
- Soporte para pagos aunque las salas sean gratuitas.
- Pasarelas de pago e integración con servicios que no se usan todavía.
- Múltiples servicios de notificación aunque solo se necesite uno.
- Clases para auditoría que no participan en ningún caso de uso real.
### 2.2 Diagrama de clases (antes)
Elementos principales:

- IReservation
  - MeetingRoomReservation implementa IReservation .
  - PaidReservation implementa IReservation (no utilizada en los escenarios actuales).
- INotificationService
  - EmailNotificationService .
  - SmsNotificationService (no utilizada).
- IPaymentGateway
  - StripePaymentGateway (no utilizada).
- ReservationManager
  - Depende de INotificationService , IPaymentGateway y IReservationRepository .
- AuditTrailService (no utilizada).
- ReservationRepository con métodos para funcionalidades que aún no existen.
### 2.3 Código representativo del diseño antes
```
public interface IReservation {
    void create();
    void cancel();
    void pay();
    void notifyUser();
}

public class MeetingRoomReservation 
implements IReservation {
    @Override
    public void create() {
        // Complex creation logic 
(placeholder)
    }

    @Override
    public void cancel() {
        // Cancel logic
    }

    @Override
    public void pay() {
        // Not really needed now, 
meeting rooms are free
    }

    @Override
    public void notifyUser() {
        // Delegates to some 
notification service
    }
}
```
```
public interface 
INotificationService {
    void sendEmail(String to, 
String content);
    void sendSms(String phone, 
String content);
}

public class 
EmailNotificationService implements 
INotificationService {
    @Override
    public void sendEmail(String 
to, String content) {
        // Send email
    }

    @Override
    public void sendSms(String 
phone, String content) {
        // Not actually supported
    }
}

public class SmsNotificationService 
implements INotificationService {
    @Override
    public void sendEmail(String 
to, String content) {
        // Not implemented
    }

    @Override
    public void sendSms(String 
phone, String content) {
        // Send SMS
    }
}
```
```
public interface IPaymentGateway {
    void charge(String customerId, 
double amount);
}

public class StripePaymentGateway 
implements IPaymentGateway {
    @Override
    public void charge(String 
customerId, double amount) {
        // Not used yet
    }
}
```
```
public class ReservationManager {

    private final 
INotificationService 
notificationService;
    private final IPaymentGateway 
paymentGateway;

    public 
ReservationManager(INotificationSer
vice notificationService,
                              
IPaymentGateway paymentGateway) {
        this.notificationService = 
notificationService;
        this.paymentGateway = 
paymentGateway;
    }

    public void 
createReservation(IReservation 
reservation) {
        reservation.create();
        // Over-engineered: payment 
although rooms are free
        reservation.pay();
        reservation.notifyUser();
    }
}
```
### 2.4 Problemas detectados
Relación con KISS:

- El diseño es innecesariamente complejo para los requisitos actuales.
- Se introducen jerarquías y generalizaciones sin un beneficio claro.
- El código es más difícil de leer, mantener y probar.
Relación con YAGNI:

- Se implementa soporte para pagos sin que exista un requerimiento actual.
- Se define infraestructura para múltiples canales de notificación sin usarlos.
- Se mantienen clases y métodos que no participan en ningún flujo de negocio real.
Señales de sobreingeniería:

- Clases sin uso efectivo.
- Métodos vacíos o con comentarios tipo "Not implemented yet".
- Jerarquías profundas para casos de uso muy simples.
- Interfaces con métodos que no aplican a todas las implementaciones.
## 3. Diseño refactorizado (después de aplicar KISS y YAGNI)
### 3.1 Objetivo del rediseño
- Mantener solo lo que el dominio necesita hoy.
- Eliminar abstracciones y funcionalidades que no están soportando requisitos reales.
- Hacer el diseño más fácil de entender, extender y probar cuando surjan nuevos requisitos.
### 3.2 Diagrama de clases (después)
Elementos principales:

- MeetingRoomReservation .
- ReservationService .
- ReservationRepository .
- EmailNotifier (solo si realmente se usa en los casos de uso actuales).
No existen ahora:

- IPaymentGateway ni StripePaymentGateway .
- Interfaces genéricas sin necesidad clara.
- Implementaciones de notificación que no se utilizan.
- Clases de auditoría sin rol claro en los casos de uso.
### 3.3 Código representativo del diseño después
```
public class MeetingRoomReservation 
{

    private final String roomId;
    private final String userId;
    private final String startTime;
    private final String endTime;

    public 
MeetingRoomReservation(String 
roomId, String userId, String 
startTime, String endTime) {
        this.roomId = roomId;
        this.userId = userId;
        this.startTime = startTime;
        this.endTime = endTime;
    }

    public String getRoomId() {
        return roomId;
    }

    public String getUserId() {
        return userId;
    }

    public String getStartTime() {
        return startTime;
    }

    public String getEndTime() {
        return endTime;
    }
}
```
```
public class ReservationService {

    private final 
ReservationRepository repository;
    private final EmailNotifier 
notifier;

    public 
ReservationService(ReservationRepos
itory repository, EmailNotifier 
notifier) {
        this.repository = 
repository;
        this.notifier = notifier;
    }

    public void 
createReservation(MeetingRoomReserv
ation reservation) {
        
repository.save(reservation);
        
notifier.notifyUser(reservation.get
UserId(), "Reservation created");
    }

    public void 
cancelReservation(String 
reservationId) {
        
repository.delete(reservationId);
    }
}
```
```
public class ReservationRepository 
{

    public void 
save(MeetingRoomReservation 
reservation) {
        // Persist reservation
    }

    public void delete(String 
reservationId) {
        // Delete reservation
    }
}
```
```
public class EmailNotifier {

    public void notifyUser(String 
userId, String message) {
        // Simple email logic
    }
}
```
### 3.4 Cómo se aplican KISS y YAGNI
Aplicación de KISS:

- Clases pequeñas y con responsabilidades claras.
- Diseño directo, sin jerarquías innecesarias.
- El código se lee casi de forma narrativa: crear reserva, guardar, notificar.
Aplicación de YAGNI:

- No se implementan pagos ni pasarelas de pago mientras no sean necesarios.
- No se soportan múltiples canales de notificación hasta que un requisito lo exija.
- No se crean interfaces genéricas con una sola implementación y sin variación prevista.
## 4. Respuestas a las preguntas fundamentales de la actividad
### 4.1 ¿Cómo distinguir simplicidad de diseño pobre?
Simplicidad:

- Resuelve los casos de uso reales de manera clara y directa.
- Mantiene modelos de dominio significativos.
- Permite extensión razonable cuando aparecen nuevos requisitos.
Diseño pobre:

- Mezcla responsabilidades sin un modelo claro.
- Tiene nombres poco expresivos y falta de encapsulamiento.
- No soporta cambios razonables sin reescrituras masivas.
En este ejemplo, el diseño refactorizado es simple pero no pobre: separa entidad de dominio ( MeetingRoomReservation ), lógica de aplicación ( ReservationService ) y persistencia ( ReservationRepository ).

### 4.2 ¿Cuándo una abstracción es prematura?
Una abstracción es prematura cuando:

- No existe aún un requisito real que la justifique.
- No hay variación concreta que requiera generalización.
- Se crea "por si acaso" pensando en escenarios hipotéticos.
En el diseño inicial, IPaymentGateway , IReservation y INotificationService son ejemplos de abstracciones prematuras: no hay múltiples pasarelas de pago, ni múltiples tipos de reservas con comportamiento distinto, ni una necesidad real de soportar varios canales de notificación.

### 4.3 ¿Qué señales indican sobreingeniería?
Señales típicas:

- Clases sin uso en ningún flujo real.
- Métodos que nunca se invocan o que están vacíos.
- Jerarquías de herencia profundas para problemas sencillos.
- Interfaces que agrupan demasiadas responsabilidades o no tienen más de una implementación real.
En el diseño inicial se observan varias de estas señales, por ejemplo StripePaymentGateway y PaidReservation , que no participan en los casos de uso actuales.

### 4.4 ¿Cómo impacta YAGNI en la evolución del sistema?
Impactos de YAGNI:

- Obliga a diseñar guiado por requisitos reales y no por especulación.
- Reduce el costo de mantenimiento al evitar código que no aporta valor.
- Permite que el diseño crezca de forma orgánica:
  - Cuando aparezca un requisito de pagos, se introducirá un componente de pagos basado en necesidades claras.
  - Si en el futuro se requieren múltiples canales de notificación, se podrá introducir una abstracción adecuada en ese momento.
YAGNI no significa "no pensar en el futuro", sino evitar pagar hoy el coste de funcionalidades cuyo valor es incierto.

## 5. Estructura sugerida de la exposición
Duración total: 15 minutos de exposición.

1. Introducción y definiciones breves (aprox. 3 minutos)
   
   - Explicar KISS y YAGNI con sus propias palabras.
   - Introducir el dominio de reservas de salas.
   - Conectar inmediatamente con un ejemplo del código.
2. Presentación del problema y diseño inicial (aprox. 4 minutos)
   
   - Mostrar el diagrama de clases inicial.
   - Enseñar el código sobreingenierizado.
   - Identificar explícitamente violaciones de KISS y YAGNI.
3. Refactorización y diseño final (aprox. 5 minutos)
   
   - Mostrar el diagrama de clases final.
   - Recorrer el código sencillo.
   - Explicar qué se eliminó y por qué, alineándolo con YAGNI.
   - Justificar cómo la simplicidad mejora claridad y mantenibilidad (KISS).
4. Comparación, trade-offs y discusión (aprox. 3 minutos)
   
   - Comparar antes vs. después en términos de:
     - Complejidad.
     - Facilidad de pruebas.
     - Facilidad para introducir futuros cambios.
   - Mencionar posibles costos del diseño actual si en el futuro se requiere mucha extensibilidad, y cómo se abordaría llegado ese momento.