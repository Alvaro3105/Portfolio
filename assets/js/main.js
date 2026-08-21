(() => {
  const loadPortfolio = () => {
    const legacy = document.createElement("script");
    legacy.src = "assets/js/legacy-main.js";
    legacy.async = false;
    legacy.onload = () => {
      const volunteerTitle = document.querySelector('[data-i18n="volunteerTitle"]');
      const volunteerCard = volunteerTitle?.closest(".timeline-item");

      if (volunteerCard && !volunteerCard.querySelector(".wcd-photo")) {
        const image = document.createElement("img");
        image.className = "timeline-photo wcd-photo";
        image.src = "assets/images/world-creativity-day.jpg";
        image.alt = "Álvaro como voluntário no World Creativity Day 2026";
        image.loading = "lazy";
        image.width = 400;
        image.height = 250;
        image.style.objectPosition = "center 31%";
        volunteerCard.prepend(image);
      }
    };
    document.head.appendChild(legacy);
  };

  loadPortfolio();
})();