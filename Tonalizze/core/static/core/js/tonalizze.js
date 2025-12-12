document.addEventListener("DOMContentLoaded", () => {
    // ===============================
    // BOTÃO DE LIGAR / DESLIGAR
    // ===============================
    const toggleBtn = document.getElementById("toggle-filter-btn");
    const body = document.body;

    function applyToggle() {
        body.classList.toggle("no-filter");
        localStorage.setItem("filterOff", body.classList.contains("no-filter"));
    }

    if (localStorage.getItem("filterOff") === "true") {
        body.classList.add("no-filter");
    }

    toggleBtn.addEventListener("click", applyToggle);


    // ===============================
    // PRESETS DE DALTONISMO
    // ===============================
    const presets = {
        deuteranopia: { tone1: -20, tone2: 0.8, tone3: 1.1 },
        protanopia: { tone1: 25, tone2: 0.7, tone3: 1.2 },
        tritanopia: { tone1: 120, tone2: 0.9, tone3: 1.0 },
        normal: { tone1: 0, tone2: 1, tone3: 1 }
    };

    const presetSelect = document.getElementById("preset-select");

    presetSelect.addEventListener("change", () => {
        const p = presets[presetSelect.value];
        if (!p) return;

        document.documentElement.style.setProperty("--tone1", p.tone1 + "deg");
        document.documentElement.style.setProperty("--tone2", p.tone2);
        document.documentElement.style.setProperty("--tone3", p.tone3);

        localStorage.setItem("tone1", p.tone1);
        localStorage.setItem("tone2", p.tone2);
        localStorage.setItem("tone3", p.tone3);
    });


    // ===============================
    // APLICAR VALORES DO LOCALSTORAGE AO CARREGAR
    // ===============================
    if (localStorage.getItem("tone1")) {
        document.documentElement.style.setProperty("--tone1", localStorage.getItem("tone1") + "deg");
        document.documentElement.style.setProperty("--tone2", localStorage.getItem("tone2"));
        document.documentElement.style.setProperty("--tone3", localStorage.getItem("tone3"));
    }


    // ===============================
    // PREVIEW AO MEXER NOS SLIDERS
    // ===============================
    const s1 = document.querySelector('input[name="tonalidade_1"]');
    const s2 = document.querySelector('input[name="tonalidade_2"]');
    const s3 = document.querySelector('input[name="tonalidade_3"]');

    const preview = document.createElement("div");
    preview.id = "preview-box";
    const form = document.querySelector("form.slider-form");
    
    if (form) form.appendChild(preview);

    function updatePreview() {
        if (!s1 || !s2 || !s3) return;

        document.documentElement.style.setProperty("--tone1", s1.value + "deg");
        document.documentElement.style.setProperty("--tone2", s2.value);
        document.documentElement.style.setProperty("--tone3", s3.value);
    }

    [s1, s2, s3].forEach(slider => {
        if (slider) slider.addEventListener("input", updatePreview);
    });
});
