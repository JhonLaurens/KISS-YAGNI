# KISS & YAGNI — Presentación Interactiva

[![GitHub](https://img.shields.io/badge/GitHub-JhonLaurens%2FKISS--YAGNI-blue?logo=github)](https://github.com/JhonLaurens/KISS-YAGNI)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Vercel](https://img.shields.io/badge/Vercel-Ready-black?logo=vercel)](https://vercel.com)

> Presentación académica interactiva sobre los principios **KISS** (Keep It Simple, Stupid) y **YAGNI** (You Aren't Gonna Need It) para la asignatura Arquitectura de Software I del ITM.

🔗 **Repositorio:** [github.com/JhonLaurens/KISS-YAGNI](https://github.com/JhonLaurens/KISS-YAGNI)

## Equipo

| Integrante                    | Rol                        |
| ----------------------------- | -------------------------- |
| Jhon Dayron Jaramillo Laurens | Desarrollo & Investigación |
| Angie Paola Meneses Calderon  | Análisis & Documentación   |
| Luis Fernando Zapata Castaño  | Diseño & Presentación      |

**Docente:** Johnathan Mauricio Calle Gallego  
**Instituto:** ITM — Instituto Tecnológico Metropolitano  
**Asignatura:** Arquitectura de Software I (190304005-1)

## 🚀 Demo en vivo

🌐 **Desplegado en Vercel:** _[Agregar URL después del deploy]_

📹 **Vista previa:** Presentación de 8 slides con efectos glassmorphism, animaciones suaves y navegación completa por teclado/mouse.

## Estructura del proyecto

```
web-presentacion-kiss-yagni/
├── index.html              ← Entrada (redirige a src/)
├── vercel.json             ← Configuración de Vercel
├── README.md               ← Este archivo
├── assets/
│   └── img/
│       └── itm_logo.png    ← Logo del ITM
├── docs/
│   ├── DIAGRAMAS_C4.md     ← Diagramas C4 (Mermaid)
│   └── KISS_YAGNI_actividad.md  ← Documento de la actividad
└── src/
    ├── index.html           ← Presentación principal
    ├── styles.css           ← Estilos (CSS externo)
    └── script.js            ← Lógica de navegación y simulador
```

## ✨ Características

### 🎨 Diseño

- **Glassmorphism UI** con efectos de vidrio translúcido y blur
- **Orbes animados** en el background con gradientes vibrantes
- **Scroll-snap** full-page para experiencia tipo presentación
- **Animaciones suaves** con IntersectionObserver y CSS transitions
- **100% responsive** con breakpoints para mobile (480px), tablet (768px) y desktop (1024px)

### 🎯 Funcionalidad

- **8 slides completos** con navegación fluida
- **Simulador interactivo** que compara código KISS vs Over-Engineering con terminal animado
- **Dashboard de métricas** con 16 barras de progreso animadas
- **Tabla comparativa** detallada con 8 métricas del caso TechCorp
- **Navegación múltiple:** teclado (←→↑↓ Home End), dots laterales, botones, scroll natural
- **Scroll spy** que actualiza indicadores según la posición actual

### ♿ Accesibilidad

- **ARIA labels** completos en todos los controles interactivos
- **Soporte para `prefers-reduced-motion`** (desactiva animaciones si el usuario lo prefiere)
- **Focus visible** para navegación por teclado
- **Contraste WCAG AA** en todos los textos

### 🛠️ Técnico

- **Sin dependencias externas** — 100% vanilla HTML/CSS/JS
- **JavaScript modular** con IIFE pattern y funciones puras
- **CSS custom properties** para theming consistente
- **Optimizado para Vercel** con configuración de cache headers

## 📖 Contenido de la presentación

| Slide | Título                   | Descripción                                                                                      |
| ----- | ------------------------ | ------------------------------------------------------------------------------------------------ |
| **1** | Hero                     | Introducción con título principal, subtítulo y metadatos (equipo, docente, institución)          |
| **2** | Principios KISS & YAGNI  | Explicación conceptual de ambos principios con definiciones y fundamentos                        |
| **3** | Caso de Estudio TechCorp | Análisis del sistema de reportes de TechCorp mostrando la problemática real                      |
| **4** | Tabla Comparativa        | 8 métricas detalladas comparando el enfoque complejo vs. simple (LOC, tiempo, complejidad, etc.) |
| **5** | Simulador Interactivo    | Comparación lado a lado de código Over-Engineering vs KISS con terminal ejecutable               |
| **6** | Dashboard de Métricas    | 16 barras animadas mostrando mejoras en mantenibilidad, rendimiento, testing, etc.               |
| **7** | Evaluación Académica     | Rúbrica de evaluación con 4 criterios (claridad, aplicación, análisis, presentación)             |
| **8** | Equipo & Conclusiones    | Información del equipo y cierre de la presentación                                               |

## 💻 Ejecutar localmente

### Opción 1: Script de inicio rápido (Recomendado)

```bash
python start.py
```

Abre automáticamente el navegador en `http://localhost:8000`

### Opción 2: Abrir directamente

Abrir `src/index.html` en el navegador (algunas funcionalidades pueden requerir servidor HTTP).

### Opción 3: Servidor local con Python

```bash
cd web-presentacion-kiss-yagni
python -m http.server 8000
```

Luego ir a: `http://localhost:8000/src/index.html`

### Opción 4: Live Server (VS Code)

Click derecho en `src/index.html` → "Open with Live Server"

## Desplegar en Vercel

### Desde la CLI

```bash
cd web-presentacion-kiss-yagni
npx vercel --prod
```

### Desde el dashboard

1. Ir a [vercel.com](https://vercel.com)
2. Importar repositorio de GitHub
3. Configurar **Root Directory** como `web-presentacion-kiss-yagni`
4. Framework Preset: `Other`
5. Deploy

## Navegación

| Acción                | Control                     |
| --------------------- | --------------------------- |
| Siguiente slide       | `→` `↓` o botón "Siguiente" |
| Slide anterior        | `←` `↑` o botón "Anterior"  |
| Ir al inicio          | `Home`                      |
| Ir al final           | `End`                       |
| Ir a slide específico | Click en dot lateral        |
| Scroll natural        | Mouse wheel / touch         |

## 🔧 Tecnologías

### Frontend

- **HTML5 semántico** — Estructura accesible con roles ARIA
- **CSS3 moderno:**
  - Custom Properties (variables CSS) para design system
  - CSS Grid y Flexbox para layouts responsive
  - Glassmorphism (`backdrop-filter`, gradientes complejos)
  - Animaciones con `@keyframes` y transitions
  - Scroll-snap para navegación tipo presentación
- **JavaScript vanilla (ES6+):**
  - IntersectionObserver API para scroll spy y reveal animations
  - Event delegation para performance
  - IIFE pattern para encapsulación
  - DOM manipulation pura sin frameworks

### Tipografías

- **[Inter](https://fonts.google.com/specimen/Inter)** (300-900) — Font variable para UI y texto
- **[JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono)** (400-600) — Monospace para código

### Deploy

- **Vercel** — Hosting estático con CDN global y cache headers optimizados

## 📚 Documentación académica

- **[Diagramas C4](docs/DIAGRAMAS_C4.md)** — Comparación arquitectónica usando modelo C4 (Contexto, Contenedores, Componentes, Código)
- **[Actividad KISS & YAGNI](docs/KISS_YAGNI_actividad.md)** — Documento completo de la actividad con caso TechCorp, ejemplos de código y análisis detallado

## 🤝 Contribuir

Este es un proyecto académico, pero se aceptan sugerencias:

1. Fork el repositorio
2. Crea una rama: `git checkout -b feature/mejora`
3. Commit: `git commit -m "feat: descripción"`
4. Push: `git push origin feature/mejora`
5. Abre un Pull Request

## 📝 Licencia

Proyecto académico — ITM 2026  
**Código fuente:** Disponible bajo licencia educativa  
**Institución:** Instituto Tecnológico Metropolitano
