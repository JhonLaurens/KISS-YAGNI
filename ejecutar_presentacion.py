#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de ayuda para ejecutar la presentación KISS + YAGNI
Ejecuta ambos diseños en secuencia con pausas para discusión.
Aplicando POO para estructura clara y mantenible.
"""

import subprocess
import sys
import time
from typing import Optional


class InterfazPresentacion:
    """
    Clase responsable de la interfaz de usuario de la presentación.
    Maneja la visualización de banners, mensajes y espera de entrada.
    """
    
    def __init__(self, ancho: int = 80):
        """
        Inicializa la interfaz de presentación.
        
        Args:
            ancho: Ancho en caracteres de los banners
        """
        self.ancho = ancho
    
    def mostrar_banner(self, texto: str, caracter: str = "=") -> None:
        """
        Imprime un banner decorativo.
        
        Args:
            texto: Texto a mostrar en el banner
            caracter: Carácter para el borde del banner
        """
        print("\n" + caracter * self.ancho)
        print(texto.center(self.ancho))
        print(caracter * self.ancho + "\n")
    
    def esperar_enter(self, mensaje: str = "Presiona ENTER para continuar...") -> None:
        """
        Espera que el usuario presione ENTER.
        
        Args:
            mensaje: Mensaje a mostrar antes de esperar
        """
        input(f"\n{mensaje}\n")
    
    def mostrar_mensaje(self, mensaje: str) -> None:
        """
        Muestra un mensaje formateado.
        
        Args:
            mensaje: Mensaje a mostrar
        """
        print(mensaje)


class EjecutorDemo:
    """
    Clase responsable de ejecutar scripts de demostración.
    Encapsula la lógica de ejecución y manejo de errores.
    """
    
    def ejecutar_script(self, nombre_script: str, descripcion: str, interfaz: InterfazPresentacion) -> bool:
        """
        Ejecuta un script de Python y maneja errores.
        
        Args:
            nombre_script: Nombre del archivo Python a ejecutar
            descripcion: Descripción de la demo
            interfaz: Instancia de InterfazPresentacion para mostrar mensajes
        
        Returns:
            True si la ejecución fue exitosa, False en caso contrario
        """
        interfaz.mostrar_banner(descripcion, caracter="=")
        time.sleep(1)
        
        try:
            subprocess.run([sys.executable, nombre_script], check=True)
            return True
        except subprocess.CalledProcessError as e:
            interfaz.mostrar_mensaje(f"\n❌ Error ejecutando {nombre_script}: {e}")
            return False
        except FileNotFoundError:
            interfaz.mostrar_mensaje(f"\n❌ No se encontró el archivo {nombre_script}")
            return False


class GestorPresentacion:
    """
    Clase principal que gestiona el flujo de la presentación KISS+YAGNI.
    Coordina la interfaz y la ejecución de demos.
    """
    
    def __init__(self):
        """Inicializa el gestor de presentación."""
        self.interfaz = InterfazPresentacion(ancho=80)
        self.ejecutor = EjecutorDemo()
    
    def mostrar_introduccion(self) -> None:
        """Muestra la introducción de la presentación."""
        self.interfaz.mostrar_banner("🎓 PRESENTACIÓN: PRINCIPIOS KISS Y YAGNI", caracter="*")
        
        self.interfaz.mostrar_mensaje("""
    Esta presentación muestra dos implementaciones del mismo sistema:
    
    1️⃣  Diseño Sobreingenierizado (Anti-Patrón) ❌
    2️⃣  Diseño Simple KISS+YAGNI (Patrón Correcto) ✅
    
    Cada demo se ejecutará y podrás pausar para discutir con la audiencia.
    """)
        
        self.interfaz.esperar_enter("Presiona ENTER para comenzar...")
    
    def ejecutar_parte_antipatron(self) -> bool:
        """
        Ejecuta la primera parte: el anti-patrón.
        
        Returns:
            True si la ejecución fue exitosa, False en caso contrario
        """
        self.interfaz.mostrar_banner("PARTE 1: EL ANTI-PATRÓN", caracter="-")
        
        self.interfaz.mostrar_mensaje("""
    📌 OBJETIVO: Mostrar cómo NO debe hacerse
    
    Verás un diseño con:
    • 8+ clases innecesarias
    • Interfaces abstractas sin justificación
    • Funcionalidades que nadie pidió (pagos, SMS, etc.)
    • Alta complejidad y bajo valor
    """)
        
        self.interfaz.esperar_enter("Presiona ENTER para ejecutar el diseño sobreingenierizado...")
        
        exito = self.ejecutor.ejecutar_script(
            "demo_1_sobreingenieria.py",
            "🚫 DISEÑO SOBREINGENIERIZADO",
            self.interfaz
        )
        
        if not exito:
            self.interfaz.mostrar_mensaje("\n❌ No se pudo ejecutar la primera demo. Verifica que el archivo exista.")
            return False
        
        self._mostrar_puntos_discusion_antipatron()
        return True
    
    def _mostrar_puntos_discusion_antipatron(self) -> None:
        """Muestra los puntos de discusión después del anti-patrón (método privado)."""
        print("\n" + "=" * 80)
        print("💡 PUNTOS DE DISCUSIÓN".center(80))
        print("=" * 80)
        
        self.interfaz.mostrar_mensaje("""
    Pregunta a la audiencia:
    
    1. ¿Han visto diseños similares en sus proyectos?
    2. ¿Cuáles son los principales problemas que identifican?
    3. ¿Por qué creen que se crean estos diseños complejos?
    4. ¿Cuál es el costo de mantener este código?
    """)
        
        self.interfaz.esperar_enter("Presiona ENTER para continuar con la solución correcta...")
    
    def ejecutar_parte_solucion(self) -> bool:
        """
        Ejecuta la segunda parte: la solución correcta.
        
        Returns:
            True si la ejecución fue exitosa, False en caso contrario
        """
        self.interfaz.mostrar_banner("PARTE 2: LA SOLUCIÓN CORRECTA", caracter="-")
        
        self.interfaz.mostrar_mensaje("""
    📌 OBJETIVO: Mostrar cómo DEBE hacerse
    
    Verás un diseño con:
    • Solo 4 clases necesarias
    • Sin abstracciones innecesarias
    • Solo funcionalidades requeridas
    • Alta simplicidad y alto valor
    """)
        
        self.interfaz.esperar_enter("Presiona ENTER para ejecutar el diseño simple KISS+YAGNI...")
        
        exito = self.ejecutor.ejecutar_script(
            "demo_2_simple.py",
            "✅ DISEÑO SIMPLE KISS+YAGNI",
            self.interfaz
        )
        
        if not exito:
            self.interfaz.mostrar_mensaje("\n❌ No se pudo ejecutar la segunda demo. Verifica que el archivo exista.")
            return False
        
        return True
    
    def mostrar_conclusion(self) -> None:
        """Muestra la conclusión de la presentación."""
        self.interfaz.mostrar_banner("🎯 CONCLUSIÓN DE LA PRESENTACIÓN", caracter="*")
        
        self.interfaz.mostrar_mensaje("""
    📊 COMPARACIÓN FINAL:
    
    ┌────────────────────────────┬──────────────────┬─────────────────┐
    │ ASPECTO                    │ SOBREINGENIERIZADO │ SIMPLE (KISS+YAGNI) │
    ├────────────────────────────┼──────────────────┼─────────────────┤
    │ Clases                     │ 8+               │ 4               │
    │ Tiempo de desarrollo       │ 3 semanas        │ 1 semana        │
    │ Facilidad de mantenimiento │ Baja             │ Alta            │
    │ Bugs potenciales           │ Muchos           │ Pocos           │
    │ Satisfacción del equipo    │ Baja             │ Alta            │
    └────────────────────────────┴──────────────────┴─────────────────┘
    
    ✨ PRINCIPIOS CLAVE:
    
    • KISS: Mantén las cosas simples, siempre que sea posible
    • YAGNI: No implementes lo que no necesitas HOY
    • Es más fácil agregar complejidad después, que quitarla
    
    💡 REGLA DE ORO:
    
    Agrega complejidad SOLO cuando tengas:
    ✓ Un requisito REAL documentado
    ✓ Al menos 2-3 casos de uso concretos
    ✓ Justificación del costo-beneficio
    """)
        
        print("\n" + "=" * 80)
        print("❓ PREGUNTAS Y RESPUESTAS".center(80))
        print("=" * 80)
        print("\nAhora es momento de responder preguntas de la audiencia.\n")
        
        self.interfaz.esperar_enter("Presiona ENTER para finalizar la presentación...")
    
    def mostrar_cierre(self) -> None:
        """Muestra el mensaje de cierre."""
        self.interfaz.mostrar_banner("¡GRACIAS POR SU ATENCIÓN!", caracter="*")
        
        self.interfaz.mostrar_mensaje("""
    📚 Recursos adicionales:
    
    • KISS_YAGNI_actividad.md - Documento completo de la actividad
    • README_DEMO.md - Guía de uso de las demos
    • demo_1_sobreingenieria.py - Código del anti-patrón
    • demo_2_simple.py - Código del patrón correcto
    
    🎯 Recuerda: Simple != Fácil, pero Simple = Mantenible
    """)
    
    def ejecutar(self) -> None:
        """
        Método principal que ejecuta toda la presentación en orden.
        Orquesta el flujo completo de la presentación.
        """
        self.mostrar_introduccion()
        
        # Ejecutar primera parte (anti-patrón)
        if not self.ejecutar_parte_antipatron():
            return
        
        # Ejecutar segunda parte (solución)
        if not self.ejecutar_parte_solucion():
            return
        
        # Mostrar conclusión y cierre
        self.mostrar_conclusion()
        self.mostrar_cierre()


def main():
    """Función principal del programa."""
    try:
        # Crear instancia del gestor y ejecutar la presentación
        gestor = GestorPresentacion()
        gestor.ejecutar()
    except KeyboardInterrupt:
        print("\n\n⚠️  Presentación interrumpida por el usuario.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
