document.addEventListener("DOMContentLoaded", () => {

const grid = document.getElementById("grid");
const modal = document.getElementById("modal");
const modalContent = document.getElementById("modalContent");

let page = 1;
let loading = false;
let hasMore = true;

const cache = {};

// ✅ TRADUÇÃO COM CACHE
async function traduzir(texto) {
  if (cache[texto]) return cache[texto];

  try {
    const res = await fetch("https://translate.argosopentech.com/translate", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ q: texto, source: "es", target: "pt" })
    });

    const data = await res.json();
    cache[texto] = data.translatedText || texto;
    return cache[texto];

  } catch {
    return texto;
  }
}

// ✅ SCROLL INFINITO
window.addEventListener("scroll", () => {
  if (!loading && hasMore &&
      window.innerHeight + window.scrollY >= document.body.offsetHeight - 200) {
    loadCharacters();
  }
});

// ✅ LOAD PERSONAGENS
async function loadCharacters() {
  loading = true;

  const res = await fetch(`https://dragonball-api.com/api/characters?page=${page}`);
  const data = await res.json();

  renderCharacters(data.items || []);

  if (data.meta.currentPage >= data.meta.totalPages) {
    hasMore = false;
  } else {
    page++;
  }

  loading = false;
}

// ✅ RENDER CORRIGIDO (IMAGEM ✅)
function renderCharacters(chars) {
  chars.forEach(c => {

    const card = document.createElement("div");
    card.className = "card";

    const img = `<img src="${c.image}" alt="${c.name}">`; // ✅ FIX PRINCIPAL

    card.innerHTML = `
      ${img}
      <div class="card-content">
        <h3>${c.name}</h3>
        <p>${(c.description || "").substring(0, 100)}...</p>
      </div>
    `;

    card.addEventListener("click", (e) => {
      e.stopPropagation();
      openModal(c);
    });

    grid.appendChild(card);
  });

  animateCards();
}

// ✅ ANIMAÇÃO ENTRADA
function animateCards() {
  const cards = document.querySelectorAll(".card");

  cards.forEach((card, i) => {
    card.style.opacity = "0";
    card.style.transform = "translateY(40px)";

    setTimeout(() => {
      card.style.transition = "0.5s";
      card.style.opacity = "1";
      card.style.transform = "translateY(0)";
    }, i * 70);
  });
}

// ✅ MODAL TRANSFORMAÇÃO
async function openModal(c) {

  modal.style.display = "flex";
  modalContent.innerHTML = "⚡ TRANSFORMANDO...";

  modalContent.style.transform = "scale(1.3)";
  modalContent.style.filter = "brightness(2)";

  const desc = await traduzir(c.description || "");

  setTimeout(() => {
    modalContent.innerHTML = `
      <h2>🔥 ${c.name}</h2>
      <img src="${c.image}">
      <p>${desc}</p>
    `;

    modalContent.style.transform = "scale(1)";
    modalContent.style.filter = "none";
  }, 400);
}

// ✅ PLANETAS CORRIGIDO (IMAGEM ✅)
window.searchPlanets = async function () {
  hasMore = false;
  grid.innerHTML = "";

  const res = await fetch("/api/getPlanet");
  const data = await res.json();

  (data.api_response || []).forEach(p => {

    const card = document.createElement("div");
    card.className = "card";

    const img = `<img src="${p.image || "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa"}">`; // ✅ FIX

    card.innerHTML = `
      ${img}
      <div class="card-content">
        <h3>${p.name}</h3>
        <p>${p.isDestroyed ? "💥 Destruído" : "🌍 Habitável"}</p>
      </div>
    `;

    card.onclick = () => openPlanet(p);

    grid.appendChild(card);
  });

  animateCards();
};

// ✅ MODAL PLANETA CORRIGIDO
function openPlanet(p) {
  modal.style.display = "flex";

  modalContent.innerHTML = `
    <h2>🌌 ${p.name}</h2>
    <img src="${p.image || "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa"}">
    <p>${p.isDestroyed ? "💥 Planeta destruído" : "🌍 Planeta habitável"}</p>
  `;
}

// ✅ SHOCKWAVE
document.addEventListener("click", (e) => {
  const wave = document.createElement("div");

  wave.className = "shockwave";
  wave.style.left = e.clientX + "px";
  wave.style.top = e.clientY + "px";

  document.body.appendChild(wave);
  setTimeout(() => wave.remove(), 600);
});

// ✅ TRAIL DO MOUSE
document.addEventListener("mousemove", (e) => {
  const trail = document.createElement("div");

  trail.className = "trail";
  trail.style.left = e.clientX + "px";
  trail.style.top = e.clientY + "px";

  document.body.appendChild(trail);
  setTimeout(() => trail.remove(), 500);
});

// ✅ ESTRELAS
for (let i = 0; i < 100; i++) {
  const star = document.createElement("div");
  star.className = "star";

  star.style.top = Math.random() * 100 + "%";
  star.style.left = Math.random() * 100 + "%";

  document.body.appendChild(star);
}

// ✅ FECHAR MODAL
modal.onclick = () => modal.style.display = "none";

// ✅ RESET
window.resetScroll = function () {
  page = 1;
  hasMore = true;
  grid.innerHTML = "";
  loadCharacters();
};

// ✅ BUSCA PERSONAGEM
window.searchCharacters = async function () {
  hasMore = false;
  grid.innerHTML = "";

  const name = document.getElementById("name").value;

  const res = await fetch(`/api/getCharacter?name=${name}`);
  const data = await res.json();

  renderCharacters(data.api_response);
};

// INIT
loadCharacters();

});