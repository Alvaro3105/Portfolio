(() => {
  const themeMedia = window.matchMedia("(prefers-color-scheme: light)");
  let theme = localStorage.getItem("portfolio-theme") || (themeMedia.matches ? "light" : "dark");

  const applyTheme = (nextTheme, persist = true) => {
    theme = nextTheme;
    document.documentElement.dataset.theme = theme;
    if (persist) localStorage.setItem("portfolio-theme", theme);

    const light = theme === "light";
    document.querySelector('meta[name="theme-color"]')?.setAttribute("content", light ? "#f6f8fc" : "#080b12");
    const button = document.querySelector("#themeSwitch");
    if (button) {
      button.querySelector(".theme-icon").textContent = light ? "☾" : "☀";
      button.setAttribute("aria-label", light ? "Ativar modo escuro" : "Ativar modo claro");
      button.setAttribute("title", light ? "Ativar modo escuro" : "Ativar modo claro");
    }
  };

  // Aplica a preferência o quanto antes. O restante do comportamento original
  // continua em legacy-main.js para preservar PT/EN, terminal, menu e certificados.
  applyTheme(theme, false);

  const legacy = document.createElement("script");
  legacy.src = "assets/js/legacy-main.js";
  legacy.onload = () => {
    const actions = document.querySelector(".nav-actions");
    if (actions && !document.querySelector("#themeSwitch")) {
      const button = document.createElement("button");
      button.className = "theme-switch";
      button.id = "themeSwitch";
      button.type = "button";
      button.innerHTML = '<span class="theme-icon" aria-hidden="true">☀</span>';
      actions.insertBefore(button, document.querySelector("#langSwitch"));
      button.addEventListener("click", () => applyTheme(theme === "dark" ? "light" : "dark"));
    }

    const volunteerTitle = document.querySelector('[data-i18n="volunteerTitle"]');
    const volunteerCard = volunteerTitle?.closest(".timeline-item");
    if (volunteerCard && !volunteerCard.querySelector(".wcd-photo")) {
      const image = document.createElement("img");
      image.className = "timeline-photo wcd-photo";
      image.src = "assets/images/world-creativity-day.jpg";
      image.alt = "Álvaro como voluntário no World Creativity Day 2026";
      image.loading = "lazy";
      image.width = 640;
      image.height = 800;
      volunteerCard.prepend(image);
    }

    applyTheme(theme, false);
  };
  legacy.onerror = () => console.error("Não foi possível carregar os recursos principais do portfólio.");
  document.head.appendChild(legacy);

  themeMedia.addEventListener?.("change", (event) => {
    if (!localStorage.getItem("portfolio-theme")) applyTheme(event.matches ? "light" : "dark", false);
  });
})();
