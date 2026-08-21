(() => {
  const legacy = document.createElement("script");
  legacy.src = "assets/js/legacy-main.js";

  legacy.onload = () => {
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
  };

  legacy.onerror = () => console.error("Não foi possível carregar os recursos principais do portfólio.");
  document.head.appendChild(legacy);
})();
