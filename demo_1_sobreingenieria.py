#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Reservas de Salas - DISEÑO SOBREINGENIERIZADO
==========================================================

Este script demuestra un diseño que VIOLA los principios KISS y YAGNI:
- Abstracciones innecesarias
- Funcionalidades no requeridas
- Complejidad excesiva

⚠️ ANTI-PATRÓN - NO SEGUIR ESTE DISEÑO ⚠️

Autor: Demo para exposición de Arquitectura de Software
Fecha: 2026-02-17
"""

from abc import ABC, abstractmethod
from typing import List


print("=" * 80)
print("DISEÑO SOBREINGENIERIZADO - Violando KISS y YAGNI")
print("=" * 80)
print("\n⚠️  ADVERTENCIA: Este es un ANTI-PATRÓN educativo\n")


# ==============================================================================
# INTERFACES GENÉRICAS INNECESARIAS (YAGNI violation)
# ==============================================================================

class IReservation(ABC):
    """
    Interfaz genérica para reservas - INNECESARIA para nuestro caso simple
    
    Problema: Solo tenemos un tipo de reserva, no necesitamos abstracción
    """
    
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


class INotificationService(ABC):
    """
    Interfaz para servicios de notificación - Demasiado genérica
    
    Problema: Solo usamos email, pero forzamos implementar SMS y Push
    """
    
    @abstractmethod
    def send_email(self, to: str, content: str) -> bool:
        pass
    
    @abstractmethod
    def send_sms(self, phone: str, content: str) -> bool:
        pass
    
    @abstractmethod
    def send_push(self, user_id: str, content: str) -> bool:
        pass


class IPaymentGateway(ABC):
    """
    Interfaz para pasarelas de pago - NO LA NECESITAMOS AÚN
    
    Problema: Las salas son gratuitas, esto es pura especulación
    """
    
    @abstractmethod
    def charge(self, customer_id: str, amount: float) -> bool:
        pass


# ==============================================================================
# IMPLEMENTACIONES COMPLEJAS E INNECESARIAS
# ==============================================================================

class EmailNotificationService(INotificationService):
    """
    Servicio de email con métodos que no implementa
    
    Problema: La interfaz obliga a implementar métodos que no usamos
    """
    
    def send_email(self, to: str, content: str) -> bool:
        print(f"📧 Email enviado a {to}: {content}")
        return True
    
    def send_sms(self, phone: str, content: str) -> bool:
        # Método no soportado pero requerido por la interfaz
        raise NotImplementedError("❌ SMS no está implementado en EmailNotificationService")
    
    def send_push(self, user_id: str, content: str) -> bool:
        # Método no soportado pero requerido por la interfaz
        raise NotImplementedError("❌ Push no está implementado en EmailNotificationService")


class SmsNotificationService(INotificationService):
    """
    Servicio SMS que nunca usamos
    
    Problema: Código muerto que solo agrega complejidad
    """
    
    def send_email(self, to: str, content: str) -> bool:
        raise NotImplementedError("❌ Email no está implementado en SmsNotificationService")
    
    def send_sms(self, phone: str, content: str) -> bool:
        print(f"📱 SMS enviado a {phone}: {content}")
        return True
    
    def send_push(self, user_id: str, content: str) -> bool:
        raise NotImplementedError("❌ Push no está implementado en SmsNotificationService")


class StripePaymentGateway(IPaymentGateway):
    """
    Implementación de Stripe que nunca usamos
    
    Problema: Las salas son gratuitas, esto es YAGNI puro
    """
    
    def charge(self, customer_id: str, amount: float) -> bool:
        # Esta funcionalidad no se usa porque las salas son gratuitas
        print(f"💳 Cargo de ${amount} procesado para cliente {customer_id}")
        return True


class MeetingRoomReservationComplex(IReservation):
    """
    Reserva de sala con complejidad innecesaria
    
    Problemas:
    - Demasiadas dependencias
    - Lógica de validación excesivamente compleja
    - Métodos que no se necesitan (pay)
    """
    
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
                print("❌ Validación compleja falló")
                return False
            
            # Proceso de creación con múltiples pasos innecesarios
            if not self._pre_create_hook():
                return False
            
            self.is_created = True
            print(f"✅ Reserva compleja creada: Sala {self.room_id} para usuario {self.user_id}")
            
            self._post_create_hook()
            return True
            
        except Exception as e:
            print(f"❌ Error en creación compleja: {e}")
            return False
    
    def _validate_complex(self) -> bool:
        """
        Validación con lógica innecesariamente compleja
        
        Problema: Podría ser una simple validación de 2 líneas
        """
        # Múltiples niveles de validación que podrían ser más simples
        if not self._validate_ids():
            return False
        if not self._validate_times():
            return False
        if not self._validate_services():
            return False
        return True
    
    def _validate_ids(self) -> bool:
        """Validación de IDs separada innecesariamente"""
        return bool(self.room_id and self.user_id)
    
    def _validate_times(self) -> bool:
        """Validación de tiempos separada innecesariamente"""
        return bool(self.start_time and self.end_time)
    
    def _validate_services(self) -> bool:
        """Validación de servicios que no necesitamos validar"""
        return bool(self.notification_service and self.payment_gateway)
    
    def _pre_create_hook(self) -> bool:
        """Hook innecesario 'por si acaso' se necesita en el futuro"""
        # No hace nada real pero agrega complejidad
        return True
    
    def _post_create_hook(self) -> None:
        """Otro hook innecesario 'por si acaso'"""
        # No hace nada real pero agrega complejidad
        pass
    
    def cancel(self) -> bool:
        """Cancelación con lógica compleja"""
        if not self.is_created:
            print("❌ No se puede cancelar una reserva no creada")
            return False
        
        # Proceso complejo de cancelación
        if not self._pre_cancel_hook():
            return False
        
        self.is_created = False
        print(f"🚫 Reserva compleja cancelada: Sala {self.room_id}")
        
        self._post_cancel_hook()
        return True
    
    def _pre_cancel_hook(self) -> bool:
        """Hook innecesario para cancelación"""
        return True
    
    def _post_cancel_hook(self) -> None:
        """Otro hook innecesario para cancelación"""
        pass
    
    def pay(self) -> bool:
        """
        Procesar pago - INNECESARIO porque las salas son gratuitas
        
        Problema: Funcionalidad especulativa que no se necesita
        """
        try:
            if self.is_paid:
                print("⚠️  Ya está pagado")
                return True
            
            # Proceso de pago innecesario
            self.payment_gateway.charge(self.user_id, 0.0)
            self.is_paid = True
            print("💳 Pago procesado (aunque sea $0)")
            return True
            
        except Exception as e:
            print(f"❌ Error en pago: {e}")
            return False
    
    def notify_user(self) -> None:
        """Notificación con dependencia compleja"""
        try:
            self.notification_service.send_email(
                self.user_id, 
                f"Reserva de sala {self.room_id} desde {self.start_time}"
            )
        except Exception as e:
            print(f"❌ Error en notificación: {e}")


class ReservationManagerComplex:
    """
    Manager sobreingenierizado con dependencias innecesarias
    
    Problemas:
    - Demasiadas dependencias inyectadas
    - Proceso de creación con pasos innecesarios
    - Lógica que podría estar en un servicio simple
    """
    
    def __init__(self, notification_service: INotificationService,
                 payment_gateway: IPaymentGateway):
        self.notification_service = notification_service
        self.payment_gateway = payment_gateway
        self.reservations: List[IReservation] = []
        self.audit_trail: List[str] = []  # Auditoría que no usamos
    
    def create_reservation(self, reservation: IReservation) -> bool:
        """
        Proceso de creación con pasos innecesarios
        
        Problema: Flujo complejo para algo simple
        """
        try:
            # Log innecesario
            self._log_audit("Iniciando creación de reserva")
            
            # Paso 1: Crear
            if not reservation.create():
                self._log_audit("Error en creación")
                return False
            
            # Paso 2: Pagar (INNECESARIO - las salas son gratuitas)
            if not reservation.pay():
                self._log_audit("Error en pago")
                # Continuamos aunque falle el pago (porque no lo necesitamos)
            
            # Paso 3: Notificar
            reservation.notify_user()
            
            # Paso 4: Guardar
            self.reservations.append(reservation)
            
            # Paso 5: Auditoría innecesaria
            self._log_audit("Reserva creada exitosamente")
            
            return True
            
        except Exception as e:
            print(f"❌ Error en manager complejo: {e}")
            self._log_audit(f"Error: {e}")
            return False
    
    def cancel_reservation(self, index: int) -> bool:
        """Cancelación con lógica compleja"""
        try:
            if index < 0 or index >= len(self.reservations):
                print("❌ Índice inválido")
                return False
            
            self._log_audit(f"Cancelando reserva {index}")
            
            reservation = self.reservations[index]
            if reservation.cancel():
                self.reservations.pop(index)
                self._log_audit("Cancelación exitosa")
                return True
            
            return False
            
        except Exception as e:
            print(f"❌ Error en cancelación: {e}")
            return False
    
    def _log_audit(self, message: str) -> None:
        """
        Sistema de auditoría que no usamos
        
        Problema: Código que agrega complejidad sin valor real
        """
        self.audit_trail.append(message)
        # En un sistema real, esto iría a una base de datos,
        # pero aquí solo ocupa memoria sin propósito
    
    def get_reservation_count(self) -> int:
        """Contador simple envuelto en método innecesario"""
        return len(self.reservations)
    
    def get_audit_trail(self) -> List[str]:
        """Obtener auditoría que nadie consulta"""
        return self.audit_trail.copy()


# ==============================================================================
# DEMOSTRACIÓN DEL DISEÑO SOBREINGENIERIZADO
# ==============================================================================

def main():
    """Función principal de demostración"""
    
    print("\n--- Demostración del Diseño Sobreingenierizado ---")
    print("Observa la complejidad innecesaria y las dependencias que no se usan\n")
    print("-" * 80)
    
    try:
        # Crear servicios que en realidad no necesitamos todos
        email_service = EmailNotificationService()
        payment_gateway = StripePaymentGateway()
        
        # Manager con demasiadas dependencias
        manager_complex = ReservationManagerComplex(email_service, payment_gateway)
        
        # Crear varias reservas con todas las dependencias innecesarias
        print("\n🔹 CREANDO RESERVAS CON DISEÑO COMPLEJO:\n")
        
        reservations_data = [
            ("Sala-A", "juan.perez@techcorp.com", "2026-02-18 09:00", "2026-02-18 10:00"),
            ("Sala-B", "maria.garcia@techcorp.com", "2026-02-18 10:00", "2026-02-18 11:30"),
            ("Sala-A", "carlos.lopez@techcorp.com", "2026-02-18 14:00", "2026-02-18 15:00"),
        ]
        
        for room, user, start, end in reservations_data:
            reservation = MeetingRoomReservationComplex(
                room_id=room,
                user_id=user,
                start_time=start,
                end_time=end,
                notification_service=email_service,
                payment_gateway=payment_gateway
            )
            
            if manager_complex.create_reservation(reservation):
                print(f"✅ Proceso complejo completado para {room}\n")
            else:
                print(f"❌ Error en proceso complejo para {room}\n")
        
        print("-" * 80)
        print(f"\n📊 Total de reservas complejas: {manager_complex.get_reservation_count()}")
        print(f"📝 Entradas de auditoría: {len(manager_complex.get_audit_trail())}")
        
        # Cancelar una reserva para demostrar
        print("\n🔹 CANCELANDO UNA RESERVA:\n")
        if manager_complex.cancel_reservation(0):
            print("✅ Cancelación compleja exitosa\n")
        
        print("-" * 80)
        print(f"\n📊 Reservas restantes: {manager_complex.get_reservation_count()}")
        
    except Exception as e:
        print(f"❌ Error en demostración compleja: {e}")
    
    # Resumen de problemas
    print("\n\n" + "=" * 80)
    print("PROBLEMAS IDENTIFICADOS EN ESTE DISEÑO:")
    print("=" * 80)
    print("""
1. ❌ Interfaces genéricas sin necesidad real (IReservation, INotificationService)
2. ❌ Funcionalidades no requeridas (pagos, SMS, push notifications)
3. ❌ Dependencias innecesarias (PaymentGateway en un sistema gratuito)
4. ❌ Complejidad que dificulta el mantenimiento
5. ❌ Métodos no implementados que lanzan excepciones
6. ❌ Hooks y abstracciones "por si acaso"
7. ❌ Sistema de auditoría que nadie usa
8. ❌ Múltiples niveles de validación innecesarios
9. ❌ Código difícil de probar (muchos mocks necesarios)
10. ❌ Violación de YAGNI: "You Aren't Gonna Need It"
11. ❌ Violación de KISS: "Keep It Simple, Stupid"

💡 Consecuencias:
   • Desarrollo lento (3+ semanas para algo simple)
   • Difícil de entender para nuevos desarrolladores
   • Alto costo de mantenimiento
   • Muchos bugs potenciales
   • Baja satisfacción del equipo
    """)
    
    print("=" * 80)
    print("👉 Ahora ejecuta: python demo_2_simple.py")
    print("   Para ver cómo debe hacerse correctamente")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
