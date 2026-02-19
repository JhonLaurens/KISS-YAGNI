/**
 * KISS & YAGNI — Presentación Interactiva
 * Script principal de navegación y simulación
 */
(() => {
  "use strict";

  // ===== CONFIG =====
  const TOTAL_SLIDES = 8;
  let currentIndex = 0;

  const slidesContainer = document.getElementById("slidesContainer");
  const progressBar = document.getElementById("progressBar");
  const currentSlideEl = document.getElementById("currentSlide");
  const totalSlidesEl = document.getElementById("totalSlides");
  const prevBtn = document.getElementById("prevBtn");
  const nextBtn = document.getElementById("nextBtn");
  const navDotsContainer = document.getElementById("navDots");

  const slideLabels = [
    "Inicio",
    "Principios",
    "Caso TechCorp",
    "Comparativa",
    "Laboratorio",
    "Dashboard",
    "Evaluación",
    "Equipo",
  ];

  // ===== INIT =====
  totalSlidesEl.textContent = TOTAL_SLIDES;
  createNavDots();
  setupScrollSpy();
  setupRevealAnimations();
  setupKeyboardNav();
  setupButtonNav();

  // ===== NAV DOTS =====
  function createNavDots() {
    slideLabels.forEach((label, i) => {
      const dot = document.createElement("button");
      dot.className = "nav-dot" + (i === 0 ? " active" : "");
      dot.setAttribute("data-tooltip", label);
      dot.setAttribute("aria-label", `Ir a: ${label}`);
      dot.addEventListener("click", () => goToSlide(i));
      navDotsContainer.appendChild(dot);
    });
  }

  // ===== GO TO SLIDE =====
  window.goToSlide = function (index) {
    if (index < 0 || index >= TOTAL_SLIDES) return;
    currentIndex = index;
    const slide = document.getElementById(`slide-${index}`);
    if (slide) slide.scrollIntoView({ behavior: "smooth", block: "start" });
    updateUI();
  };

  function nextSlide() {
    if (currentIndex < TOTAL_SLIDES - 1) goToSlide(currentIndex + 1);
  }
  function prevSlide() {
    if (currentIndex > 0) goToSlide(currentIndex - 1);
  }

  // ===== UPDATE UI =====
  function updateUI() {
    currentSlideEl.textContent = currentIndex + 1;

    // Progress bar
    const pct = ((currentIndex + 1) / TOTAL_SLIDES) * 100;
    progressBar.style.width = `${pct}%`;

    // Dots
    navDotsContainer.querySelectorAll(".nav-dot").forEach((d, i) => {
      d.classList.toggle("active", i === currentIndex);
    });
  }

  // ===== SCROLL SPY (IntersectionObserver) =====
  function setupScrollSpy() {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const id = entry.target.id; // slide-N
            const idx = parseInt(id.split("-")[1], 10);
            if (!isNaN(idx)) {
              currentIndex = idx;
              updateUI();
            }
          }
        });
      },
      { root: null, threshold: 0.5 },
    );

    for (let i = 0; i < TOTAL_SLIDES; i++) {
      const s = document.getElementById(`slide-${i}`);
      if (s) observer.observe(s);
    }
  }

  // ===== REVEAL ANIMATIONS =====
  function setupRevealAnimations() {
    const revealObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("active");
            // Animate bar-fills inside chart cards
            if (entry.target.hasAttribute("data-chart")) {
              entry.target.querySelectorAll(".bar-fill").forEach((bar) => {
                bar.style.width = bar.dataset.width + "%";
              });
            }
          }
        });
      },
      { threshold: 0.15 },
    );

    document
      .querySelectorAll(".reveal")
      .forEach((el) => revealObserver.observe(el));
  }

  // ===== KEYBOARD NAV =====
  function setupKeyboardNav() {
    document.addEventListener("keydown", (e) => {
      switch (e.key) {
        case "ArrowDown":
        case "ArrowRight":
          e.preventDefault();
          nextSlide();
          break;
        case "ArrowUp":
        case "ArrowLeft":
          e.preventDefault();
          prevSlide();
          break;
        case "Home":
          e.preventDefault();
          goToSlide(0);
          break;
        case "End":
          e.preventDefault();
          goToSlide(TOTAL_SLIDES - 1);
          break;
      }
    });
  }

  // ===== BUTTON NAV =====
  function setupButtonNav() {
    prevBtn.addEventListener("click", prevSlide);
    nextBtn.addEventListener("click", nextSlide);
  }

  // ===== SIMULATOR =====
  window.runSimulation = function (mode) {
    const output = document.getElementById("terminalOutput");
    output.innerHTML = "";

    const logs =
      mode === "kiss"
        ? [
            { type: "log-success", msg: "✓ Iniciando backend simple..." },
            {
              type: "log-success",
              msg: "✓ Conectando a base de datos...",
            },
            {
              type: "log-success",
              msg: "✓ Cargando rutas (3 archivos)...",
            },
            {
              type: "log-success",
              msg: "✓ Configurando middleware básico...",
            },
            {
              type: "log-success",
              msg: "✓ Sistema listo en 2.3 segundos",
            },
            { type: "log-success", msg: "✓ Memoria: 145 MB | CPU: 8%" },
            {
              type: "log-success",
              msg: "✓ Server escuchando en puerto 3000",
            },
            {
              type: "log-success",
              msg: "🚀 KISS: Simple, rápido y funcional!",
            },
          ]
        : [
            { type: "", msg: "⚙️ Iniciando sistema complejo..." },
            { type: "", msg: "⏳ Cargando 230 dependencias..." },
            {
              type: "log-warning",
              msg: "⚠️ Inicializando 15 microservicios...",
            },
            {
              type: "log-warning",
              msg: "⚠️ Configurando service mesh...",
            },
            {
              type: "log-error",
              msg: "❌ Error en UserServiceFactoryAdapter",
            },
            {
              type: "log-warning",
              msg: "⚠️ Reintentar configuración...",
            },
            { type: "log-warning", msg: "⚠️ Memoria: 3.2 GB | CPU: 72%" },
            { type: "", msg: "⏳ Sistema listo en 47 segundos" },
            {
              type: "log-error",
              msg: "❌ 3 servicios fallaron al iniciar",
            },
            {
              type: "log-warning",
              msg: "⚠️ Sistema parcialmente operativo",
            },
            {
              type: "log-error",
              msg: "🔥 Over-Engineering: Complejo e inestable",
            },
          ];

    logs.forEach((log, i) => {
      setTimeout(() => {
        const line = document.createElement("div");
        line.className = "log-line";
        const time = new Date().toLocaleTimeString();
        line.innerHTML = `<span class="log-time">[${time}]</span><span class="${log.type}">${log.msg}</span>`;
        output.appendChild(line);
        // Auto-scroll
        const terminal = document.getElementById("terminal");
        terminal.scrollTop = terminal.scrollHeight;
      }, i * 350);
    });
  };

  // Prevent zoom on mobile
  document.addEventListener("gesturestart", (e) => e.preventDefault());
})();
