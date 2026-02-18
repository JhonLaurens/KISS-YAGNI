#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de ayuda para ejecutar la presentación KISS + YAGNI
Ejecuta ambos diseños en secuencia con pausas para discusión
"""

import subprocess
import sys
import time

def print_banner(text, width=80, char="="):
    """Imprime un banner decorativo"""
    print("\n" + char * width)
    print(text.center(width))
    print(char * width + "\n")

def wait_for_enter(message="Presiona ENTER para continuar..."):
    """Espera que el usuario presione ENTER"""
    input(f"\n{message}\n")

def run_demo(script_name, description):
    """Ejecuta un script de demostración"""
    print_banner(description, char="=")
    time.sleep(1)
    
    try:
        subprocess.run([sys.executable, script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error ejecutando {script_name}: {e}")
        return False
    except FileNotFoundError:
        print(f"\n❌ No se encontró el archivo {script_name}")
        return False
    
    return True

def main():
    """Función principal de la presentación"""
    
    print_banner("🎓 PRESENTACIÓN: PRINCIPIOS KISS Y YAGNI", char="*")
    
    print("""
    Esta presentación muestra dos implementaciones del mismo sistema:
    
    1️⃣  Diseño Sobreingenierizado (Anti-Patrón) ❌
    2️⃣  Diseño Simple KISS+YAGNI (Patrón Correcto) ✅
    
    Cada demo se ejecutará y podrás pausar para discutir con la audiencia.
    """)
    
    wait_for_enter("Presiona ENTER para comenzar...")
    
    # ========================================================================
    # PARTE 1: Anti-Patrón
    # ========================================================================
    
    print_banner("PARTE 1: EL ANTI-PATRÓN", char="-")
    print("""
    📌 OBJETIVO: Mostrar cómo NO debe hacerse
    
    Verás un diseño con:
    • 8+ clases innecesarias
    • Interfaces abstractas sin justificación
    • Funcionalidades que nadie pidió (pagos, SMS, etc.)
    • Alta complejidad y bajo valor
    """)
    
    wait_for_enter("Presiona ENTER para ejecutar el diseño sobreingenierizado...")
    
    if not run_demo("demo_1_sobreingenieria.py", "🚫 DISEÑO SOBREINGENIERIZADO"):
        print("\n❌ No se pudo ejecutar la primera demo. Verifica que el archivo exista.")
        return
    
    print("\n" + "=" * 80)
    print("💡 PUNTOS DE DISCUSIÓN".center(80))
    print("=" * 80)
    print("""
    Pregunta a la audiencia:
    
    1. ¿Han visto diseños similares en sus proyectos?
    2. ¿Cuáles son los principales problemas que identifican?
    3. ¿Por qué creen que se crean estos diseños complejos?
    4. ¿Cuál es el costo de mantener este código?
    """)
    
    wait_for_enter("Presiona ENTER para continuar con la solución correcta...")
    
    # ========================================================================
    # PARTE 2: Patrón Correcto
    # ========================================================================
    
    print_banner("PARTE 2: LA SOLUCIÓN CORRECTA", char="-")
    print("""
    📌 OBJETIVO: Mostrar cómo DEBE hacerse
    
    Verás un diseño con:
    • Solo 4 clases necesarias
    • Sin abstracciones innecesarias
    • Solo funcionalidades requeridas
    • Alta simplicidad y alto valor
    """)
    
    wait_for_enter("Presiona ENTER para ejecutar el diseño simple KISS+YAGNI...")
    
    if not run_demo("demo_2_simple.py", "✅ DISEÑO SIMPLE KISS+YAGNI"):
        print("\n❌ No se pudo ejecutar la segunda demo. Verifica que el archivo exista.")
        return
    
    # ========================================================================
    # CONCLUSIÓN
    # ========================================================================
    
    print_banner("🎯 CONCLUSIÓN DE LA PRESENTACIÓN", char="*")
    print("""
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
    
    wait_for_enter("Presiona ENTER para finalizar la presentación...")
    
    print_banner("¡GRACIAS POR SU ATENCIÓN!", char="*")
    print("""
    📚 Recursos adicionales:
    
    • KISS_YAGNI_actividad.md - Documento completo de la actividad
    • README_DEMO.md - Guía de uso de las demos
    • demo_1_sobreingenieria.py - Código del anti-patrón
    • demo_2_simple.py - Código del patrón correcto
    
    🎯 Recuerda: Simple != Fácil, pero Simple = Mantenible
    """)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Presentación interrumpida por el usuario.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        sys.exit(1)
