# KISS & YAGNI — Presentación Interactiva

> Presentación académica sobre los principios **KISS** (Keep It Simple, Stupid) y **YAGNI** (You Aren't Gonna Need It) para la asignatura Arquitectura de Software I del ITM.

## Equipo

| Integrante                    | Rol                        |
| ----------------------------- | -------------------------- |
| Jhon Dayron Jaramillo Laurens | Desarrollo & Investigación |
| Angie Paola Meneses Calderon  | Análisis & Documentación   |
| Luis Fernando Zapata Castaño  | Diseño & Presentación      |

**Docente:** Johnathan Mauricio Calle Gallego  
**Instituto:** ITM — Instituto Tecnológico Metropolitano  
**Asignatura:** Arquitectura de Software I (190304005-1)

## Demo en vivo

Desplegado en Vercel: _[Agregar URL después del deploy]_

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

## Características

- **8 slides** con navegación completa (teclado, dots, botones)
- **Scroll-snap** full-page para experiencia tipo presentación
- **Simulador interactivo** KISS vs Over-Engineering con terminal
- **Dashboard de métricas** con 16 barras animadas
- **Tabla comparativa** con 8 métricas detalladas del caso TechCorp
- **Evaluación académica** con 4 criterios
- **Diseño glassmorphism** con orbes animados
- **100% responsive** (mobile, tablet, desktop)
- **Accesible** (ARIA labels, prefers-reduced-motion, focus visible)
- **Sin dependencias** (vanilla HTML/CSS/JS)

## Ejecutar localmente

### Opción 1: Abrir directamente

Abrir `src/index.html` en el navegador.

### Opción 2: Servidor local con Python

```bash
cd web-presentacion-kiss-yagni
python -m http.server 8000
```

Luego ir a: `http://localhost:8000/src/index.html`

### Opción 3: Live Server (VS Code)

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

## Tecnologías

- HTML5 semántico
- CSS3 (variables, grid, flexbox, glassmorphism, animaciones)
- JavaScript vanilla (IntersectionObserver, scroll-snap)
- Google Fonts (Inter, JetBrains Mono)

## Documentación académica

- [Diagramas C4](docs/DIAGRAMAS_C4.md) — Comparación arquitectónica usando modelo C4
- [Actividad KISS & YAGNI](docs/KISS_YAGNI_actividad.md) — Documento completo de la actividad

## Licencia

Proyecto académico — ITM 2026
