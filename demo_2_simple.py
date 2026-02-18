#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Reservas de Salas - DISEÑO SIMPLE
=============================================

Este script demuestra un diseño que APLICA los principios KISS y YAGNI:
- Código simple y directo
- Solo funcionalidades necesarias
- Fácil de entender y mantener

✅ PATRÓN CORRECTO - SEGUIR ESTE DISEÑO ✅

Autor: Demo para exposición de Arquitectura de Software
Fecha: 2026-02-17
"""

from typing import List, Dict
from datetime import datetime


print("=" * 80)
print("DISEÑO SIMPLE - Aplicando KISS y YAGNI")
print("=" * 80)
print("\n✅ Este es el diseño CORRECTO\n")


# ==============================================================================
# CLASES SIMPLES Y DIRECTAS
# ==============================================================================

class MeetingRoomReservation:
    """
    Reserva de sala de reuniones - Clase simple con solo lo necesario
    
    ✅ Aplica KISS: Estructura simple y directa
    ✅ Aplica YAGNI: Solo tiene lo que necesitamos HOY
    
    No tiene:
    - Interfaces abstractas innecesarias
    - Métodos de pago (las salas son gratuitas)
    - Hooks complejos
    - Validaciones excesivas
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
    
    ✅ Aplica KISS: Una clase, una responsabilidad clara
    ✅ Aplica YAGNI: Solo email, sin SMS ni push (no los necesitamos aún)
    
    Si en el futuro necesitamos SMS o push, agregaremos clases entonces.
    No hay interfaz abstracta porque no tenemos múltiples implementaciones.
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
    Repositorio simple para almacenar reservas
    
    ✅ Aplica KISS: Implementación directa sin ORM complejo
    ✅ Aplica YAGNI: Almacenamiento en memoria (suficiente para la demo)
    
    En producción, aquí iría una base de datos real.
    Lo implementamos cuando sea necesario, no antes.
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
    
    ✅ Aplica KISS: Lógica clara y fácil de seguir
    ✅ Aplica YAGNI: Solo operaciones necesarias (crear, cancelar, consultar)
    
    No tiene:
    - Procesamiento de pagos (no se necesita)
    - Sistema de auditoría (no se necesita)
    - Hooks complejos (no se necesitan)
    - Validaciones excesivas (solo lo básico)
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
        
        Proceso simple:
        1. Validar datos básicos
        2. Crear objeto de reserva
        3. Guardar en repositorio
        4. Notificar usuario
        
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
            # Validación simple y directa
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

def main():
    """Función principal de demostración"""
    
    print("\n--- Demostración del Diseño Simple ---")
    print("Observa la claridad y simplicidad del código\n")
    print("-" * 80)
    
    # Inicializar componentes - Solo 3 líneas, muy claro
    repository = ReservationRepository()
    notifier = EmailNotifier()
    service = ReservationService(repository, notifier)
    
    # Crear varias reservas
    print("\n🔹 CREANDO RESERVAS:\n")
    
    reservas_demo = [
        ("Sala-A", "juan.perez@techcorp.com", "2026-02-18 09:00", "2026-02-18 10:00", "Juan Pérez"),
        ("Sala-B", "maria.garcia@techcorp.com", "2026-02-18 10:00", "2026-02-18 11:30", "María García"),
        ("Sala-A", "carlos.lopez@techcorp.com", "2026-02-18 14:00", "2026-02-18 15:00", "Carlos López"),
        ("Sala-C", "ana.martinez@techcorp.com", "2026-02-18 11:00", "2026-02-18 12:00", "Ana Martínez"),
    ]
    
    for room, user, start, end, name in reservas_demo:
        service.create_reservation(room, user, start, end, name)
        print()
    
    print("-" * 80)
    
    # Consultar reservas por sala
    print("\n🔹 CONSULTANDO RESERVAS POR SALA:\n")
    sala_a_reservations = service.get_room_reservations("Sala-A")
    print(f"📍 Sala-A tiene {len(sala_a_reservations)} reserva(s):")
    for res in sala_a_reservations:
        print(f"   {res}")
    
    # Consultar reservas por usuario
    print("\n🔹 CONSULTANDO RESERVAS POR USUARIO:\n")
    user_reservations = service.get_user_reservations("juan.perez@techcorp.com")
    print(f"👤 Juan Pérez tiene {len(user_reservations)} reserva(s):")
    for res in user_reservations:
        print(f"   {res}")
    
    # Cancelar una reserva
    print("\n🔹 CANCELANDO UNA RESERVA:\n")
    service.cancel_reservation("Sala-A", "juan.perez@techcorp.com")
    
    # Mostrar todas las reservas restantes
    print("\n🔹 RESUMEN FINAL DE TODAS LAS RESERVAS:\n")
    all_reservations = service.get_all_reservations()
    print(f"📊 Total de reservas activas: {len(all_reservations)}")
    for res in all_reservations:
        print(f"   {res}")
    
    print("\n" + "-" * 80)
    
    # Resumen de beneficios
    print("\n\n" + "=" * 80)
    print("BENEFICIOS DE ESTE DISEÑO SIMPLE:")
    print("=" * 80)
    print("""
✅ KISS (Keep It Simple, Stupid):
   • Solo 4 clases vs 8+ del diseño complejo
   • Código fácil de leer y entender
   • Sin abstracciones innecesarias
   • Flujo de ejecución claro y directo
   • Menos líneas de código (~150 vs ~300)

✅ YAGNI (You Aren't Gonna Need It):
   • Sin funcionalidad de pagos (no se necesita)
   • Sin SMS ni push notifications (no se necesitan)
   • Sin sistema de auditoría (no se necesita)
   • Sin hooks complejos (no se necesitan)
   
✅ Resultados:
   • Desarrollo en 1 semana vs 3+ semanas
   • Fácil de mantener y extender
   • Menos bugs potenciales
   • Nuevos desarrolladores entienden rápido
   • Tests más simples de escribir
   • Equipo más productivo y feliz
    """)
    
    print("=" * 80)
    print("COMPARACIÓN FINAL")
    print("=" * 80)
    
    comparison_table = """
┌─────────────────────────────┬─────────────────────────┬──────────────────────────┐
│ ASPECTO                     │ DISEÑO SOBREINGENIERIZADO │ DISEÑO SIMPLE (KISS+YAGNI)│
├─────────────────────────────┼─────────────────────────┼──────────────────────────┤
│ Número de clases            │ 8+ clases               │ 4 clases                 │
│ Interfaces abstractas       │ 3 interfaces            │ 0 interfaces             │
│ Líneas de código            │ ~300+ líneas            │ ~150 líneas              │
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
    print("¿CUÁNDO AGREGAR COMPLEJIDAD?")
    print("=" * 80)
    print("""
Agrega abstracciones y funcionalidades SOLO cuando:

1. 📋 Existe un requisito REAL y documentado
2. 🔄 Ya tienes al menos 2-3 casos de uso concretos
3. 💰 El costo de no tenerlo es mayor que el costo de implementarlo
4. 📊 Tienes datos que justifican la inversión

Ejemplos para este sistema:
• ¿Agregar pagos? → Cuando tengas salas premium de pago
• ¿Agregar SMS? → Cuando los usuarios lo soliciten activamente  
• ¿Agregar auditoría? → Cuando sea requisito de compliance

RECUERDA: Es más fácil agregar complejidad cuando se necesita,
que eliminar complejidad innecesaria.
    """)
    
    print("=" * 80)
    print("💡 Preguntas para discusión:")
    print("=" * 80)
    print("""
1. ¿Qué otras funcionalidades innecesarias has visto en proyectos reales?
2. ¿Cómo balanceas simplicidad con preparación para el futuro?
3. ¿Cuándo está justificado un diseño más complejo desde el inicio?
4. ¿Cómo convences a un equipo de que "simple" no significa "malo"?
5. ¿Qué métricas usas para detectar sobreingeniería?
    """)
    
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
