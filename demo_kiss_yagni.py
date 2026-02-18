#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Reservas de Salas - Demostración KISS y YAGNI
=========================================================

Este script demuestra los principios KISS (Keep It Simple, Stupid) y 
YAGNI (You Aren't Gonna Need It) mediante dos implementaciones del mismo 
sistema de reservas de salas:

1. VERSIÓN SOBREINGENIERIZADA: Con abstracciones innecesarias y funcionalidades no requeridas
2. VERSIÓN KISS+YAGNI: Simple, directa y enfocada en los requisitos actuales

Autor: Demo para exposición de Arquitectura de Software
Fecha: 2026-02-17
"""

from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import json


# ==============================================================================
# PARTE 1: DISEÑO SOBREINGENIERIZADO (ANTI-PATRÓN)
# ==============================================================================
print("=" * 80)
print("PARTE 1: DISEÑO SOBREINGENIERIZADO - Violando KISS y YAGNI")
print("=" * 80)


# Interfaz genérica innecesaria (YAGNI violation)
class IReservation(ABC):
    """Interfaz genérica para reservas - INNECESARIA para nuestro caso simple"""
    
    @abstractmethod
    def create(self) -> bool:
        """Crear la reserva"""
        pass
    
    @abstractmethod
    def cancel(self) -> bool:
        """Cancelar la reserva"""
        pass
    
    @abstractmethod
    def pay(self) -> bool:
        """Procesar pago - NO NECESITAMOS ESTO AÚN"""
        pass
    
    @abstractmethod
    def notify_user(self) -> None:
        """Notificar al usuario"""
        pass


# Múltiples interfaces de notificación que no usamos (YAGNI violation)
class INotificationService(ABC):
    """Interfaz para servicios de notificación - Demasiado genérica"""
    
    @abstractmethod
    def send_email(self, to: str, content: str) -> bool:
        pass
    
    @abstractmethod
    def send_sms(self, phone: str, content: str) -> bool:
        pass
    
    @abstractmethod
    def send_push(self, user_id: str, content: str) -> bool:
        pass


class EmailNotificationService(INotificationService):
    """Servicio de email con métodos que no implementa"""
    
    def send_email(self, to: str, content: str) -> bool:
        print(f"📧 Email enviado a {to}: {content}")
        return True
    
    def send_sms(self, phone: str, content: str) -> bool:
        # Método no soportado pero requerido por la interfaz
        raise NotImplementedError("SMS no está implementado en EmailNotificationService")
    
    def send_push(self, user_id: str, content: str) -> bool:
        # Método no soportado pero requerido por la interfaz
        raise NotImplementedError("Push no está implementado en EmailNotificationService")


# Pasarela de pago que NO NECESITAMOS (YAGNI violation)
class IPaymentGateway(ABC):
    """Interfaz para pasarelas de pago - NO LA NECESITAMOS AÚN"""
    
    @abstractmethod
    def charge(self, customer_id: str, amount: float) -> bool:
        pass


class StripePaymentGateway(IPaymentGateway):
    """Implementación de Stripe que nunca usamos"""
    
    def charge(self, customer_id: str, amount: float) -> bool:
        # Esta funcionalidad no se usa porque las salas son gratuitas
        print(f"💳 Cargo de ${amount} procesado para cliente {customer_id}")
        return True


# Implementación compleja de reserva (KISS violation)
class MeetingRoomReservationComplex(IReservation):
    """Reserva de sala con complejidad innecesaria"""
    
    def __init__(self, room_id: str, user_id: str, start_time: str, end_time: str,
                 notification_service: INotificationService,
                 payment_gateway: IPaymentGateway):
        self.room_id = room_id
        self.user_id = user_id
        self.start_time = start_time
        self.end_time = end_time
        self.notification_service = notification_service
        self.payment_gateway = payment_gateway
        self.is_paid = False
        self.is_created = False
    
    def create(self) -> bool:
        """Proceso de creación excesivamente complejo"""
        try:
            # Validaciones innecesariamente complejas
            if not self._validate_complex():
                return False
            
            self.is_created = True
            print(f"✅ Reserva compleja creada: Sala {self.room_id} para usuario {self.user_id}")
            return True
        except Exception as e:
            print(f"❌ Error en creación compleja: {e}")
            return False
    
    def _validate_complex(self) -> bool:
        """Validación con lógica innecesariamente compleja"""
        # Múltiples niveles de validación que podrían ser más simples
        if not self.room_id or not self.user_id:
            return False
        if not self.start_time or not self.end_time:
            return False
        return True
    
    def cancel(self) -> bool:
        """Cancelación con lógica compleja"""
        if not self.is_created:
            return False
        self.is_created = False
        print(f"🚫 Reserva compleja cancelada: Sala {self.room_id}")
        return True
    
    def pay(self) -> bool:
        """Procesar pago - INNECESARIO porque las salas son gratuitas"""
        # Esta funcionalidad no se necesita pero está implementada "por si acaso"
        try:
            self.payment_gateway.charge(self.user_id, 0.0)
            self.is_paid = True
            return True
        except Exception as e:
            print(f"❌ Error en pago: {e}")
            return False
    
    def notify_user(self) -> None:
        """Notificación con dependencia compleja"""
        try:
            self.notification_service.send_email(
                self.user_id, 
                f"Reserva de sala {self.room_id}"
            )
        except Exception as e:
            print(f"❌ Error en notificación: {e}")


# Manager con demasiadas dependencias (KISS violation)
class ReservationManagerComplex:
    """Manager sobreingenierizado con dependencias innecesarias"""
    
    def __init__(self, notification_service: INotificationService,
                 payment_gateway: IPaymentGateway):
        self.notification_service = notification_service
        self.payment_gateway = payment_gateway
        self.reservations: List[IReservation] = []
    
    def create_reservation(self, reservation: IReservation) -> bool:
        """Proceso de creación con pasos innecesarios"""
        try:
            # Paso 1: Crear
            if not reservation.create():
                return False
            
            # Paso 2: Pagar (INNECESARIO - las salas son gratuitas)
            reservation.pay()
            
            # Paso 3: Notificar
            reservation.notify_user()
            
            # Paso 4: Guardar
            self.reservations.append(reservation)
            
            return True
        except Exception as e:
            print(f"❌ Error en manager complejo: {e}")
            return False


# ==============================================================================
# DEMOSTRACIÓN DEL DISEÑO SOBREINGENIERIZADO
# ==============================================================================
print("\n--- Demostración del Diseño Sobreingenierizado ---")
print("Nota: Observa la complejidad innecesaria y las dependencias que no se usan\n")

try:
    # Crear servicios que en realidad no necesitamos todos
    email_service = EmailNotificationService()
    payment_gateway = StripePaymentGateway()
    
    # Manager con demasiadas dependencias
    manager_complex = ReservationManagerComplex(email_service, payment_gateway)
    
    # Crear una reserva con todas las dependencias innecesarias
    reservation_complex = MeetingRoomReservationComplex(
        room_id="Sala-A",
        user_id="juan.perez@techcorp.com",
        start_time="2026-02-18 10:00",
        end_time="2026-02-18 11:00",
        notification_service=email_service,
        payment_gateway=payment_gateway
    )
    
    # Proceso complejo de creación
    if manager_complex.create_reservation(reservation_complex):
        print("✅ Proceso complejo completado")
    
    print(f"\n📊 Total de reservas complejas: {len(manager_complex.reservations)}")
    
except Exception as e:
    print(f"❌ Error en demostración compleja: {e}")


print("\n" + "=" * 80)
print("PROBLEMAS IDENTIFICADOS EN EL DISEÑO SOBREINGENIERIZADO:")
print("=" * 80)
print("""
1. ❌ Interfaces genéricas sin necesidad real (IReservation, INotificationService)
2. ❌ Funcionalidades no requeridas (pagos, SMS, push notifications)
3. ❌ Dependencias innecesarias (PaymentGateway en un sistema gratuito)
4. ❌ Complejidad que dificulta el mantenimiento
5. ❌ Métodos no implementados que lanzan excepciones
6. ❌ Código difícil de probar y extender
7. ❌ Violación de YAGNI: "You Aren't Gonna Need It"
8. ❌ Violación de KISS: "Keep It Simple, Stupid"
""")


# ==============================================================================
# PARTE 2: DISEÑO SIMPLE - APLICANDO KISS Y YAGNI
# ==============================================================================
print("\n" + "=" * 80)
print("PARTE 2: DISEÑO SIMPLE - Aplicando KISS y YAGNI")
print("=" * 80)


class MeetingRoomReservation:
    """
    Reserva de sala de reuniones - Clase simple con solo lo necesario
    
    Aplica KISS: Estructura simple y directa
    Aplica YAGNI: Solo tiene lo que necesitamos HOY
    """
    
    def __init__(self, room_id: str, user_id: str, start_time: str, 
                 end_time: str, user_name: str = ""):
        """
        Inicializar una reserva con la información mínima necesaria
        
        Args:
            room_id: Identificador de la sala
            user_id: Email o ID del usuario
            start_time: Hora de inicio (formato: "YYYY-MM-DD HH:MM")
            end_time: Hora de fin (formato: "YYYY-MM-DD HH:MM")
            user_name: Nombre del usuario (opcional)
        """
        self.room_id = room_id
        self.user_id = user_id
        self.start_time = start_time
        self.end_time = end_time
        self.user_name = user_name or user_id
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def __str__(self) -> str:
        """Representación legible de la reserva"""
        return (f"🏢 Sala: {self.room_id} | "
                f"👤 Usuario: {self.user_name} | "
                f"🕐 {self.start_time} - {self.end_time}")
    
    def to_dict(self) -> Dict:
        """Convertir a diccionario para fácil serialización"""
        return {
            'room_id': self.room_id,
            'user_id': self.user_id,
            'user_name': self.user_name,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'created_at': self.created_at
        }


class EmailNotifier:
    """
    Notificador de email simple - Solo hace lo que necesitamos
    
    Aplica KISS: Una clase, una responsabilidad clara
    Aplica YAGNI: Solo email, sin SMS ni push (no los necesitamos aún)
    """
    
    def notify_user(self, user_id: str, message: str) -> bool:
        """
        Enviar notificación por email
        
        Args:
            user_id: Email del usuario
            message: Mensaje a enviar
            
        Returns:
            True si se envió correctamente
        """
        try:
            # En producción, aquí iría la lógica real de envío
            print(f"📧 Email enviado a {user_id}")
            print(f"   Mensaje: {message}")
            return True
        except Exception as e:
            print(f"❌ Error al enviar email: {e}")
            return False


class ReservationRepository:
    """
    Repositorio simple para almacenar reservas - En memoria por simplicidad
    
    Aplica KISS: Implementación directa sin ORM complejo
    Aplica YAGNI: Almacenamiento en memoria (suficiente para la demo)
    """
    
    def __init__(self):
        """Inicializar repositorio vacío"""
        self.reservations: List[MeetingRoomReservation] = []
    
    def save(self, reservation: MeetingRoomReservation) -> bool:
        """
        Guardar una reserva
        
        Args:
            reservation: Objeto de reserva a guardar
            
        Returns:
            True si se guardó correctamente
        """
        try:
            self.reservations.append(reservation)
            print(f"💾 Reserva guardada: {reservation}")
            return True
        except Exception as e:
            print(f"❌ Error al guardar: {e}")
            return False
    
    def delete(self, room_id: str, user_id: str) -> bool:
        """
        Eliminar una reserva específica
        
        Args:
            room_id: ID de la sala
            user_id: ID del usuario
            
        Returns:
            True si se eliminó correctamente
        """
        try:
            initial_count = len(self.reservations)
            self.reservations = [
                r for r in self.reservations 
                if not (r.room_id == room_id and r.user_id == user_id)
            ]
            deleted = initial_count > len(self.reservations)
            
            if deleted:
                print(f"🗑️  Reserva eliminada: Sala {room_id}, Usuario {user_id}")
            else:
                print(f"⚠️  No se encontró la reserva para eliminar")
            
            return deleted
        except Exception as e:
            print(f"❌ Error al eliminar: {e}")
            return False
    
    def find_by_room(self, room_id: str) -> List[MeetingRoomReservation]:
        """
        Buscar reservas por sala
        
        Args:
            room_id: ID de la sala
            
        Returns:
            Lista de reservas de esa sala
        """
        return [r for r in self.reservations if r.room_id == room_id]
    
    def find_by_user(self, user_id: str) -> List[MeetingRoomReservation]:
        """
        Buscar reservas por usuario
        
        Args:
            user_id: ID del usuario
            
        Returns:
            Lista de reservas de ese usuario
        """
        return [r for r in self.reservations if r.user_id == user_id]
    
    def get_all(self) -> List[MeetingRoomReservation]:
        """Obtener todas las reservas"""
        return self.reservations.copy()


class ReservationService:
    """
    Servicio de reservas - Coordinador simple
    
    Aplica KISS: Lógica clara y fácil de seguir
    Aplica YAGNI: Solo operaciones necesarias (crear, cancelar, consultar)
    """
    
    def __init__(self, repository: ReservationRepository, 
                 notifier: EmailNotifier):
        """
        Inicializar servicio con dependencias mínimas
        
        Args:
            repository: Repositorio para persistencia
            notifier: Notificador para emails
        """
        self.repository = repository
        self.notifier = notifier
    
    def create_reservation(self, room_id: str, user_id: str, 
                          start_time: str, end_time: str,
                          user_name: str = "") -> bool:
        """
        Crear una nueva reserva
        
        Args:
            room_id: ID de la sala
            user_id: Email/ID del usuario
            start_time: Hora de inicio
            end_time: Hora de fin
            user_name: Nombre del usuario (opcional)
            
        Returns:
            True si se creó correctamente
        """
        try:
            # Validación simple
            if not all([room_id, user_id, start_time, end_time]):
                print("❌ Error: Faltan datos requeridos")
                return False
            
            # Crear reserva
            reservation = MeetingRoomReservation(
                room_id, user_id, start_time, end_time, user_name
            )
            
            # Guardar
            if not self.repository.save(reservation):
                return False
            
            # Notificar
            self.notifier.notify_user(
                user_id,
                f"Tu reserva de {room_id} está confirmada para {start_time}"
            )
            
            return True
            
        except Exception as e:
            print(f"❌ Error al crear reserva: {e}")
            return False
    
    def cancel_reservation(self, room_id: str, user_id: str) -> bool:
        """
        Cancelar una reserva
        
        Args:
            room_id: ID de la sala
            user_id: ID del usuario
            
        Returns:
            True si se canceló correctamente
        """
        try:
            if self.repository.delete(room_id, user_id):
                self.notifier.notify_user(
                    user_id,
                    f"Tu reserva de {room_id} ha sido cancelada"
                )
                return True
            return False
        except Exception as e:
            print(f"❌ Error al cancelar reserva: {e}")
            return False
    
    def get_room_reservations(self, room_id: str) -> List[MeetingRoomReservation]:
        """Obtener reservas de una sala específica"""
        return self.repository.find_by_room(room_id)
    
    def get_user_reservations(self, user_id: str) -> List[MeetingRoomReservation]:
        """Obtener reservas de un usuario específico"""
        return self.repository.find_by_user(user_id)
    
    def get_all_reservations(self) -> List[MeetingRoomReservation]:
        """Obtener todas las reservas"""
        return self.repository.get_all()


# ==============================================================================
# DEMOSTRACIÓN DEL DISEÑO SIMPLE
# ==============================================================================
print("\n--- Demostración del Diseño Simple ---")
print("Nota: Observa la claridad y simplicidad del código\n")

# Inicializar componentes
repository = ReservationRepository()
notifier = EmailNotifier()
service = ReservationService(repository, notifier)

# Crear varias reservas
print("\n🔹 CREANDO RESERVAS:")
print("-" * 80)

reservas_demo = [
    ("Sala-A", "juan.perez@techcorp.com", "2026-02-18 09:00", "2026-02-18 10:00", "Juan Pérez"),
    ("Sala-B", "maria.garcia@techcorp.com", "2026-02-18 10:00", "2026-02-18 11:30", "María García"),
    ("Sala-A", "carlos.lopez@techcorp.com", "2026-02-18 14:00", "2026-02-18 15:00", "Carlos López"),
    ("Sala-C", "ana.martinez@techcorp.com", "2026-02-18 11:00", "2026-02-18 12:00", "Ana Martínez"),
]

for room, user, start, end, name in reservas_demo:
    service.create_reservation(room, user, start, end, name)
    print()

# Consultar reservas por sala
print("\n🔹 CONSULTANDO RESERVAS POR SALA:")
print("-" * 80)
sala_a_reservations = service.get_room_reservations("Sala-A")
print(f"\n📍 Sala-A tiene {len(sala_a_reservations)} reserva(s):")
for res in sala_a_reservations:
    print(f"   {res}")

# Consultar reservas por usuario
print("\n🔹 CONSULTANDO RESERVAS POR USUARIO:")
print("-" * 80)
user_reservations = service.get_user_reservations("juan.perez@techcorp.com")
print(f"\n👤 Juan Pérez tiene {len(user_reservations)} reserva(s):")
for res in user_reservations:
    print(f"   {res}")

# Cancelar una reserva
print("\n🔹 CANCELANDO UNA RESERVA:")
print("-" * 80)
service.cancel_reservation("Sala-A", "juan.perez@techcorp.com")

# Mostrar todas las reservas restantes
print("\n🔹 RESUMEN FINAL DE TODAS LAS RESERVAS:")
print("-" * 80)
all_reservations = service.get_all_reservations()
print(f"\n📊 Total de reservas activas: {len(all_reservations)}")
for res in all_reservations:
    print(f"   {res}")


# ==============================================================================
# COMPARACIÓN VISUAL FINAL
# ==============================================================================
print("\n\n" + "=" * 80)
print("COMPARACIÓN: SOBREINGENIERIZADO vs SIMPLE (KISS + YAGNI)")
print("=" * 80)

comparison_table = """
┌─────────────────────────────┬─────────────────────────┬──────────────────────────┐
│ ASPECTO                     │ DISEÑO SOBREINGENIERIZADO │ DISEÑO SIMPLE (KISS+YAGNI)│
├─────────────────────────────┼─────────────────────────┼──────────────────────────┤
│ Número de clases            │ 8+ clases               │ 4 clases                 │
│ Interfaces abstractas       │ 3 interfaces            │ 0 interfaces             │
│ Líneas de código            │ ~200+ líneas            │ ~150 líneas              │
│ Dependencias por clase      │ 3-4 dependencias        │ 1-2 dependencias         │
│ Funcionalidad no usada      │ Pagos, SMS, Push        │ Ninguna                  │
│ Complejidad de pruebas      │ Alta (muchos mocks)     │ Baja (simple)            │
│ Tiempo de desarrollo        │ 3 semanas               │ 1 semana                 │
│ Facilidad de mantenimiento  │ Baja                    │ Alta                     │
│ Legibilidad del código      │ Difícil                 │ Fácil                    │
│ Facilidad de extensión      │ Media-Baja              │ Alta                     │
└─────────────────────────────┴─────────────────────────┴──────────────────────────┘
"""

print(comparison_table)

print("\n" + "=" * 80)
print("BENEFICIOS DE APLICAR KISS Y YAGNI")
print("=" * 80)
print("""
✅ KISS (Keep It Simple, Stupid):
   • Código más fácil de leer y entender
   • Menos bugs por menor complejidad
   • Onboarding más rápido para nuevos desarrolladores
   • Mantenimiento más sencillo

✅ YAGNI (You Aren't Gonna Need It):
   • Desarrollo más rápido (solo lo necesario)
   • Menos código que mantener
   • Menor superficie de bugs
   • Flexibilidad para cambiar cuando realmente se necesite

✅ Resultado:
   • Sistema funcional en menos tiempo
   • Costo de desarrollo reducido
   • Mayor satisfacción del cliente
   • Equipo más productivo
""")

print("\n" + "=" * 80)
print("¿CUÁNDO AGREGAR COMPLEJIDAD?")
print("=" * 80)
print("""
Agrega abstracciones y funcionalidades SOLO cuando:

1. 📋 Existe un requisito REAL y documentado
2. 🔄 Ya tienes al menos 2-3 casos de uso concretos
3. 💰 El costo de no tenerlo es mayor que el costo de implementarlo
4. 📊 Tienes datos que justifican la inversión

Ejemplo para este sistema:
• ¿Agregar pagos? → Cuando tengas salas premium de pago
• ¿Agregar SMS? → Cuando los usuarios lo soliciten activamente
• ¿Agregar auditoría? → Cuando sea requisito de compliance

RECUERDA: Es más fácil agregar complejidad cuando se necesita,
que eliminar complejidad innecesaria.
""")

print("\n" + "=" * 80)
print("FIN DE LA DEMOSTRACIÓN")
print("=" * 80)
print("\n💡 Preguntas para discusión:")
print("   1. ¿Qué otras funcionalidades innecesarias has visto en proyectos reales?")
print("   2. ¿Cómo balanceas simplicidad con preparación para el futuro?")
print("   3. ¿Cuándo está justificado un diseño más complejo desde el inicio?")
print("\n")
